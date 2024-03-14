import cv2
from ultralytics import YOLO
from djitellopy import Tello
from time import sleep

model = YOLO("../../models/yolov8n-pose.pt")
cap = cv2.VideoCapture(0)

# Connect to drone first
drone = Tello()
drone.connect()
drone.streamon()
drone.move_up(30)

# Get Frame and annotate
while(True):
    # ret, frame = cap.read()
    frame = drone.get_frame_read().frame

    results = model.predict(frame, save=True, imgsz=640, conf=0.6)
    annotated_frame = results[0].plot()
    cv2.imshow("Img", annotated_frame)

    if cv2.waitKey(1) == ord('q'):
        break

drone.streamoff()
drone.land()
cap.release()
cv2.destroyAllWindows()
