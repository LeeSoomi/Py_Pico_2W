# 04_pedestrian_light.py — 실습4 보행자 요청 신호등
# 차량 신호: 빨강 GP13, 노랑 GP14, 초록 GP15
# 보행 신호: 내장 LED (켜짐 = 건너세요, 깜빡임 = 곧 바뀜)
# 보행 버튼: GP12 (외부 10kΩ 풀다운, 누르면 1)
from machine import Pin
from time import sleep

red = Pin(13, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(15, Pin.OUT)
walk = Pin("LED", Pin.OUT)
button = Pin(12, Pin.IN)

def light(r, y, g):
    red.value(r)
    yellow.value(y)
    green.value(g)

def walk_signal():
    walk.on()                    # 보행 신호 켜기
    sleep(3)
    for i in range(3):           # 곧 바뀜 → 3번 깜빡임
        walk.off()
        sleep(0.5)
        walk.on()
        sleep(0.5)
    walk.off()

light(0, 0, 1)  # 처음에는 차량 초록
walk.off()

while True:
    if button.value() == 1:
        sleep(0.05)                      # 50ms 후 재확인
        if button.value() == 1:
            print("보행자 요청!")
            light(0, 1, 0)               # 노랑
            sleep(2)
            light(1, 0, 0)               # 빨강
            sleep(1)                     # 안전 여유 시간
            walk_signal()                # 보행 신호
            sleep(1)
            light(0, 0, 1)               # 다시 초록
            while button.value() == 1:   # 버튼을 놓을 때까지 대기
                sleep(0.05)
    sleep(0.05)
