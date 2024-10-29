from codrone_edu.drone import *

drone = Drone()
# 接続
drone.pair()
# 離陸
drone.takeoff()

"""

バッテリーが、50％以下もしくは、連続フリップは、フリップできない。
"""

drone.hover(3)
# 前方フリップする
drone.flip("front")


# 着陸
drone.land()

# 終了
drone.close()
