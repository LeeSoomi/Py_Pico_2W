# 02_traffic_auto.py — 실습2 자동 신호등
# 순서: 빨강 3초 → 초록 3초 → 노랑 1초 → 반복
from machine import Pin
from time import sleep

red = Pin(13, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(15, Pin.OUT)

def light(r, y, g):
    red.value(r)
    yellow.value(y)
    green.value(g)

while True:
    light(1, 0, 0)  # 빨강
    sleep(3)
    light(0, 0, 1)  # 초록
    sleep(3)
    light(0, 1, 0)  # 노랑
    sleep(1)

# [학생 활동] 빨강 5초, 초록 4초, 노랑 2초로 바꿔 보세요.
