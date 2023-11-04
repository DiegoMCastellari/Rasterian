import numpy as np 

def index_norm(band_1, band2):
    np.seterr(divide='ignore', invalid='ignore')
    index_value = (band2.astype(float)-band_1.astype(float))/(band2+band_1)
    return index_value

def index_ratio(band_1, band_2):
    np.seterr(divide='ignore', invalid='ignore')
    index_value =  band_2.astype(float) / band_1
    return index_value

def calc_index(image, band_1, band_2, index_type):
    b1 = image[band_1 - 1]
    b2 = image[band_2 - 1]
    np.seterr(divide='ignore', invalid='ignore')

    if index_type == 'band_norm':
        index_norm(b1, b2)
    elif index_type == 'ratio':
        index_ratio(b1, b2)
    else:
        print("Posible index_type values: band_norm or ratio.-")