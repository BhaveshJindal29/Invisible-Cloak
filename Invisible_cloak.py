import cv2
import numpy as np

cap = cv2.VideoCapture(0)                                    #open camera
background = cv2.imread('./image.jpg')                       #get the background image

while cap.isOpened():
    ret,current_frame = cap.read()                           #read frames
    if ret:
        hsv_frame = cv2.cvtColor(current_frame,cv2.COLOR_BGR2HSV)      #converting RGB into HSV


        #defining the HSV range
        #note : this project creates the mask for red color if you want to do it for some other color then change these HSV values values
        l_red = np.array([0,120,70])
        u_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv_frame,l_red,u_red)

        l_red = np.array([170,120,70])
        u_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv_frame,l_red,u_red)

        red_mask = mask1+mask2      #any shade of "red" color form 0 to 10 and 170 to 180 will be stored in the variable "red_mask"

        #use "MORPH_OPEN" to clear out the noises
        red_mask  = cv2.morphologyEx(red_mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=10)
        #use "MORPH_DILATE" to increase smoothness of the image
        red_mask  = cv2.morphologyEx(red_mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=10)

        red_free = cv2.bitwise_not(red_mask)  #everything expect the cloak

        result_1 = cv2.bitwise_and(background,background,mask=red_mask)               #segmentation of color
        result_2 = cv2.bitwise_and(current_frame,current_frame,mask=red_free)         #substitute of cloak part


        cv2.imshow("red cloak", result_1+result_2)            #combining both the red part and red free part
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

