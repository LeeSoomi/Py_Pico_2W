# bonus_interrupt.py — [보너스] 인터럽트 (쉬운 버전)
# 지금까지(폴링): 프로그램이 "눌렸나?"를 계속 직접 확인 → sleep 중에는 확인 못 함
# 인터럽트: 버튼이 눌리는 순간 보드가 알아서 함수를 실행 → sleep 중에도 기억!
#           비유: 현관문을 계속 열어 보기(폴링) vs 초인종(인터럽트)
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

request = False     # 요청 깃발

# 버튼이 눌리는 순간 "자동으로" 실행되는 함수
def pressed(pin):
    global request          # 함수 밖의 request를 바꾸겠다는 표시
    request = True

# 초인종 달기: 0 → 1이 되는 순간(누르는 순간) pressed 함수 실행
button.irq(trigger=Pin.IRQ_RISING, handler=pressed)

while True:
    light(0, 0, 1)              # 초록
    time.sleep(5)               # 이 5초 동안 눌러도 기억됨!

    while request == False:     # 요청이 올 때까지 초록 유지
        time.sleep(0.1)

    while button.value() == 1:  # 버튼을 놓을 때까지 기다린 뒤
        time.sleep(0.1)
    request = False             # 깃발 내리기

    light(0, 1, 0)              # 노랑
    time.sleep(2)
    light(1, 0, 0)              # 빨강
    time.sleep(1)
    walk.on()                   # 보행 신호
    time.sleep(4)               # 이때 눌러도 다음 차례 요청으로 기억됨!
    walk.off()
    time.sleep(1)
