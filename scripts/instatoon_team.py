"""Start bounded Paseo roles; the calling session retains image generation tools."""
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TEAM = ROOT / '.agents/teams/instatoon.json'
CLI = ROOT / '.tools/paseo/node_modules/.bin/paseo.cmd'
ENTRY = ROOT / '.tools/paseo/node_modules/@getpaseo/cli/bin/paseo'


def paseo(*args: str) -> str:
    env = os.environ.copy()
    env.pop('PASEO_HOST', None)
    env['PASEO_HOME'] = str(ROOT / '.paseo-local')
    env['PATH'] = str(CLI.parent) + os.pathsep + env.get('PATH', '')
    node = shutil.which('node')
    if not node:
        raise RuntimeError('Node.js is required.')
    # Invoke Node directly: cmd.exe can truncate multiline prompts at newlines.
    result = subprocess.run([node, str(ENTRY), *args], cwd=ROOT, env=env,
                            capture_output=True, encoding='utf-8', errors='replace')
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=['check', 'plan', 'qa', 'caption'])
    parser.add_argument('--job', type=Path, help='Existing docs/jobs/<job-id> directory')
    parser.add_argument('--image', type=Path, action='append', default=[],
                        help='Attach target, reference and anchor images; repeat as needed')
    parser.add_argument('--report', default='qa-01-v1.md', help='Unique QA report filename')
    parser.add_argument('--skill', default='fantasy-party-insta-toon',
                        help='Selected skill directory under skills/')
    args = parser.parse_args()
    if not CLI.is_file():
        parser.error('Install Paseo using docs/agent-team-workflow.md first.')
    team = json.loads(TEAM.read_text(encoding='utf-8-sig'))
    if args.phase == 'check':
        print(paseo('--version').strip())
        print(paseo('daemon', 'status').strip())
        print(paseo('plugin', 'ls').strip())
        return
    if args.job is None:
        parser.error('--job is required')
    job = (ROOT / args.job).resolve()
    if not job.is_relative_to(ROOT / 'docs/jobs') or not (job / 'request.md').is_file():
        parser.error('Job must be inside docs/jobs and contain request.md.')
    report = Path(args.report)
    if report.name != args.report or not args.report.endswith('.md'):
        parser.error('--report must be a Markdown filename without directories')
    images = [p.resolve() for p in args.image]
    for image in images:
        if not image.is_file():
            parser.error(f'Image not found: {image}')
    if args.phase in ('qa', 'caption') and not images:
        parser.error('Attach actual images with --image for qa/caption.')
    output = job / {'plan': 'plan.md', 'qa': args.report, 'caption': 'caption.md'}[args.phase]
    if output.exists():
        parser.error(f'Preserve existing output; use a new job/report: {output}')
    if args.phase != 'plan' and not (job / 'plan.md').is_file():
        parser.error('plan.md is required before QA or caption.')
    role_name = 'visual-qa' if args.phase == 'qa' else 'editor'
    skill = (ROOT / 'skills' / args.skill).resolve()
    if not skill.is_relative_to(ROOT / 'skills') or not (skill / 'SKILL.md').is_file():
        parser.error('--skill must name an existing workspace skill')
    role = next(r for r in team['roles'] if r['name'] == role_name)
    # A stopped daemon is recoverable; do not install packages or alter permissions here.
    try:
        paseo('workspace', 'ls', '--json')
    except RuntimeError:
        paseo('daemon', 'start', '--timeout', '45')
    workspaces = json.loads(paseo('workspace', 'ls', '--json'))
    matches = [w for w in workspaces
               if w.get('name', w.get('title')) == team['orchestrator']['workspace']
               and Path(w.get('cwd', w.get('path', ''))).resolve() == ROOT]
    if len(matches) != 1:
        raise RuntimeError('Expected exactly one instatoon workspace for this checkout; see setup docs.')
    workspace_id = matches[0].get('id', matches[0].get('workspaceId'))
    task = {
        'plan': 'Read request.md. Write the page plan only. Do not generate images or captions yet.',
        'qa': 'Read request.md and plan.md. Inspect every attached actual image, compare references/anchor and target identified in request.md. Write PASS/REVISE/BLOCKED_TOOL with concrete corrections. Do not change images.',
        'caption': 'Read request.md, plan.md and available QA reports. Inspect attached completed images. Write the final 100–500 character Instagram caption, supplementing omitted facts without inventing claims.',
    }[args.phase]
    prompt = (f'{role["instructions"]}\nJob directory: {job}\n'
              f'Only output file you may write: {output}\n{task}\n'
              'Do not start other agents. Report tool limitations honestly. '
              'Other workers share this checkout; preserve their files and changes.')
    prompt += '\n\nRequest (authoritative job data):\n' + (job / 'request.md').read_text(encoding='utf-8-sig')
    if args.phase != 'plan':
        prompt += '\n\nPage plan:\n' + (job / 'plan.md').read_text(encoding='utf-8-sig')
    prompt += '\n\nWorkspace rules:\n' + (ROOT / 'AGENTS.md').read_text(encoding='utf-8-sig')
    prompt += '\n\nExecution workflow:\n' + (ROOT / 'docs/agent-team-workflow.md').read_text(encoding='utf-8-sig')
    prompt += '\n\nSelected skill:\n' + (skill / 'SKILL.md').read_text(encoding='utf-8-sig')
    qa_checklist = skill / 'references/qa-checklist.md'
    if args.phase == 'qa' and qa_checklist.is_file():
        prompt += '\n\nQA checklist:\n' + qa_checklist.read_text(encoding='utf-8-sig')
    if args.phase == 'caption':
        for qa_report in sorted(job.glob('qa-*.md')):
            prompt += f'\n\n{qa_report.name}:\n' + qa_report.read_text(encoding='utf-8-sig')
    prompt += '\nIf shell access fails, use apply_patch for the assigned output. If all file tools fail, return the complete artifact text in the final response and explicitly report that saving failed; the caller can save it. Do not ask the user for content already included above.'
    command = ['run', '--workspace', workspace_id, '--provider',
               f'{role["provider"]}/{role["model"]}', '--mode', 'auto-review',
               '--title', f'{role_name}-{job.name}', '--label', f'role={role_name}',
               '--no-wait', '--json']
    for image in images:
        command.extend(['--image', str(image)])
    command.append(prompt)
    print(paseo(*command))
    print(f'Expected artifact: {output}')


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError, OSError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)
