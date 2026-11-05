# 05_wifi_connect.py — Wi-Fi 연결 후 IP 주소 확인
# 준비: config.py를 Pico 2W 내부에 먼저 저장하세요.
# LED 상태  깜빡임: 연결 중 / 켜짐: 연결 성공 / 꺼짐: 연결 실패
import network
import time
from machine import Pin
import config

led = Pin("LED", Pin.OUT)

# 국가 설정 (한국 무선 채널 사용) — 펌웨어에 따라 없을 수 있어 예외 처리
try:
    network.country("KR")
except Exception:
    pass

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print("Wi-Fi 연결 시도 중:", config.SSID)
    wlan.connect(config.SSID, config.PASSWORD)

    for i in range(20):          # 최대 약 10초 대기
        if wlan.isconnected():
            break
        led.toggle()
        print(".", end="")
        time.sleep(0.5)
    print()

if wlan.isconnected():
    led.on()
    print("Wi-Fi 연결 성공!")
    print("IP 주소:", wlan.ifconfig()[0])
else:
    led.off()
    code = wlan.status()
    reasons = {
        -3: "비밀번호 오류",
        -2: "공유기를 찾을 수 없음 (SSID 오타 또는 5GHz 전용)",
        -1: "연결 실패 (공유기 상태 확인)",
        1: "아직 연결 중 (대기 시간 부족)",
        2: "IP 주소를 받지 못함 (공유기 DHCP 확인)",
    }
    print("Wi-Fi 연결 실패, 상태 코드:", code)
    print("원인:", reasons.get(code, "알 수 없음"))
