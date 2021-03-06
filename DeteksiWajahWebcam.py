# xml deteksi wajah https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# xml deteksi mata https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640) # ubah lebar cam menjadi 640
cam.set(4, 480) # ubah tinggi cam menjadi 480
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeDetector = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
  retVal, frame = cam.read() # akan menghasilkan 2 nilai, boolean dan frame/gambarnya.
  frame = cv2.flip(frame,1) # menghilangkan mirror effect
  greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = faceDetector.detectMultiScale(greyscale, 1.3, 5) # scale factor dari 0 < 2, utk optimasi biasanya menggunakan angka ini
  eyes = eyeDetector.detectMultiScale(greyscale, 1.3, 5)
  
  for (x, y, w, h) in faces:
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
  
  for (x, y, w, h) in eyes:
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
  
  frame = cv2.putText(frame, 'Face', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
  
  cv2.imshow('Face Detection Screen', frame)
  # cv2.imshow('Webcamku 2', greyscale)

  # terminate condition
  keyTerminate = cv2.waitKey(1) & 0xFF
  if keyTerminate == 27 or keyTerminate == ord('q'):
    break

cam.release()
cv2.destroyAllWindows()