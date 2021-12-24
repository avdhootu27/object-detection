import cv2

cap = cv2.VideoCapture(0)

tracker = cv2.legacy.TrackerMOSSE_create()
success, img = cap.read()

bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)

while True:
    success, img = cap.read()
    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break