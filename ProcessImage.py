from PIL import Image
import os, argparse

def set_matrix_dimensions(height, width):
    """
        Sets the dimension of the matrix (a 2D array) using the height and width of the image specified
    """
    greyscaleMatrix = [[0 for num in range(height)] for num in range(width)] # initialises everything to 0

    print("Height", height)
    print("Width", width)

    return greyscaleMatrix

def populate_greyscale_matrix(greyscaleMatrix, height, width, pix):
    for w in range(0, width):
        for h in range(0, height):
            # print("x:", w)
            # print("y:", h)
            greyscaleColor = pix[w, h] # 0 = black, 255 = white
            # print(" --> greyscale color:", greyscaleColor)
            greyscaleMatrix[w][h] = greyscaleColor


def generate_greyscale_matrix(myImage):
    pix = myImage.load() # loads it as a Pixel Access Object
    height = myImage.size[1] # the height of the image
    width = myImage.size[0] # the width of the image

    greyscaleMatrix = set_matrix_dimensions(height, width) # Obtain matrix (all elements are zero)
    populate_greyscale_matrix(greyscaleMatrix, height, width, pix) # Populate the matrix with the greyscale values

    return greyscaleMatrix
