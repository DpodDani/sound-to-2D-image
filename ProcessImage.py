from PIL import Image
import os, argparse

def generate_color_matrix(filePath, paletteID):

    if paletteID == 0:
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

    colorMatrix = convert_color_palette(colorMatrix, paletteID, width) #Convert RGB to color palette

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

def convert_color_palette(colorMatrix, paletteID, width):
    if(paletteID == 1):
        for w in range(0, width):
            for h in range(0, width):
                RGB = colorMatrix[w][h]
                convRGB = []
                for i in range (3):
                    print(RGB[i])
                    print(RGB[i] / 128)
                    convRGB.append( (RGB[i] / 128) * 255 ) #Takes each RGB value and takes it to either 0 or 255
                colorMatrix[w][h] = convRGB

    # if(paletteID == 2):
    #     for w in range(0, width):
    #         for h in range(0, width):
    #             RGB = colorMatrix[w][h]
    #             convRGB = [-1 for num in range(3)]
    #             for i in range (0,3):
    #                 convRGB[i] = int(RGB[i] / 64) * 85  #Takes each RGB value and takes it to either 0, 85, 170 or 255
    #             colorMatrix[w][h] = convRGB
    # return colorMatrix
