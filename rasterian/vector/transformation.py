import geopandas as gpd
import rasterio
from rasterio.features import shapes

def raster_to_polygon(raster_path):
    mask = None
    with rasterio.Env():
        with rasterio.open(raster_path) as src:
            raster_crs = src.meta['crs']
            image = src.read(1) # first band
            results = (
                {'properties': {'raster_val': v}, 'geometry': s}
                for i, (s, v) in enumerate(
                    shapes(image, mask=mask, transform=src.transform))
            )
    src.close()
    gpd_polygonized_raster = gpd.GeoDataFrame.from_features(list(results)) 
    gpd_polygonized_raster = gpd_polygonized_raster.set_crs(raster_crs)
    return gpd_polygonized_raster
