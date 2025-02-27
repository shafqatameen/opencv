import cv2 as cv

# resizing frame of video or image
def rescaleFrame(frame,scale=75):
    width=int(frame.shape[1]*scale//100)
    height=int(frame.shape[0]*scale//100)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
frame=cv.imread('images/cat_large.jpg')
cv.imshow('Cat',frame)
rescaled_frame=rescaleFrame(frame,25)
cv.imshow('Cat reduced to 75%',rescaled_frame)
cv.waitKey(0)

'''import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Calculate the new dimensions based on the scale
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Resize the frame using the calculated dimensions
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Example usage:
# Assuming 'frame' is an image or video frame loaded using OpenCV
frame = cv.imread('images/cat.jpg')
resized_frame = rescaleFrame(frame, scale=0.5)
cv.imshow('Resized Frame', resized_frame)
cv.waitKey(0)'''