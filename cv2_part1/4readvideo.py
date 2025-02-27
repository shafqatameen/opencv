import cv2 as cv
capture =cv.VideoCapture('videos/dog.mp4')
if not capture.isOpened():
    print('Error: Could not open video.')
    exit()
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print('End of video or Error reading video.')
        break
    cv.imshow('dog video', frame)
    if cv.waitKey(33)==ord('z'):
        break
capture.release()
cv.destroyAllWindows()