import numpy as np
import PIL
from sklearn import preprocessing

class Image():
    def __init__(self, image_file):
        self.image = PIL.Image.open(image_file)
        self.image.convert("L") #converts the image to grey scale
        self.image = np.asarray(self.image)
        self.image = PIL.ImageOps.invert(self.image) #inverts the color of the image to help is the cutting process
        self.image = preprocessing.normalize(self.image) #normalizes the image for the model

    def vert_crop(self):
        """crops the vertical whitespace of the image"""
        crop_img = []
        for row in self.image:
            if np.sum(row) != 0:
                crop_img.append(row)

        return(crop_img)

    def to_letters(self):
        """seperates the image of the word to the same sequence of letters"""
        letters = []
        crop_img = []
        for row in range(len(self.image[:,0])):
            if np.sum(self.image[:,i]) != 0:
                for i in range(len(self.image[:,0])):
                    crop_img.append(self.image[row,i])

            elif len(crop_img) != 0:
                letters.append(crop_img)
                crop_img = []

        return(letters)


    def preprocessing(self, image):
        """preprocceses a given image"""
        pass