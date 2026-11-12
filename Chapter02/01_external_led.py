# 01_external_led.py — 실습1 외부 LED 켜고 끄기
# 배선: 빨강 GP13(핀17), 노랑 GP14(핀19), 초록 GP15(핀20), GND(핀18)
from machine import Pin
from time import sleep

red = Pin(13, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(15, Pin.OUT)

red.on()
sleep(1)
red.off()

yellow.on()
sleep(1)
yellow.off()

green.on()
sleep(1)
green.off()

print("확인 완료 — 세 LED가 순서대로 켜졌나요?")
# 안 켜지는 LED가 있다면: 다리 방향(긴 다리 +) → 저항 위치 → GP 번호 순서로 확인
