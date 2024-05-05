# Co Drone EDU
from codrone_edu.drone import *
import time

# ドローンオブジェクト
drone = Drone()

# ペアリング
drone.pair()

# トリム値確認
print(drone.get_trim())

# トリムを左に調整
drone.set_trim(-5, 0)

time.sleep(1)

# 離陸
drone.takeoff()

# hover
drone.hover(3)

# ピッチをスピード力30で、ロール(+であれば、前傾  -であえば、後傾)
drone.set_pitch(30)

# ドローンを動かす
drone.move(1)

# 着陸
drone.land()

# 接続を閉じる
drone.close()
