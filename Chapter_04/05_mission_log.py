# 05_mission_log.py — 심화 미션 정답 예시
# 감지 기록을 Pico 안의 log.txt 파일에 저장하기
# → 전원을 껐다 켜도 기록이 남습니다. (Thonny 보기 > 파일 에서 확인)
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
    t = time.localtime()
    h = str(t[3])
    m = str(t[4])
    s = str(t[5])
    return h + ":" + m + ":" + s

def save_log(number):
    f = open("log.txt", "a")        # 이어 쓰기
    f.write(str(number) + "," + now_text() + "\n")
    f.close()                       # 저장 완료

def show_log():
    try:
        f = open("log.txt", "r")    # "r" = 읽기
        print("--- 지금까지의 기록 ---")
        print(f.read())
        f.close()
    except OSError:
        print("아직 기록이 없습니다.")

show_log()
count = 0
last = 0

print("센서 준비 중... 30초 기다리기")
time.sleep(30)
print("감시 시작!")
green.value(1)

while True:
    now = pir.value()
    if last == 0 and now == 1:
        count = count + 1
        save_log(count)
        print(count, "번째 감지 — 기록 저장 완료")
        green.value(0)
        siren()
        green.value(1)
    last = now
    time.sleep(0.1)
