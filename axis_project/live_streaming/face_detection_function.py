def face_count():
    import cv2
    import sys
    import numpy as np
    model_path = 'haarcascade_frontalface_dataset.xml'  # dataset
    faceCascade = cv2.CascadeClassifier(model_path)
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
           
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count_face_list=np.array(faces) 
        #print(len(count_face_list))
        fc=len(count_face_list)
        print(fc)
        if fc==1:
            print(fc)
            #video_capture.release()
            #cv2.destroyAllWindows()
            break
            
        #print(fc)
    video_capture.release()
    cv2.destroyAllWindows()
    return fc
    
    
face_count()
