---
name: git-account-switch
description: Show and manage the active GitHub CLI account for Git operations. Use when the user asks to switch GitHub accounts, check which account is active, authenticate a second account, or push a repository with a different GitHub identity.
---

# Git Account Switch

Use GitHub CLI account commands and keep the distinction clear between stored accounts and the currently active account.

## Check accounts

Run:

```powershell
gh auth status
```

This lists stored accounts for `github.com` and marks the active one. An account can be listed but still have an expired or invalid token.

## Switch the active account

Show the exact command using the requested username:

```powershell
gh auth switch -h github.com -u USERNAME
```

Examples:

```powershell
gh auth switch -h github.com -u access1061
gh auth switch -h github.com -u newtype-studio
```

After switching, verify with `gh auth status` before pushing.

## Add or repair an account

If the account is missing or its token is invalid, use:

```powershell
gh auth login -h github.com
```

Do not ask the user to paste an access token into chat. Let the interactive GitHub CLI flow handle authentication.

## Repository push guidance

When the user asks to push with a particular account:

1. Run `gh auth status`.
2. Switch with `gh auth switch -h github.com -u USERNAME` if needed.
3. Confirm the repository remote and intended files before committing.
4. Run `git push` only after the active account is verified.

If authentication is invalid, explain the exact login command and stop before pushing.
