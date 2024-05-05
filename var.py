"""
変数を使った飛行方法の書き方→　drone.飛行方法(変数名)
duration　→ドローンの飛行時間   speed　→ドローンの速度
下記コードは、「ジグザグ飛行」
"""
from codrone_edu.drone import *

drone = Drone()

drone.pair()

"ドローンの速度"
speed = 20

"ドローンの速度0"
zero_speed = 0

"ドローンの飛行時間"
duration = 1.2

drone.takeoff()

drone.hover(3)

# 右
drone.set_roll(speed)

drone.move(duration)

drone.set_roll(zero_speed)

# 前
drone.set_pitch(speed)

drone.move(duration)

drone.set_pitch(zero_speed)

# 左
drone.set_roll(-speed)

drone.move(duration)

drone.set_roll(zero_speed)

# 前
drone.set_pitch(speed)

drone.move(duration)

drone.set_pitch(zero_speed)

# 後ろ
drone.set_pitch(-speed)

drone.move(duration)

drone.set_pitch(zero_speed)

# 右
drone.set_roll(speed)

drone.move(duration)

drone.set_roll(zero_speed)

# 後ろ
drone.set_pitch(-speed)

drone.move(duration)

drone.set_pitch(zero_speed)

# 左
drone.set_roll(-speed)

drone.move(duration)

drone.set_roll(zero_speed)

drone.land()

drone.close()
