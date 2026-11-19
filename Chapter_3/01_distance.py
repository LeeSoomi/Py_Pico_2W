# 01_distance.py — 실습1 초음파 센서로 거리 측정
# 배선: VCC → 5V 레일(VBUS 40번), GND → GND 레일
#       TRIG → GP16(21번 핀)
#       ECHO → 1kΩ → GP17(22번 핀), GP17 → 2kΩ → GND  (5V 신호를 3.3V로 낮추기)
from machine import Pin, time_pulse_us
import time

trig = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)

def get_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)                 # 10µs 신호
    time.sleep_us(10)
    trig.value(0)
    t = time_pulse_us(echo, 1, 30000)   # 왕복 시간(µs)
    if t < 0:
        return -1                 # 측정 실패
    return t * 0.0343 / 2         # 거리(cm)

while True:
    d = get_distance()
    if d < 0:
        print("측정 실패")
    else:
        print("거리:", round(d, 1), "cm")
    time.sleep(0.5)
