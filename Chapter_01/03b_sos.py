# 03b_sos.py — [심화] 모스부호 SOS ( ··· — — — ··· )
# 짧은 신호(점)와 긴 신호(선)는 "켜진 시간"만 다르고
# 신호 사이 간격(꺼진 시간)은 똑같이 짧게 유지합니다.
from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

UNIT = 0.2                   # 기본 시간 단위(초)

def blink(count, on_time, off_time):
    for i in range(count):
        led.on()
        sleep(on_time)
        led.off()
        sleep(off_time)

def sos():
    blink(3, UNIT, UNIT)         # S : 점 3개
    sleep(UNIT * 2)              # 글자 사이 간격
    blink(3, UNIT * 3, UNIT)     # O : 선 3개 (점의 3배 길이)
    sleep(UNIT * 2)
    blink(3, UNIT, UNIT)         # S : 점 3개

for n in range(3):           # SOS 3번 반복
    sos()
    sleep(UNIT * 7)              # 단어 사이 간격
    print("SOS", n + 1, "회 전송")
