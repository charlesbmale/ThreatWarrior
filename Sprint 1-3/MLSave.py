# Python program to save a video using OpenCV
# Edited by Cadet Malé, Dec-2023
# References: https://www.geeksforgeeks.org/saving-a-video-using-opencv/

import cv2
from ultralytics import YOLO

# Create an object to read from camera
# Loading of model
model = YOLO("../models/yolov8n-pose.pt")
video = cv2.VideoCapture(0)

# We need to check if camera
# is opened previously or not
if (video.isOpened() == False):
    print("Error reading video file")

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

# Below VideoWriter object will create a frame of above defined The output is stored in 'filename.avi' file.
result = cv2.VideoWriter('../filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

while (True):
    ret, frame = video.read()

    results = model.predict(frame, save=True, imgsz=640, conf=0.6)
    annotated_frame = results[0].plot()
    # cv2.imshow("Img", annotated_frame)

    if ret == True:

        # Write the frame into the
        # file 'filename.avi'
        result.write(annotated_frame)

        # Display the frame
        # saved in the file
        # cv2.imshow('Frame', frame)
        cv2.imshow("Img", annotated_frame)

        # Press S on keyboard
        # to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    # Break the loop
    else:
        break

# -------------------------------------------------------------------
# while(True):
    # ret, frame = video.read()

    # results = model.predict(frame, save=True, imgsz=640, conf=0.6)
    # annotated_frame = results[0].plot()
    # cv2.imshow("Img", annotated_frame)

    # if cv2.waitKey(1) == ord('q'):
        # break

# -------------------------------------------------------------------


# When everything done, release
# the video capture and video
# write objects
video.release()
result.release()

# Closes all the frames
cv2.destroyAllWindows()

print("The video was successfully saved")