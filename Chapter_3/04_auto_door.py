# 04_auto_door.py — 실습4 스마트 자동문
# 15cm 안에 사람이 오면 문 열기(90도, 초록)
# 3초 동안 아무도 없으면 문 닫기(0도, 빨강)
from machine import Pin, PWM, time_pulse_us
import time

trig = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)
servo = PWM(Pin(18))
servo.freq(50)
red = Pin(13, Pin.OUT)
green = Pin(15, Pin.OUT)

OPEN_DIST = 15          # 문이 열리는 거리(cm)

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

door_open = False       # False = 닫힘
count = 0               # 10 = 1초
set_angle(0)
red.value(1)
green.value(0)

while True:
    d = get_distance()

    if 0 < d < OPEN_DIST:        # 사람이 가까이
        count = 0
        if door_open == False:   # 닫혀 있으면 열기
            set_angle(90)
            red.value(0)
            green.value(1)
            door_open = True
            print("문 열림", round(d, 1), "cm")
    else:                        # 아무도 없으면
        count = count + 1        # 0.1초마다 +1
        if door_open == True and count >= 30:  # 3초
            set_angle(0)
            red.value(1)
            green.value(0)
            door_open = False
            print("문 닫힘")

    time.sleep(0.1)
