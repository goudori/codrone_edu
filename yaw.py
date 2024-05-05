"""
ヨーとは、機体ごと旋回する(＋であれば、左回転 -であれば、右回転　※127～-128度まで)

degree　→機体の角度(向き)を変える
"""
from codrone_edu.drone import *

# ドローンオブジェクト作成
drone = Drone()

# ペアリング
drone.pair()

# 　離陸
drone.takeoff()

# hover
drone.hover(1)

# 左回転
drone.set_yaw(80)

# 移動
drone.move(1)

# 右回転
drone.set_yaw(-80)

# 移動
drone.move(1)

# 右回転
drone.set_yaw(-80)

# 移動
drone.move(1)

# 左回転
drone.set_yaw(80)

# 移動
drone.move(1)

# 着陸
drone.land()

# 閉じる
drone.close()
