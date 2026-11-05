# bonus_temperature.py — [보너스] 내장 온도센서 읽기
# 9차시 '센서 데이터 수집'의 예고 활동입니다.
from machine import ADC
from time import sleep

sensor = ADC(4)                  # 내장 온도센서 채널
FACTOR = 3.3 / 65535             # 읽은 값 → 전압 변환

while True:
    voltage = sensor.read_u16() * FACTOR
    temp = 27 - (voltage - 0.706) / 0.001721
    print("칩 온도:", round(temp, 1), "°C")
    sleep(1)

# ※ 칩 자체의 온도라 실제 실내 온도보다 조금 높게 나올 수 있습니다.
