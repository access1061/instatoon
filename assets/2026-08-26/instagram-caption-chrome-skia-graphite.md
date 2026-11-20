크롬이 버벅인다면 PC 교체 전에 그래픽 설정부터 확인해 볼 것. `chrome://settings/system`에서 그래픽 가속을 켠 뒤, `chrome://flags`에서 Skia를 검색해 `Skia Graphite`를 Enabled로 바꾸고 재시작하면 됨.

적용 여부는 `chrome://gpu`의 `Skia Graphite: Enabled`로 확인. 공식 M3 MotionMark 테스트에서는 약 15% 향상됐지만 실제 체감은 PC와 사이트에 따라 다름. 화면 깨짐이나 속도 저하가 생기면 Default 또는 Disabled로 되돌리고 재시작 권장.

#크롬속도향상 #SkiaGraphite #크롬설정 #하드웨어가속 #크롬최적화
