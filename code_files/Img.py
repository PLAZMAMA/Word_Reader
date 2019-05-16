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

    def prepare(self):
        """prepares the image to start the preprocessing process"""
        img = np.asarray(self.image)
        img = img.tolist()
        for array in img:
            for i in range(len(array)):
                if array[i] > 125:
                    array[i] = 255
        img = np.array(img, dtype = np.float64)
        self.image = Image.fromarray(img).convert("L")


    def preprocess(self):
        """
        preprocceses the image and returns the cropped numpy arrays of each letter in the same sequance of the original image
        
        returns the letters as a list of normalized numpy arrays
        """
        self.prepare()
        self.image = ImageOps.invert(self.image) #inverts the color of the image to help is the cutting process
        self.image = np.asarray(self.image)
        #self.image = preprocessing.normalize(self.image) 
        letters = self.to_letters()
        #resizes all the letters into same shape and size while keeping the aspect ratio
        for i in range(len(letters)):
            letter = Image.fromarray(np.uint8(letters[i])) #it doesnt work because the image is normalized
            letter.thumbnail((35,35))
            letter.convert("L")
            bg_img = Image.new("L", (35,35))
            loc = (int(bg_img.width/2 - letter.width/2), int(bg_img.height/2 - letter.height/2))
            bg_img.paste(letter, loc)
            bg_img = np.asarray(bg_img)
            bg_img = preprocessing.normalize(bg_img) #normalizes the array of the image for the model
            letters[i] = bg_img
        self.image = Image.fromarray(self.image)

        return(letters)
