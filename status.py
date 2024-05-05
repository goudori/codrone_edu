from codrone_edu.drone import *
import time

drone = Drone()

drone.pair()

time.sleep(5)
# 気圧
presuure = drone.get_pressure()

# 気温
temp = drone.get_temperature()

# 飛行ステータス
status = drone.get_flight_state()

# エラー確認
error = drone.get_error_data()
drone.sendCommand(CommandType.ClearBias)
print(str(presuure) + "Pa")
print(str(temp) + "度")
print(str(status) + "(飛行状態)")
print(str(error) + "というエラーを確認しました")
time.sleep(5)

drone.land()
drone.close()
