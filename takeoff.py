# これは「Co Drone EDU」のサンプルファイルです。
# Co Drone EDU
from codrone_edu.drone import *
import time

# ドローンオブジェクトを作成
drone = Drone()

# ペアリング
drone.pair()

# トリム値の確認
print(drone.get_trim())

"""
ドローンが、右にドリフトを防ぐため、左にトリム調整
(drone.set_trimの時は、必ずtime.sleepとtake offを必ず設定する。)
"""
drone.set_trim(-5, 0)

time.sleep(1)

# 離陸
drone.takeoff()

# hoverする
drone.hover(3)

# 着陸
drone.land()

# 接続を閉じる
drone.close()

