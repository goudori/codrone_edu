from codrone_edu.drone import *

drone = Drone()

drone.pair()

"""
light_color　→選択した色

※コントローラー「R1ボタン」を押せば、ドローンとコントローラーの色が変わる
"""
light_color = "blue"

duration = 1

drone.takeoff()

if light_color == "red":
    drone.set_pitch(35)
    drone.move(duration)

elif light_color == "yellow":
    drone.set_roll(30)
    drone.move(duration)

elif light_color == "green":
    drone.hover(3)

else:
    print("色が見つかりません")

# ドローンの飛行状態
print(drone.get_flight_state())

drone.land()

drone.close()
