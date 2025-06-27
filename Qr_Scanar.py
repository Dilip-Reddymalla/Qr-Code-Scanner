import cv2
from pyzbar.pyzbar import decode
import time


cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)


while True:
    
    success, frames = cam.read()
    
    if not success:
        print("Error in accessing the camera.")
        break
    
    cv2.imshow("QR Code Scanner", frames)
    key = cv2.waitKey(1)

    scanned_codes = decode(frames)
    
    if scanned_codes:
        for code in scanned_codes:
            data = code.data.decode('utf-8')
            print("QR Code Data:", data)
            time.sleep(5)
        break

    
