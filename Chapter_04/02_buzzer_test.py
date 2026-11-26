# 02_buzzer_test.py — 실습2 부저로 소리 내기 (수동 부저)
# 배선: 부저 + → GP20(26번 핀), 부저 − → GND
# PWM의 주파수(freq) = 음의 높이
from machine import Pin, PWM
import time

buzzer = PWM(Pin(20))

def play(hz, sec):
    buzzer.freq(hz)             # 음 높이
    buzzer.duty_u16(32768)      # 소리 켜기 (50%)
    time.sleep(sec)
    buzzer.duty_u16(0)          # 소리 끄기
    time.sleep(0.05)

# 도   레   미   파   솔   라   시   도
notes = [262, 294, 330, 349, 392, 440, 494, 523]
for hz in notes:
    print(hz, "Hz")
    play(hz, 0.3)

# [미션] notes를 바꿔 '학교종'을 연주해 보세요.
#        솔솔라라 솔솔미 = [392, 392, 440, 440, 392, 392, 330]
