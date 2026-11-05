# 02_repeat.py — 정해진 횟수만큼 점멸 후 종료
from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

for i in range(5):           # 0, 1, 2, 3, 4 → 5번 반복
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
    print(i + 1, "번째 점멸")

print("5번 점멸 완료")

# [도전] range(5)를 range(10)으로 바꿔 보세요.
# [질문] while True와 for는 각각 언제 사용할까요?
