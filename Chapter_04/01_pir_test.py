# 01_pir_test.py — 실습1 PIR 센서로 움직임 감지
# 배선: PIR VCC → + 레일(5V), GND → − 레일, OUT → GP19(25번 핀)
# ※ 전원을 켠 뒤 30~60초는 센서가 준비하는 시간이라 값이 들쑥날쑥합니다.
from machine import Pin
import time

pir = Pin(19, Pin.IN)
red = Pin(13, Pin.OUT)
green = Pin(15, Pin.OUT)

print("센서 준비 중... 30초 기다리기")
time.sleep(30)
print("감시 시작!")

while True:
    if pir.value() == 1:        # 움직임 감지
        red.value(1)
        green.value(0)
        print("움직임 감지!")
    else:                       # 조용함
        red.value(0)
        green.value(1)
    time.sleep(0.2)
