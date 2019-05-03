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

    def part_vert_crop(self, img):
        """crops the starting vertical whitespace of the image"""
        crop_img = []
        for row in img:
            if np.sum(row) != 0:
                crop_img.append(row)
            elif len(crop_img) != 0:
                crop_img.append(row)

        return(crop_img)

    def vert_crop(self):
        croppeed_image = self.part_vert_crop(self.image) #calls the function to remove the whitespace ontop
        croppeed_image = self.part_vert_crop(croppeed_image[::-1]) #calls the function to remove the whitespace on the bottom
        cropped_image = cropped_image[::-1] #since the funtion returns the image flipped because we gave it the image flipped, we are flipping it back

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