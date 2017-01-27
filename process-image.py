from PIL import Image
import os, argparse

# Initialises the argument parser
parser = argparse.ArgumentParser()
# Adds the required arguments
parser.add_argument("imageFilePath", help="The file path of the image to be processed") # by default this is a string
parser.add_argument("--usage", help="python process-image.py <path_to_file>\nPreferably the image should be in the same folder as this python module")
# Enables the use of these arguments in the code below
args = parser.parse_args()

myImage = Image.open(args.imageFilePath).convert('L') # converts image to greyscale
pix = myImage.load() # loads it as a Pixel Access Object
height = myImage.size[1] # the height of the image
width = myImage.size[0] # the width of the image

def set_matrix_dimensions():
    """
        Sets the dimension of the matrix (a 2D array) using the height and width of the image specified
    """
    greyscaleMatrix = [[0 for num in range(height)] for num in range(width)] # initialises everything to 0

    print("Height", height)
    print("Width", width)

    return greyscaleMatrix

def populate_greyscale_matrix(greyscaleMatrix):
    for w in range(0, width):
        for h in range(0, height):
            # print("x:", w)
            # print("y:", h)
            greyscaleColor = pix[w, h] # 0 = black, 255 = white
            # print(" --> greyscale color:", greyscaleColor)
            greyscaleMatrix[w][h] = greyscaleColor

    print greyscaleMatrix

greyscaleMatrix = set_matrix_dimensions() # Obtain matrix (all elements are zero)
populate_greyscale_matrix(greyscaleMatrix) # Populate the matrix with the greyscale values
