# 04_security_system.py — 실습4 보안 시스템 (감지 횟수 기록)
# 감지가 '시작된 순간'만 세어서 횟수와 시각을 기록합니다.
# (2차시 버튼 '눌린 순간 세기'와 같은 방법: last와 now 비교)
from machine import Pin, PWM
import time

pir = Pin(19, Pin.IN)
buzzer = PWM(Pin(20))
red = Pin(13, Pin.OUT)
green = Pin(15, Pin.OUT)

def siren():
    for i in range(5):
        buzzer.freq(880)
        buzzer.duty_u16(32768)
        red.value(1)
        time.sleep(0.2)
        buzzer.freq(660)
        red.value(0)
        time.sleep(0.2)
    buzzer.duty_u16(0)

def now_text():
    t = time.localtime()            # 지금 시각
    h = str(t[3])                   # 시
    m = str(t[4])                   # 분
    s = str(t[5])                   # 초
    return h + "시 " + m + "분 " + s + "초"

count = 0           # 감지 횟수
last = 0            # 직전 센서 값

print("센서 준비 중... 30초 기다리기")
time.sleep(30)
print("감시 시작!", now_text())
green.value(1)

while True:
    now = pir.value()

    if last == 0 and now == 1:      # 감지가 시작된 순간
        count = count + 1
        print(count, "번째 감지 —", now_text())
        green.value(0)
        siren()
        green.value(1)

    last = now
    time.sleep(0.1)
