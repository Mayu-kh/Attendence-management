import cv2
import numpy as np
model_path = 'haarcascade_frontalface_dataset.xml'
faceCascade = cv2.CascadeClassifier(model_path)
# Capturing video frme by frame
video_capture = cv2.VideoCapture(0)  
ret, frame = video_capture.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
#Detecting Number of face in video 
list_face=np.array(faces)
print("number of face deteced is {}".format(len(list_face)))
    # Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
# Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
