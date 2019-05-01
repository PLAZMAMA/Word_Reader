import numpy as np 
import PIL

class Image():
    def __init__(self, image_file):
        self.image = PIL.Image.open(image_file)
        self.image = np.asarray(self.image)
        ###normalize the image

    def vert_crop(self):
        """crops the vertical whitespace of the image"""
        pass


    def preprocessing(self, image):
        """preprocceses a given image"""
        pass