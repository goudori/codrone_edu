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

# ロール角度３０度で、ロール設定(+であれば、右移動  -であえば、左移動)
drone.set_roll(+30)

# ドローンを動かす
drone.move(1.5)

# 着陸
drone.land()

# 接続を閉じる
drone.close()
