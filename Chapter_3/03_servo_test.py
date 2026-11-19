# 03_servo_test.py — 실습3 서보모터 각도 제어
# 배선: 갈색(GND) → GND 레일, 빨강(+) → 5V 레일(VBUS), 주황(신호) → GP18(24번 핀)
from machine import Pin, PWM
import time

servo = PWM(Pin(18))
servo.freq(50)                  # 50Hz (20ms)

def set_angle(angle):
    pulse = 500 + angle * 2000 / 180    # µs
    servo.duty_u16(int(pulse * 65535 / 20000))

for angle in [0, 45, 90, 135, 180, 90, 0]:
    print("각도:", angle)
    set_angle(angle)
    time.sleep(1)

# [관찰] 0도와 180도에서 서보가 '지잉' 소리를 내면, 범위 끝에 닿은 것입니다.
#        자동문에서는 0도(닫힘)와 90도(열림)만 사용합니다.
