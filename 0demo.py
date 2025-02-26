import cv2 as cv

#resiszng the frame of live video, its working for all videos,live and images
def resizedFrame(frame,scale=75):
    width=int(frame.shape[1]*scale/100)
    height=int(frame.shape[0]*scale/100)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
'''def changeRes(width,height):
    #only for live video another method for live video
    capture.set(3,width)
    capture.set(4,height)'''
# Open the default camera (0), or use 1, 2 for external cameras
capture = cv.VideoCapture(0)


# Check if the camera opened successfully
if not capture.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    isTrue, frame = capture.read()
    if not isTrue:  # Break if frame is not read (camera error)
        print("Error reading frame.")
        break
    #change image to other type
    converted_color=cv.cvtColor(frame,cv.COLOR_BGR2YUV)
    # Resize the frame
    resized_frame=resizedFrame(converted_color,scale=110)
    cv.imshow('Webcam', resized_frame)

    # Press 'd' to exit
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release resources
capture.release()
cv.destroyAllWindows()
