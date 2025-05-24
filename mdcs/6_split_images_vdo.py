# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("C:\\Users\\Dhayanithi\\Music\\MUSIC_$$$\\vedhalam.mp4")

try:
    # Creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

# Frame counter
currentframe = 0

while True:
    # Reading from frame
    ret, frame = cam.read()

    if ret:
        # If video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # Writing the extracted images
        cv2.imwrite(name, frame)

        # Increasing counter
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
