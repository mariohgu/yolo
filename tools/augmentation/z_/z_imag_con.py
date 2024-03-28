# import cv2
# import numpy as np

# path = r'C:\Users\user\Documents\Coding\TFODCourse\Tensorflow\workspace\images\collectedimages\wea_shoo_v3\p1\CA00001.jpg'
# img = cv2.imread(path)
# cv2.imshow('Original', img)

# #Identity kernel
# kernel1 = np.array([[0,0,0], [0, 1,0], [0,0,0]])
# im1 = cv2.filter2D(img, -1, kernel1)
# cv2.imshow('Identity kernel', im1)

# #sharpening kernel
# kernel2 = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])
# im2 = cv2.filter2D(img, -1, kernel2)
# cv2.imshow('Sharpening kernel', im2)

# #blurring kernel
# kernel3 = np.array([[0.02040816, 0.02040816, 0.02040816, 0.02040816, 0.02040816,
#         0.02040816, 0.02040816],
#        [0.02040816, 0.02040816, 0.02040816, 0.02040816, 0.02040816,
#         0.02040816, 0.02040816],
#        [0.02040816, 0.02040816, 0.02040816, 0.02040816, 0.02040816,
#         0.02040816, 0.02040816],
#        [0.02040816, 0.02040816, 0.02040816, 0.02040816, 0.02040816,
#         0.02040816, 0.02040816],
#        [0.02040816, 0.02040816, 0.02040816, 0.02040816, 0.02040816,
#         0.02040816, 0.02040816],
#        [0.02040816, 0.02040816, 0.02040816, 0.02040816, 0.02040816,
#         0.02040816, 0.02040816],
#        [0.02040816, 0.02040816, 0.02040816, 0.02040816, 0.02040816,
#         0.02040816, 0.02040816]])
# im3 = cv2.filter2D(img, -1, kernel3)
# cv2.imshow('Blurring kernel', im3)

from keras.preprocessing.image import ImageDataGenerator
from skimage import io
import numpy as np
import os
from PIL import Image
import cv2


# Construct an instance of the ImageDataGenerator class
# Pass the augmentation parameters through the constructor. 

datagen = ImageDataGenerator(
        #rotation_range=45,     #Random rotation between 0 and 45
        #width_shift_range=0.2,   #% shift
        #height_shift_range=0.2,
        #shear_range=0.2,
        #zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='constant', cval=125)    #Also try nearest, constant, reflect, wrap

dataset = []

kernel1 = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]]) #AQUI

image_directory = 'test_folder/'
SIZE = 512

my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):        
        image = io.imread(image_directory + image_name)
        
        image = cv2.filter2D(image, -1, kernel1) #AQUI

        image = Image.fromarray(image, 'RGB')
        image = image.resize((SIZE,SIZE))
        
        dataset.append(np.array(image))

x = np.array(dataset)

i = 0
for batch in datagen.flow(x, batch_size=16,  
                          save_to_dir='augmented', #nombre del directorio raiz de la imagen
                          save_prefix='aug', 
                          save_format='jpg'):
    i += 1
    if i >= 2:
        break  # otherwise the generator would loop indefinitely 