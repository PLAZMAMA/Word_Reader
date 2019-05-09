import numpy as np
from PIL import Image , ImageOps
from sklearn import preprocessing
import matplotlib.pyplot as plt

class Img():
    def __init__(self, image_file):
        self.image = Image.open(image_file).convert("L")
        
    def part_vert_crop(self, img):
        """crops the starting vertical whitespace of the image"""
        crop_img = []
        for row in img:
            if np.sum(row) != 0:
                crop_img.append(row)
            elif len(crop_img) != 0:
                crop_img.append(row)

        return(crop_img)

    def vert_crop(self, img):
        """verticaly crops the image and returns it as a numpy array"""
        cropped_image = self.part_vert_crop(img) #calls the function to remove the whitespace ontop
        cropped_image = self.part_vert_crop(cropped_image[::-1]) #calls the function to remove the whitespace on the bottom
        cropped_image = cropped_image[::-1] #since the funtion returns the image flipped because we gave it the image flipped, we are flipping it back
        
        return(np.array(cropped_image))

    def to_letters(self):
        """seperates the image of the word to the same sequence of letters"""
        letters = []
        crop_img = [[] for _ in range(self.image.shape[0])]
        for column in range(self.image.shape[1]):
            if np.sum(self.image[:,column]) != 0:
                for i in range(len(crop_img)):
                    crop_img[i].append(self.image[i,column])

            elif len(crop_img[0]) != 0:
                crop_img = np.array(crop_img)
                letters.append(crop_img)
                crop_img = [[] for _ in range(self.image.shape[0])]

        for i in range(len(letters)):
            letters[i] = self.vert_crop(letters[i])

        return(letters)


    def preprocess(self):
        """preprocceses the image and returns the cropped numpy arrays of each letter in the same sequance of the original image and returns the letters as a list of numpy arrays"""
        self.image = ImageOps.invert(self.image) #inverts the color of the image to help is the cutting process
        self.image = np.asarray(self.image)
        self.image = preprocessing.normalize(self.image) #normalizes the image for the model
        letters = self.to_letters()
        return(letters)