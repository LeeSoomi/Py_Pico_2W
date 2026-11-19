# 05_mission_door.py — 심화 미션 정답 예시
# ① 문이 천천히 열리고 닫히기 (5도씩 움직이기)
# ② 문이 열린 횟수 세기 (4차시 '감지 횟수 기록' 예고)
from machine import Pin, PWM, time_pulse_us
import time

trig = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)
servo = PWM(Pin(18))
servo.freq(50)
red = Pin(13, Pin.OUT)
green = Pin(15, Pin.OUT)

OPEN_DIST = 15

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

def set_angle(angle):
    pulse = 500 + angle * 2000 / 180
    servo.duty_u16(int(pulse * 65535 / 20000))

def open_door():
    for angle in range(0, 91, 5):     # 5도씩
        set_angle(angle)
        time.sleep(0.03)

def close_door():
    for angle in range(90, -1, -5):   # 5도씩
        set_angle(angle)
        time.sleep(0.03)

door_open = False
count = 0
open_count = 0          # 문이 열린 횟수
set_angle(0)
red.value(1)
green.value(0)

while True:
    d = get_distance()

    if 0 < d < OPEN_DIST:
        count = 0
        if door_open == False:
            open_door()
            red.value(0)
            green.value(1)
            door_open = True
            open_count = open_count + 1
            print("문 열림 — 오늘", open_count, "번째 방문")
    else:
        count = count + 1
        if door_open == True and count >= 30:
            close_door()
            red.value(1)
            green.value(0)
            door_open = False
            print("문 닫힘")

    time.sleep(0.1)
