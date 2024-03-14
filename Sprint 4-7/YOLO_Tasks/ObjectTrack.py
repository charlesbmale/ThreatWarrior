from ultralytics import YOLO
from ultralytics.models import yolo

model = YOLO("../../models/yolov8n.pt")
'''
yolo task=detect mode=predict source="path/to/video.mp4" classes=[16] show=True
'''

results = model.track(source=0, show=True, tracker="bytetrack.yaml", save=False, classes = 0)

#yolotask=detect mode=predict source="path/to/video.mp4" classes=[2, 5, 6, 7] show=True


