import cv2 
import os
import time 

# Open the device at the ID 0
time_threshold = 3
directory = "/home/vudh1/Desktop"
output_dir = "output"
cap = cv2.VideoCapture(0) 

#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
	print("Could not open video device")
else:
	original_time = time.time()

	os.chdir(directory) 
	os.mkdir("output")
	os.chdir(output_dir)

#To set the resolution
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

	cnt = -1

	while(True):

# Capture frame-by-frame
		ret, frame = cap.read()

# Display the resulting frame
		# cv2.imshow("preview",frame)

		time_span = int(time.time() - original_time)
		
		if (time_span % time_threshold) == 0 and time_span/time_threshold != cnt:
			cnt += 1
			filename = "savedImage-"+str(cnt)+".jpg"
			cv2.imwrite(filename, frame)

	#Waits for a user input to quit the application

		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()