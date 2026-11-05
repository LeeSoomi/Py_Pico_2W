# 04_wifi_scan.py — 주변 Wi-Fi 검색
# Pico 2W는 2.4GHz만 지원하므로 5GHz 공유기는 목록에 나타나지 않습니다.
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("주변 Wi-Fi 검색 중...")
networks = wlan.scan()

# 신호가 강한 순서로 정렬 (RSSI: 0에 가까울수록 강함)
networks.sort(key=lambda n: n[3], reverse=True)

for net in networks:
    ssid = net[0].decode()
    channel = net[2]
    rssi = net[3]
    if ssid == "":
        ssid = "(숨김 네트워크)"
    print(ssid, "| 채널:", channel, "| 신호세기:", rssi, "dBm")

print("검색된 개수:", len(networks))
