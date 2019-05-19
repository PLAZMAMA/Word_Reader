from Img import Img
from sklearn import svm
import numpy as np
from random import randint
from PIL import Image
import os
import matplotlib.pyplot as plt

class Model():
    def __init__(self):
        self.classes = np.array(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])

    def train_test_split(self, size = 20):
        """
        creates the data from the data/letters folder and returns x_train, y_train, x_test, y_test
        size(the precent of the test data that is taken from the whole data)
        """
        x = [] #features
        y = [] #labels 

        #extracts the data from the letters folder
        num_label = 0
        for folder in self.classes:
            folder_len = os.listdir(f"data/letters/{folder}")
            folder_len = [file for file in folder_len if ".png" in file]
            folder_len = len(folder_len)
            for i in range(folder_len):
                letter_img = Image.open(f"data/letters/{folder}/{i}.png") #gets the image
                letter_img = np.asarray(letter_img, dtype = np.float64) #converts the image to a numpy array
                x.append(letter_img)
                y.append(np.where(self.classes == folder)[0][0])
            num_label += 1

        #suffles the data
        for i in range(len(x)*10):
            r_i = randint(0, len(x) - 1) #creates a random index to pop from the list
            #pops same element from x and y
            pop_x = x.pop(r_i)
            pop_y = y.pop(r_i)
            #appends each popped element to each corresponding list
            x.append(pop_x)
            y.append(pop_y)

        percent_split = int((size * len(x)) / 100)

        
        #splits the data to train and test data
        x_train = np.array(x[:-percent_split])
        y_train = np.array(y[:-percent_split])
        x_test = np.array(x[percent_split:])
        y_test = np.array(y[percent_split:])
        
        return(x_train, y_train, x_test, y_test)

    def fit(self):
        """trains the model on the data"""
        x_train, y_train, x_test, y_test = self.train_test_split() #creates the training and testing data
        #flattens the arrays of the images 35x35->1225
        flat_x_train = [im.flatten() for im in x_train]
        flat_x_test = [im.flatten() for im in x_test]
        x_train = np.array(flat_x_train)
        x_test = np.array(flat_x_test)
        self.model = svm.SVC(C = 2,gamma = "auto", kernel = "poly", tol = 1e-8) #defines the model
        self.model.fit(x_train, y_train) #trains the model
        accuracy = self.model.score(x_test, y_test)
        print(f"score: {accuracy}") #displayes the testing score

    def predict(self, img_path):
        """predicts a given picture of a word and returns the prediction"""
        img = Img(img_path)
        letters = img.preprocess()
        word = ""
        #runs throught each letter, predicts them and adds each to the word
        for letter in letters:
            prediction = self.model.predict(letter)
            word += self.classes[prediction]

        return(word)