1차시. Raspberry Pi Pico 2W 시작하기 — 실습 코드

[파일 목록]
config.py           Wi-Fi 정보 (Pico 2W 내부에 저장)
01_blink.py         실습3  LED 무한 점멸
02_repeat.py        실습4  횟수 지정 반복
03_led_pattern.py   실습5  함수로 LED 패턴
03b_sos.py          미션   모스부호 SOS (심화)
04_wifi_scan.py     실습6  주변 Wi-Fi 검색
05_wifi_connect.py  실습7  Wi-Fi 연결 및 IP 확인
bonus_temperature.py 보너스 내장 온도센서

[main.py 자동 실행 실습]
05_wifi_connect.py를 Thonny에서 "Raspberry Pi Pico"에 main.py라는 이름으로 저장합니다.
USB를 PC가 아닌 보조배터리/충전기에 꽂아 LED로 연결 상태를 확인합니다.
실습 후에는 Pico 내부의 main.py 이름을 바꾸거나 삭제하세요.

[주의]
- config.py의 SSID/PASSWORD를 실제 수업용 공유기 정보로 바꾸세요.
- 반드시 "Pico 2 W"용 MicroPython 펌웨어를 설치해야 합니다.

[Thonny 설치]
https://thonny.org/
>> Intel/AMD 설치 파일,약 30MB	  " thonny-5.0.1-x64.exe "


[micropython.org에서 RPI_PICO2_W 안정 버전 .uf2 다운로드]
https://micropython.org/resources/firmware/RPI_PICO2_W-20260824-v1.29.0.uf2
