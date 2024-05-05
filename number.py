from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

print("Command Options: ")
print("w: throttle up \n"
      "s: throttle down \n"
      "a: yaw left \n"
      "d: yaw right \n"
      "i: pitch forward \n"
      "k: pitch backward \n"
      "j: roll left \n"
      "l: roll right \n"
      "q: quit")

drone.takeoff()
power = 10

while True:
    drone.set_throttle(0)
    drone.set_roll(0)
    drone.set_yaw(0)
    drone.set_pitch(0)

    direction = input("Input a command: ")

    if direction == "w":
        drone.set_throttle(power)

    elif direction == "s":
        drone.set_throttle(-power)

    elif direction == "a":
        drone.set_yaw(-power)

    elif direction == "d":
        drone.set_yaw(power)

    elif direction == "i":
        drone.set_pitch(power)

    elif direction == "k":
        drone.set_pitch(-power)

    elif direction == "j":
        drone.set_roll(-power)

    elif direction == "l":
        drone.set_roll(power)

    elif direction == "q":
        drone.land()
        drone.close()
        break
    else:
        print("Not a command")

    drone.move(1)
print("Done")
