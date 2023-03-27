import uuid
import os
import cv2


# open webcam for collect images
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # cut frame in required size
    frame = frame[120:120+250, 200:200+250, :]
    
    # for collecting anchor images press "a"
    if cv2.waitKey(1) & 0xFF == ord('a'):
        # create the path
        imgname = os.path.join('/home/sangramdh/jupyter/Siamese_Architecture/data/anchor', '{}.jpg'. format(uuid.uuid3()))
        # write anchor images
        cv2.imwrite(imgname, frame)
        
    # for collecting anchor images press "p"
    if cv2.waitKey(1) & 0XFF == ord('p'):
        imgname = os.path.join('/home/sangramdh/jupyter/Siamese_Architecture/data/positive', '{}.jpg'. format(uuid.uuid3()))
        # write positive images
        cv2.imwrite(imgname, frame)
        
    # show image
    cv2.imshow('Image Collection', frame)
    
    # come out of camera
    if cv2.waitKey(0) & 0XFF == ord('q'):
        break
        
        
cap.release()
cv2.destroyAllWindows()