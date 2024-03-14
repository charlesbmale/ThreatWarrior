import cv2
from ultralytics import YOLO

model = YOLO("../../models/yolov8n-oiv7.pt")
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    results = model.predict(source=0, save=True, imgsz=640, conf=0.5)
    annotated_frame = results[0].plot()
    cv2.imshow("Img", annotated_frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()