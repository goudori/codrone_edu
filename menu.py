"""
メニューコマンド操作
"""
from codrone_edu.drone import *

drone = Drone()

drone.pair()

drone.takeoff()

duration = 1.2

while True:
    print("1. pitch \n"
          "2. triangle \n"
          "3. flip \n"
          "4. Sway \n"
          "5. Quit \n"
          )

    option = input("Select an option: ")

    if option == "1":
        drone.set_yaw(30)
        drone.move(duration)

    elif option == "2":
        drone.set_roll(30)
        drone.move(duration)

    elif option == "3":
        drone.flip("back")

    elif option == "4":
        drone.sway(duration)

    elif option == "5":
        print("Quit the menu.")
        break

    else:
        print("Please Try again.")

    drone.land()

print("Done")
drone.close()
