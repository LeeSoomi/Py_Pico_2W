# 03_button_test.py — 실습3 버튼 상태 확인 (외부 풀다운)
# 배선: 스위치 한쪽 다리 → 3V3(36번 핀, + 레일)
#       대각선 반대쪽 다리 → GP12(16번 핀) + 10kΩ 저항 → GND
# 풀다운 → 놓으면 0, 누르면 1
from machine import Pin
from time import sleep

button = Pin(12, Pin.IN)     # 외부 10kΩ 풀다운

while True:
    if button.value() == 1:
        print("버튼 눌림")
    else:
        print("버튼 놓임")
    sleep(0.2)

# [질문] 버튼을 눌렀는데 결과가 바뀌지 않으면 어떤 회로를 점검해야 할까?
