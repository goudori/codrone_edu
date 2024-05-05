from codrone_edu.drone import *

drone = Drone()

drone.pair()

duration = 1.5

# 揺れの回数
sways = 0

argle = 40

drone.takeoff()

drone.hover(3)

while sways < 3:
    drone.set_roll(argle)

    drone.move(duration)

    drone.set_roll(0)

    drone.set_roll(-argle)

    drone.move(duration)

    drone.set_roll(0)

    sways += 1

    drone.land()

    drone.close()
