import numpy as np
from scipy.signal import convolve # correlate

def conv_media(band, n):
    matrix_ones = np.ones((n, n))
    img_conv = convolve(band, matrix_ones, mode='same')

    image_ones = np.ones(band.shape) 
    img_conv_ones = convolve(image_ones, matrix_ones, mode='same')

    result = img_conv / img_conv_ones
    return result

def conv_matrix(band, matrix):
    matrix = np.array(matrix)
    img_conv = convolve(band, matrix, mode='same')

    matrix_ones = np.ones(matrix.shape)
    image_ones = np.ones(band.shape)
    img_conv_ones = convolve(image_ones, matrix_ones, mode='same')

    result = img_conv / img_conv_ones
    return result

def conv_image(image, matrix_n):
    band_list = []
    if type(matrix_n) == list:
        for b in range(len(image)):
            img = conv_matrix(image[b], matrix_n)
            band_list.append(img)
    elif type(matrix_n) == int:
        for b in range(len(image)):
            img = conv_media(image[b], matrix_n)
            band_list.append(img)
    else:
        print("Posible matrix_n values types: list or int.-")

    raster_stacked = np.stack(band_list, axis=0)
    return raster_stacked