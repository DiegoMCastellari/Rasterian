import rasterio
# from rasterio.plot import show

""" def plot_raster(raster_path, cmap='terrain'):
    raster = rasterio.open(raster_path)
    show((raster, 3), cmap=cmap) """

def get_meta(raster):
    with rasterio.open(raster) as src0:
        meta = src0.meta
    src0.close()
    return meta

def raster_to_file(image, meta, output_image):
    # Update meta to reflect the number of layers
    meta.update(count = len(image))
    # Save image bands
    with rasterio.open(output_image, 'w', **meta) as dst:
        for id, layer in enumerate(image, start=1):
            dst.write_band(id, layer)
    dst.close()