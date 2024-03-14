import cv2
from ultralytics import YOLO

model = YOLO('../../yolov8n.pt')
cap = cv2.VideoCapture(0)

results = model(source=1, show=True, con=0.4, save=True)