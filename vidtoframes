import cv2
def save_vid_to_images(filename):
    print("Starting Video")
    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
    print("Video frame capturing Complete")


save_vid_to_images("Video_1.avi")
    
