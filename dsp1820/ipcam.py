import cv2

cam = cv2.VideoCapture("rtsp://192.168.0.157/live/ch00_0")
#cam = cv2.VideoCapture("rtsp://192.168.0.157:554?user=admin&pwd=admin&action=stream")
while True:
    ret, img = cam.read()
    cv2.imshow('getCamera', img)
    if 0xFF & cv2.waitKey(5)==27:
        break
cv2.destroyAllWindows()