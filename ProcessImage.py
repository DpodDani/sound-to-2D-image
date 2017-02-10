from PIL import Image
import os, argparse

def generate_color_matrix(filePath,colorType):

    if colorType == 0:
        myImage = Image.open(filePath).convert('L') # converts image to greyscale
    else:
        myImage = Image.open(filePath).convert('RGB') # converts image to greyscale

    pix = myImage.load() # loads it as a Pixel Access Object

    if myImage.size[1] != myImage.size[0]:
        raise ValueError('Input image must be square')

    width = myImage.size[0] # the height & width of the image

    colorMatrix = set_matrix_dimensions(width) # Obtain matrix (all elements are zero)

    populate_matrix(colorMatrix, width, pix) # Populate the matrix with the greyscale values
    print(colorMatrix)
    return colorMatrix


def set_matrix_dimensions(width):
    """
        Sets the dimension of the matrix (a 2D array) using the height and width of the image specified
    """
    colorMatrix = [[0 for num in range(width)] for num in range(width)] # initialises everything to 0

    print("Height", width)
    print("Width", width)

    return colorMatrix

def populate_matrix(colorMatrix, width, pix):
    for w in range(0, width):
        for h in range(0, width):
            # print("x:", w)
            # print("y:", h)
            color = pix[w, h] #Stored as RGB values in an array
            colorMatrix[w][h] = color
