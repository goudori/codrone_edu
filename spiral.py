from codrone_edu.drone import *

drone = Drone()
drone.pair()
drone.takeoff()
# default spiral parameters (50, 5, 1)
drone.spiral(20, 4, -1)

drone.spiral(20, 4, 1)
drone.land()
drone.close()
