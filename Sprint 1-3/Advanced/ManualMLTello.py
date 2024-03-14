# Manual Tello drone (keyboard control) and YOLOv8 Integration (ML Object Detection Algorithm)
# Edited by Dr. Park and Cadets: Bonilla, Major, & Malé, Dec-2023
# References: https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf

# Importation of Python Libraries
import cv2
import pygame
from time import sleep
from ultralytics import YOLO
from djitellopy import Tello

# Loading of ML Algorithm
model = YOLO("../../models/yolov8n-pose.pt")

# Initialization of Video Capture
cap = cv2.VideoCapture(0)

# Initialization of pygame object
# Must be in active mode to get keyboard input
def initPygame():
    pygame.init()
    window = pygame.display.set_mode((300, 200))

# Check keyboard input and returns if the pressed_key is a control key
# Returns 'true' only if the pressed key matches with keyName
"""
 'LEFT'    : move left     'RIGHT'   : move right
 'UP'      : move back     'DOWN'    : move forward
 'W'       : move up       'S'       : move down
 'A'       : yaw left      'D'       : yaw right
"""

# Establishment of key acquisition method
def getKey(keyName):
    for event in pygame.event.get():
        pass
    keyPressed = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))

    pygame.display.update()
    return keyPressed[myKey]

# Establishment of key values
def getControlValue():

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if getKey("LEFT"):
        lr = -speed
    elif getKey("RIGHT"):
        lr = speed

    if getKey("UP"):
        fb = speed
    elif getKey("DOWN"):
        fb = -speed

    if getKey("w"):
        ud = speed
    elif getKey("s"):
        ud = -speed

    if getKey("a"):
        yv = -speed
    elif getKey("d"):
        yv = speed
        # Might have to switch "speed" values

    return [lr, fb, ud, yv]

# Dr
if __name__ == '__main__':

    initPygame()

    drone = Tello()
    drone.connect()
    print(drone.get_battery())

    drone.streamon()
    drone.takeoff()

    while True:

        frame = drone.get_frame_read().frame
        results = model.predict(frame, save=True, imgsz=640, conf=0.6)
        annotated_frame = results[0].plot()
        cv2.imshow("Img", annotated_frame)

        #cv2.resize(frame, (300, 200))
        #qcv2.imshow('DRONE', frame)

        vals = getControlValue()
        print(vals[0], "-", vals[1], "-", vals[2], "-", vals[3])

        drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        sleep(0.05)

        """ if 'q' pressed, break while loop """
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    drone.land()
    drone.streamoff()
    cv2.destroyAllWindows()
    # exit()