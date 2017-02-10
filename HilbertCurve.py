
import numpy as np
import math
vect = []



def hilbertmatrix(greyscaleMatrix):             # decides initial shape based on size of matrix
    mat = np.matrix(np.array(greyscaleMatrix))

    if ((2*math.log(len(mat)) % 4,2) == 0):
        recursion(mat, 2)
    else:
        recursion(mat, 1)

    return vect

def recursion(mat, shape):

    m = len(mat)

    if (m == 2):                    # adds in the pixel values to the vector
        if (shape == 1):
            #print('shape1', m)
            vect.append(mat[0,0])
            vect.append(mat[0,1])
            vect.append(mat[1,1])
            vect.append(mat[1,0])
        elif (shape == 2):
            #print('shape2', m)
            vect.append(mat[0,0])
            vect.append(mat[1,0])
            vect.append(mat[1,1])
            vect.append(mat[0,1])
        elif (shape == 3):
            #print('shape3', m)
            vect.append(mat[1,1])
            vect.append(mat[1,0])
            vect.append(mat[0,0])
            vect.append(mat[0,1])
        else:
            #print('shape4', m)
            vect.append(mat[1,1])
            vect.append(mat[0,1])
            vect.append(mat[0,0])
            vect.append(mat[1,0])
    else:
        #print(m)
        #print(m//2)
        array1 = mat[0:((m//2)), 0:((m//2))]
        array2 = mat[(m//2):(m), 0:((m//2))]
        array3 = mat[0:((m//2)), (m//2):(m)]
        array4 = mat[(m//2):(m), (m//2):(m)]
        if (shape == 1):
            #print('shape1', m)                 # makes a |   | shape
            recursion(array1, 2)                #         |___|
            recursion(array3, 1)                #
            recursion(array4, 1)
            recursion(array2, 4)
        elif (shape == 2):
            #print('shape2', m)
            #array1
            #print(array1)
            recursion(array1, 1)                # makes a ___ shape
            recursion(array2, 2)                #            |
            recursion(array4, 2)                #         ___|
            recursion(array3, 3)
        elif (shape == 3):
            #print('shape3', m)
            recursion(array4, 4)                # makes a ____ shape
            recursion(array2, 3)                #        |    |
            recursion(array1, 3)                #        |    |
            recursion(array3, 1)
        else:
            #print('shape4', m)
            recursion(array4, 3)                # makes a ___ shape
            recursion(array3, 4)                #        |
            recursion(array1, 4)                #        |___
            recursion(array2, 1)
