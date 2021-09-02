#this file captures the background image and saves it on the local system
#the image captured by this program will used in the file "invisible_cloak.py"

import cv2

cap = cv2.VideoCapture(0)     #starting camera

while cap.isOpened():
    ret,background =  cap.read()
    if ret:
        cv2.imshow("Capturing Background Image",background)
        if cv2.waitKey(1) == ord('q'):                                #when user presses 'q' the captured image will be saved
            cv2.imwrite("image.jpg",background)
            break

cap.release()
cv2.destroyAllWindows()

