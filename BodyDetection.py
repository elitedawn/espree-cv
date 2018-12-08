import os
import cv2
import time

person_cascade = cv2.CascadeClassifier(
	os.path.join('./models/haarcascade_fullbody.xml')
)
cam1 = cv2.VideoCapture("rtsp://username:password@<ip-address>:<port>")

while True:
	r1, frame1 = cam1.read()
	if r1:
		start_time = time.time()
		# frame1 = cv2.resize(frame1,(640,360))
		gray_frame = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
		rects = person_cascade.detectMultiScale(gray_frame)
						
		for (x, y, w, h) in rects:
			cv2.rectangle(frame1, (x,y), (x+w,y+h),(0,255,0),2)
		cv2.imshow("Channel 1", frame1)
	k = cv2.waitKey(1)
	if k & 0xFF == ord("q"): # Exit condition
		break