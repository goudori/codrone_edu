"""
正弦波飛行
"""
from codrone_edu.drone import *

drone = Drone()

drone.pair()

drone.takeoff()

drone.hover(1)

# 上昇
drone.set_throttle(35)

# 移動
drone.move(0.5)

# 前進
drone.set_pitch(35)

# 移動
drone.move(0.5)

# 停止
drone.set_pitch(0)

# 下降
drone.set_throttle(-35)

drone.move(0.5)

# 前進
drone.set_pitch(35)

# 移動
drone.move(0.5)

# 停止
drone.set_pitch(0)

# 上昇
drone.set_throttle(35)

# 移動
drone.move(0.5)

# 前進
drone.set_pitch(35)

# 移動
drone.move(0.5)

# 停止
drone.set_pitch(0)

# 下降
drone.set_throttle(-35)

drone.move(0.5)

# 前進
drone.set_pitch(35)

# 移動
drone.move(0.5)

drone.land()

# ドローンとの接続を切る
drone.close()
