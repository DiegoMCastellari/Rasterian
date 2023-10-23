import os
import numpy as np
import rasterio
from scale_intensity_correction import scale_intensity

# Create stacked
def stack_bands(raster_list):
    band_list = []
    for id, layer in enumerate(raster_list, start=1):
        with rasterio.open(layer) as src1:
            img = src1.read(1)
            band_list.append(img)
            src1.close()
    raster_stacked = np.stack(band_list, axis=0)
    return raster_stacked

def create_stacked_raster(band_rasters_folder_dir):
    # bands images names
    raster_list = []
    for img in os.listdir(band_rasters_folder_dir):
        raster_list.append(band_rasters_folder_dir+img)
    print(raster_list)
    # Create stacked
    raster = stack_bands(raster_list)
    return raster

def stack_new_bands_to_raster(original_image, new_image_bands):
    band_list = []
    # original image
    original_bands = len(original_image)
    for img in original_bands:
        band_list.append(original_image[img])
    # new image
    new_bands = len(new_image_bands)
    for img in new_bands:
        band_list.append(new_image_bands[img])
    # Create stacked
    raster_stacked = np.stack(band_list, axis=0)
    return raster_stacked