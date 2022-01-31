# Imports
import os
import cv2
import time
import numpy as np


# If "DCIM" directory is not there, create it and 'cd DCIM'
if not os.path.exists('DCIM'):
    os.makedirs('DCIM')
    os.chdir('DCIM')

# Else 'cd DCIM' 
else:
    os.chdir('DCIM')


# Set video capture device
cap = cv2.VideoCapture(0)

# Take photo every n number of seconds
while True:
    error, frame = cap.read()
    timestr = time.strftime("%Y_%m_%d__%H_%M_%S")
    cv2.imwrite("IMG___{}.png".format(timestr), frame)
    time.sleep(86400)# in seconds
