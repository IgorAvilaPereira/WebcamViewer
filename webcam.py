import cv2

cv2.namedWindow("WebCamViewer")
# para verificar qual index de sua webcam. No Linux: sudo apt install v4l-utils && v4l2-ctl --list-devices
vc = cv2.VideoCapture(3)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
while rval:
    cv2.imshow("WebCamViewer", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
vc.release()
cv2.destroyWindow("WebCamViewer")