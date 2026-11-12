# 05_mission_request.py — 심화 미션 정답 (쉬운 버전)
# 실습 4와 다른 점: 버튼을 누르면 바로 바뀌지 않고 "요청"만 기억해 둔다.
#   ① 요청 저장      → request 변수 (깃발)
#   ② 초록 최소 5초  → count 변수 (0.1초마다 1씩 세기)
#   ③ 1회만 처리     → 깃발은 여러 번 올려도 한 번 올린 것과 같다
from machine import Pin
import time

red = Pin(13, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(15, Pin.OUT)
walk = Pin("LED", Pin.OUT)
button = Pin(12, Pin.IN)        # 외부 10kΩ 풀다운 (누르면 1)

def light(r, y, g):
    red.value(r)
    yellow.value(y)
    green.value(g)

def walk_signal():
    walk.on()
    time.sleep(3)
    for i in range(3):
        walk.off()
        time.sleep(0.5)
        walk.on()
        time.sleep(0.5)
    walk.off()

request = False     # 요청 깃발 (False = 요청 없음)
count = 0           # 초록이 켜진 뒤 센 숫자 (10 = 1초)
light(0, 0, 1)

while True:
    # 1) 버튼을 누르면 깃발을 올린다
    if button.value() == 1:
        request = True

    # 2) 깃발이 올라가 있고, 초록이 5초(50번) 이상 켜졌으면 신호를 바꾼다
    if request == True and count >= 50:
        light(0, 1, 0)      # 노랑
        time.sleep(2)
        light(1, 0, 0)      # 빨강
        time.sleep(1)
        walk_signal()       # 보행 신호
        time.sleep(1)
        light(0, 0, 1)      # 다시 초록
        request = False     # 깃발 내리기
        count = 0           # 처음부터 다시 세기

    # 3) 0.1초 쉬고 1 더하기
    time.sleep(0.1)
    count = count + 1
