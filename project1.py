

import cv2

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# A haar Cascade is basically a classifier which is used to detect particular object from the source.

# The haarcascade_frontalface_default.xml is haar cascade designed by opencv to detect the frontal face.

imp_img = cv2.VideoCapture("elon.jpg") 

res, img = imp_img.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 
 # detect faces of differnt sizes in the input image
 # (gray_image, Sacle factor, minneighbor)
faces = detect.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    # To draw a rectangle in a face
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)


cv2.imshow("Elon Image", img)

cv2.waitKey(0)
# Close the window
imp_img.release()
cv2.destroyAllWindows()
