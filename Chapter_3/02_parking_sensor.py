# 02_parking_sensor.py — 실습2 주차 센서 (거리별 LED)
# 30cm 이상: 초록 / 15~30cm: 노랑 / 15cm 미만: 빨강
# LED는 2차시 회로 그대로: 빨강 GP13, 노랑 GP14, 초록 GP15
from machine import Pin, time_pulse_us
import time

trig = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)
red = Pin(13, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(15, Pin.OUT)

def get_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    t = time_pulse_us(echo, 1, 30000)
    if t < 0:
        return -1
    return t * 0.0343 / 2

def light(r, y, g):
    red.value(r)
    yellow.value(y)
    green.value(g)

while True:
    d = get_distance()
    if d < 0:
        light(0, 0, 0)          # 측정 실패 → 모두 끄기
    elif d < 15:
        light(1, 0, 0)          # 가까움 → 빨강
    elif d < 30:
        light(0, 1, 0)          # 조금 가까움 → 노랑
    else:
        light(0, 0, 1)          # 멀다 → 초록
    print(round(d, 1), "cm")
    time.sleep(0.2)

# [미션] 기준 거리(15, 30)를 바꿔 보세요.
