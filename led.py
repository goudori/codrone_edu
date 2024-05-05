"""
LEDライト決められた７色とそれ以外の色の設定

※色の設定は、できないのや変わらない時がある。(例)黒は、LED OFFになる。
"""
from codrone_edu.drone import *
import time

drone = Drone()

drone.pair()

# 茶色
drone.set_drone_LED(153, 51, 0, 100)
drone.set_controller_LED(153, 51, 0, 100)

time.sleep(2)

# 赤色
drone.set_drone_LED(255, 0, 0, 100)
drone.set_controller_LED(255, 0, 0, 100)

time.sleep(2)

# 緑色
drone.set_drone_LED(0, 255, 0, 100)
drone.set_controller_LED(0, 255, 0, 100)

time.sleep(2)

# 青色
drone.set_drone_LED(0, 0, 255, 100)
drone.set_controller_LED(0, 0, 255, 100)

time.sleep(2)

# 黄色
drone.set_drone_LED(255, 255, 0, 100)
drone.set_controller_LED(255, 255, 0, 100)

time.sleep(2)

# 紫色
drone.set_drone_LED(128, 0, 128, 100)
drone.set_controller_LED(128, 0, 128, 100)

time.sleep(2)

# 白色
drone.set_drone_LED(255, 255, 255, 100)
drone.set_controller_LED(255, 255, 255, 100)

time.sleep(2)

# ライトブルー
drone.set_drone_LED(0, 204, 255, 100)
drone.set_controller_LED(0, 204, 255, 100)

time.sleep(2)

# LEDをオフ
drone.drone_LED_off()
drone.controller_LED_off()

time.sleep(2)

# 色の濃さを変化させる 0~255回まで繰り返す
for i in range(256):
    drone.set_drone_LED(0, i, 0, 100)
    drone.set_controller_LED(0, i, 0, 100)
    time.sleep(0.05)

for i in range(256):
    drone.set_drone_LED(0, 0, i, 100)
    drone.set_controller_LED(0, 0, i, 100)
    time.sleep(0.05)

    if i >= 255:
        drone.drone_LED_off()
        drone.controller_LED_off()
        print("終了")

drone.close()
