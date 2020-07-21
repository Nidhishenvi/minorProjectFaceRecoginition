import numpy as np
import cv2
import pickle
from twilio.rest import Client

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels={"person_name":1}
with open("labels.pickle","rb") as f :
    og_labels=pickle.load(f)
labels={v:k for k,v in og_labels.items()}

video=cv2.VideoCapture(0)
visited = False
while (True) :
    ret,frame=video.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.3,5)
    
    for (x,y,w,h) in faces :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            roi_grey=grey[y:y+h,x:x+w]
            roi_color=frame[y:y+h,x:x+w]
            id_, conf= recognizer.predict(roi_grey)
            
            if id_== 2 and visited==False :
                print("hello")
                account_sid = 'ACd6380ec451a762cda90dae02f88949a3'
                auth_token = 'd573fa958ba6766c55c5bb2ad41dd0cf'
                myPhone = '+917899539745'
                TwilioNumber = '+12058096027'
                client = Client(account_sid, auth_token)
                client.messages.create(to=myPhone,from_=TwilioNumber,body='Alert!Your child is out of the gate ' + u'\U0001f680')
                print("MESSAGE SENT")
                visited = True
                
            if conf>=45 and conf<=85 :
                print(id_)
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color=(255,255,255)
                stroke=2
                cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            img_item="my.png"
            cv2.imwrite(img_item,roi_grey)
    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
            break;
video.release()
cv2.destroyAllWindows()
