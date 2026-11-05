# 01_blink.py — 내장 LED 1초 간격 무한 점멸
# 정지: Thonny의 Stop 버튼 또는 Ctrl+C
from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)    # Pico 2W 내장 LED (GPIO 25 아님!)

while True:                  # 아두이노의 loop()와 같은 역할
    led.on()
    print("LED ON")
    sleep(1)                 # 1초 대기 = 아두이노 delay(1000)
    led.off()
    print("LED OFF")
    sleep(1)

# [도전] sleep(1)을 sleep(0.2)로 바꿔 속도를 비교해 보세요.
# [도전] led.on()/led.off() 대신 led.toggle()로 줄여 보세요.
