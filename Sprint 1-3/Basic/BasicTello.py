from djitellopy import Tello
from time import sleep

drone = Tello()
drone.connect()
print(drone.get_battery())
print(drone.get_barometer())

drone.takeoff()

drone.move_up(30)
sleep(3)

drone.land()