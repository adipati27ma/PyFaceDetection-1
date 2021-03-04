import cv2

cam = cv2.VideoCapture(0)

while True:
  retVal, frame = cam.read() # akan menghasilkan 2 nilai, boolean dan frame/gambarnya.
  cv2.imshow('Webcamku', frame)

  # terminate condition
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cam.release()
cv2.destroyAllWindows()