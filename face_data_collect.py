import cv2

video = cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    cv2.imshow("Frame",frame)
    key_exit=cv2.waitKey(1)
    if key_exit==ord('q'):
        break

video.release()
cv2.destroyAllWindows()