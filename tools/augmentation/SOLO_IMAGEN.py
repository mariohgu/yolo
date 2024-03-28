import imgaug as ia
from imgaug import augmenters as iaa
import os
import sys
import argparse
import cv2
import numpy as np
from glob import glob


cwd = os.path.dirname(os.path.abspath(__file__))
#### Define control variables and parse user inputs
parser = argparse.ArgumentParser()
parser.add_argument('--imgdir', help='Folder containing images to augment', default=cwd+'\input')
                    #required=True)
parser.add_argument('--imgext', help='File extension of images (for example, .JPG)',
                    default='.jpg')
parser.add_argument('--labels', help='Text file with list of classes', default=cwd+'\labels.txt')
                    #required=True)
parser.add_argument('--num', help='Number of augmented images to create from each original image',
                    default=5)
parser.add_argument('--debug', help='Displays every augmented image when enabled',
                    default=False)
parser.add_argument('--dirout', help='Folder output', default=cwd+'\output')

args = parser.parse_args()

DIR_OUT=args.dirout
if not os.path.isdir(DIR_OUT):
    print('%s is not a valid directory.' % DIR_OUT)
    sys.exit(1)
IMG_DIR = args.imgdir
if not os.path.isdir(IMG_DIR):
    print('%s is not a valid directory.' % IMG_DIR)
    sys.exit(1)
IMG_EXTENSION = args.imgext
LABEL_FN = args.labels
if not os.path.isfile(LABEL_FN):
    print('%s is not a valid file path.' % LABEL_FN)
    sys.exit(1)
NUM_AUG_IMAGES = args.num
debug = args.debug
#cwd = os.getcwd()
count=0

seq1 = iaa.Sequential([
#    iaa.Resize({"height": 450, "width": 450}),  #resize image   

#     iaa.Fliplr(0.5),            # Horizontal flip 50% of images
#     iaa.Rot90((1, 3)),           #rotate
#     #iaa.CoarseDropout(p=0.02, size_percent=0.5,per_channel=True),   #Generates a dropout mask at 5 to 50 percent of each input image’s size.                          
     iaa.Crop(percent=(0.04, 0.05)),                # Crop all images between 0% to 20%                
#     #iaa.GaussianBlur(sigma=(0, 1)),             # Add slight blur to images
#     iaa.Multiply((0.7, 1.3), per_channel=0.2),  # Slightly brighten, darken, or recolor images
#    # iaa.Convolve(matrix=matrix),                #sharpener
#     iaa.Affine(
#        scale={"x": (0.8, 1.2), "y": (0.8,1.2)},                # Resize image
# ##        translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)}, # Translate image
#         rotate=(-15, 15),                                         # Rotate image
#         mode=ia.ALL, cval=(125)  )                             # Filling in extra pixels
    
    ])


img_fns = glob(IMG_DIR + '/*' + IMG_EXTENSION)

for img_fn in img_fns:
    count+=1

    # Open image, get shape and base filename
    original_img = cv2.imread(img_fn)
    imgH, imgW, _ = original_img.shape
    base_img_fn = os.path.split(img_fn)[-1]
    base_fn = base_img_fn.replace(IMG_EXTENSION,'')
    print("Imagen numero ",count)
    for n in range(int(NUM_AUG_IMAGES)):
        
        # Define new filenames
        img = np.copy(original_img)
        seq1_det = seq1.to_deterministic()
        img_aug = seq1_det.augment_images([img])[0]
        
        img_aug_fn = 'C' + base_fn + IMG_EXTENSION
        img_aug_path = os.path.join(cwd,DIR_OUT,img_aug_fn)
        cv2.imwrite(img_aug_path,img_aug)
        
        
        if debug:
            
            img_show = np.copy(img)
            img_aug_show = np.copy(img_aug)
            
            if n == 0:
                cv2.imshow('Normal',img_show)
            
            cv2.imshow('Augmented %d' % n,img_aug_show)
            cv2.waitKey()

if debug:
    cv2.destroyAllWindows()