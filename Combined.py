from ProcessImage import generate_color_matrix
from HilbertCurve import hilbertmatrix
from VectorToMusic import generateMusic

import numpy as np
import math
from PIL import Image
import os, argparse

vect = []

# Initialises the argument parser
parser = argparse.ArgumentParser()
# Adds the required arguments
parser.add_argument("imageFilePath", help="The file path of the image to be processed") # by default this is a string
parser.add_argument("--usage", help="python ProcessImage.py <path_to_file>\nPreferably the image should be in the same folder as this python module")
# Enables the use of these arguments in the code below
args = parser.parse_args()



paletteID = int(input('Enter color palette type: (0 = greyscale, 1 = RGB-8bit, 2 = RGB-16bit)'))

colorMatrix = generate_color_matrix(args.imageFilePath, paletteID) #Generate the greyscale matrix

vect = hilbertmatrix(colorMatrix) #Turns matrix into vector using Hilbert curve

tempo = int(input('Enter desired tempo:'))
scaleType = int(input('Enter scale type (0 = Chromatic, 1 = Diatonic):'))

generateMusic(vect, tempo, scaleType) #Generates the music as a MIDI file using the vector
