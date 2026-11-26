# 03_intruder_alarm.py — 실습3 침입 경보기
# 움직임 감지 → 빨강 LED + 사이렌 / 평소 → 초록 LED
from machine import Pin, PWM
import time

pir = Pin(19, Pin.IN)
buzzer = PWM(Pin(20))
red = Pin(13, Pin.OUT)
green = Pin(15, Pin.OUT)

def siren():
    for i in range(5):              # 삐-뽀 5번 (약 2초)
        buzzer.freq(880)
        buzzer.duty_u16(32768)
        red.value(1)
        time.sleep(0.2)
        buzzer.freq(660)
        red.value(0)
        time.sleep(0.2)
    buzzer.duty_u16(0)              # 소리 끄기

print("센서 준비 중... 30초 기다리기")
time.sleep(30)
print("감시 시작!")

while True:
    if pir.value() == 1:
        green.value(0)
        print("침입 감지!")
        siren()
    else:
        green.value(1)
    time.sleep(0.1)
