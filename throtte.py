"""
スロットルとは、上昇や下降する。(+は、上昇で、-は、下降です。※127～-128度まで)
"""
from codrone_edu.drone import *

# ドローンオブジェクト
drone = Drone()

# ペアリング
drone.pair()

# 離陸
drone.takeoff()

# hover
drone.hover(2)

# 上昇
drone.set_throttle(50)

# 移動
drone.move(1.5)

# 下降
drone.set_throttle(-90)

# 移動
drone.move(1.5)

# 着陸
drone.land()

# 閉じる
drone.close()