# 03_led_pattern.py — 함수로 LED 패턴 만들기
from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

def blink(count, speed):
    """count번, speed초 간격으로 점멸"""
    for i in range(count):
        led.on()
        sleep(speed)
        led.off()
        sleep(speed)

blink(3, 0.2)     # 빠르게 3번
sleep(1)          # 1초 쉬기
blink(2, 1)       # 느리게 2번

print("패턴 실행 완료")
