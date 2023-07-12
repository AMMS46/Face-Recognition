import cv2
import face_recognition
from simple_facerec import SimpleFacerec

'''img= cv2.imread("image1\Messi.webp")
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_encoding= face_recognition.face_encodings(rgb_img)[0]

img2= cv2.imread("image1\Elon Musk.jpg")
rgb_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img_encoding2= face_recognition.face_encodings(rgb_img2)[0]

result= face_recognition.compare_faces([img_encoding],img_encoding2)
print("Result: ",result)

cv2.imshow("Img",img)
cv2.imshow('Img 2',img2)
cv2.waitKey(0)'''


#encoding images
sfr = SimpleFacerec()
sfr.load_encoding_images("D:\pro1\source code\images\image1")



#load camera
cap=cv2.VideoCapture(0)

# ret is blooean value which indicates wheter frame was succesfully read or not
# frame is numpy array which represent the image of current frame
while True:
    ret, frame = cap.read()

    #detect faces

    face_locations,face_names = sfr.detect_known_faces(frame)
    for face_loc,name in zip(face_locations,face_names):

#y1=top,x2=right,y2=bottom,x1=left
        y1,x2,y2,x1=face_loc[0],face_loc[1],face_loc[2],face_loc[3]
        cv2.putText(frame,name,(x1,y1 -10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
        cv2.rectangle(frame, (x1,y1),(x2,y2),(0,0,200),4)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
#releases the vid capture object
#destroy all the windows tht were created  by opencv()
cap.release()
cv2.destroyAllWindows()




