"""
PEMDAS　→計算の順番の頭文字の事。

range　→整数の開始から終了までの範囲指定する関数の事。

for　→決められた繰り返し

while　→わからない繰り返し

for　変数名　in  range(変数開始の値,変数終了の値(stop),変数開始の値の増加もしくは、減る値):
"""
from codrone_edu.drone import *

drone = Drone()

drone.pair()

speed = 15

angel_right = 127

duration = 1.5

drone.takeoff()

for i in range(0, 4, 1):
    # 前
    drone.set_pitch(speed)
    drone.move(duration)
    drone.set_pitch(0)

# 右
    drone.set_yaw(-angel_right)
    drone.move(duration)
    drone.set_yaw(0)

    drone.land()
    drone.close()
