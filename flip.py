from codrone_edu.drone import *

drone = Drone()
# 接続
drone.pair()
# 離陸
drone.takeoff()

"""

バッテリーが、連続フリップや50％以下になれば、フリップできない。
"""

drone.hover(3)
# 前方フリップする
drone.flip("forward")


# 着陸
drone.land()

# 終了
drone.close()
