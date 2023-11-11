import pandas as pd
import rasterio
# from rasterio.plot import show

""" def plot_raster(raster_path, cmap='terrain'):
    raster = rasterio.open(raster_path)
    show((raster, 3), cmap=cmap) """

def get_meta(raster_path):
    with rasterio.open(raster_path) as src0:
        meta = src0.meta
    src0.close()
    return meta

def image_to_file(image, meta, output_raster_path):
    # Update meta to reflect the number of layers
    meta.update(count = len(image))
    # Save image bands
    with rasterio.open(output_raster_path, 'w', **meta) as dst:
        for id, layer in enumerate(image, start=1):
            dst.write_band(id, layer)
    dst.close()


### DATA FRAME TRANSFORMATION
def df_to_image(df_data, output_shape):
    shape_size = output_shape[0] * output_shape[1] * output_shape[2]
    df_size = len(df_data) * len(df_data.columns)

    if (shape_size == df_size):
        array_sample = df_data.to_numpy()
        array_sample_reshaped = array_sample.reshape(output_shape[0], output_shape[1], output_shape[2])
        return array_sample_reshaped
    else:
        print(f"ERROR: shape size ({shape_size}) is not equal to gdf size ({df_size}).-")

def image_to_gdf(image):
    gdf_from_array = pd.DataFrame(image.reshape(image.shape[1] * image.shape[2], image.shape[0]))
    return gdf_from_array