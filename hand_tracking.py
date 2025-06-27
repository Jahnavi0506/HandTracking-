import cv2 as cv
import mediapipe as mp
import time
cap=cv.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands("""static_image_mode=False,
                     max_num_hands=2,
                     min_detection_confidence=0.5,
                     min_tracking_confidence=0.5""")

mpdraw=mp.solutions.drawing_utils
pTime=0
cTime=0

while True:
    success,img=cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks :
        for handLms in results.multi_hand_landmarks:
            for Id,lm in enumerate(handLms.landmark):
                #print(Id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(Id,cx,cy)
                if Id==4:
                    cv.circle(img,(cx,cy),15,(255,0,255),cv.FILLED)
            mpdraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)       
    pTime=cTime
    cv.putText(img,f'FPS:{int(fps)}',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv.imshow("Image",img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    #cv.waitKey(1)
cap.release()
cv.destroyAllWindows()