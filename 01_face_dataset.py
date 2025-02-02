import csv
import cv2
import os

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640) 
cam.set(4, 480) 

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

filename="Id_Name_ref_sheet.csv"
ogdata=[]

id = input('\n enter face id end press <return> ==>  ')
name = input('\n enter face name end press <return> ==>  ')

with open(filename,"r",newline='') as csvfile:
    filereader=csv.reader(csvfile)
    for row in filereader:
        ogdata.append(row)

data=[id,name]
ogdata.append(data)
print(ogdata)

with open(filename,"w",newline='') as csvfile:
    filewriter=csv.writer(csvfile)
    filewriter.writerows(ogdata)

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
count = 0

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
                
        #cv2.imwrite("dataset/User." + str(id) + '.' + str(count) + ".jpg", img)
        cv2.imwrite("dataset/User." + str(id) + '.' + str(count) + "."+name+".jpg", gray[y:y+h,x:x+w])
        
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff 
    if k == 27:
        break
    elif count >= 30: 
         break

cam.release()
cv2.destroyAllWindows()


