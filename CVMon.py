
import os
import cv2
import time

cam1 = cv2.VideoCapture("rtsp://username:password@<ip-address>:<port>")

while True:
	r1, frame1 = cam1.read()
	if r1:
		cv2.imshow("View", frame1)

	k = cv2.waitKey(1)
	if k & 0xFF == ord("q"): # Exit condition
		break