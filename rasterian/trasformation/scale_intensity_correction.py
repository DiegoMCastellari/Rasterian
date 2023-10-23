import numpy as np
from skimage import exposure

# Return image after stretching or shrinking its intensity levels.
def rescale_intensity(image):
    image_bands = len(image)
    band_list = []
    for img in range(image_bands):
        p2, p98 = np.percentile(img, (2, 98))
        img[img <= p2] = p2
        img[img >= p98] = p98
        img_rescale = exposure.rescale_intensity(img, in_range=(p2, p98))
        band_list.append(img_rescale)
    raster_stacked = np.stack(band_list, axis=0)
    return raster_stacked

# Return image after histogram equalization.
def equalize_hist(image):
    image_bands = len(image)
    band_list = []
    for img in range(image_bands):
        p2, p98 = np.percentile(img, (2, 98))
        img[img <= p2] = p2
        img[img >= p98] = p98
        img_rescale = exposure.equalize_hist(img) * 255
        band_list.append(img_rescale)
    raster_stacked = np.stack(band_list, axis=0)
    return raster_stacked

# Contrast Limited Adaptive Histogram Equalization (CLAHE).
def equalize_adapthist(image):
    image_bands = len(image)
    band_list = []
    for img in range(image_bands):
        img_rescale = exposure.equalize_adapthist(image[img], clip_limit=0.03) * 255
        band_list.append(img_rescale)
    raster_stacked = np.stack(band_list, axis=0)
    return raster_stacked

def scale_intensity(image, correction_type):
    if correction_type == 'rescale_intensity':
        img_rescale = rescale_intensity(image)
    elif correction_type == 'equalize_hist':
        img_rescale = rescale_intensity(image)
    elif correction_type == 'equalize_adapthist':
        img_rescale = rescale_intensity(image)
    else:
        print('Posible values: rescale_intensity, equalize_hist or equalize_adapthist')
    return img_rescale