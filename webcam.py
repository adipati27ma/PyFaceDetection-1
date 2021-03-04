import cv2

cam = cv2.VideoCapture(0)

while True:
  retVal, frame = cam.read() # akan menghasilkan 2 nilai, boolean dan frame/gambarnya.
  abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('Webcamku', frame)
  cv2.imshow('Webcamku 2', abuAbu)

  # terminate condition
  keyTerminate = cv2.waitKey(1) & 0xFF
  if keyTerminate == 27 or keyTerminate == ord('q'):
    break

cam.release()
cv2.destroyAllWindows()