import cv2
vidcap = cv2.VideoCapture('www.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*80))
  success,image = vidcap.read()
  print('Read a new frame: ', success, count)
  count += 1

# import cv2
# vidcap = cv2.VideoCapture('01.mp4')
# success,image = vidcap.read()
# count = 0
# while success:
#   cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   count += 1
  
# # Program To Read video
# # and Extract Frames
# import cv2
  
# # Function to extract frames
# def FrameCapture(path):
      
#     # Path to video file
#     vidObj = cv2.VideoCapture(path)
  
#     # Used as counter variable
#     count = 0
  
#     # checks whether frames were extracted
#     success = 1
  
#     while success:
  
#         # vidObj object calls read
#         # function extract frames
#         success, image = vidObj.read()
  
#         # Saves the frames with frame-count
#         cv2.imwrite("frame%d.jpg" % count, image)
  
#         count += 1
  
# # Driver Code
# if __name__ == '__main__':
  
#     # Calling the function
#     FrameCapture("C:\\Users\\user\\Documents\\Coding\\TFODCourse\\TOOLS\\extract_from_video\\save\\01.mp4")