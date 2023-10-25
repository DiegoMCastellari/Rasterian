import pandas as pd
import geopandas as gpd
from shapely.geometry import box
from fiona.crs import from_epsg
import rasterio 
from rasterio.mask import mask
from ..tools import image_array_to_gdf

def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

def create_bbox_polygon(gdf_poly, output_crs):
    gdf_poly_bounds = gdf_poly.bounds
    minx, miny = gdf_poly_bounds.minx, gdf_poly_bounds.miny
    maxx, maxy = gdf_poly_bounds.maxx, gdf_poly_bounds.maxy
    bbox = box(minx, miny, maxx, maxy)
    gdf_bbox = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=output_crs)
    return gdf_bbox

def clip_raster_by_polygon(raster, gdf_poly):
    bbox_coords = getFeatures(gdf_poly)
    out_img, out_transform = mask(raster, shapes=bbox_coords, crop=True)
    
    out_meta = raster.meta.copy()
    out_meta.update({
        "driver": "GTiff",
        "height": out_img.shape[1],
        "width": out_img.shape[2],
        "transform": out_transform
        }
    )
    return out_img, out_meta

def create_raster_samples_tiles(raster_path, gdf_polys, output_folder):
    raster = rasterio.open(raster_path)
    raster_crs = raster.meta['crs']
    gdf_polys = gdf_polys.to_crs(crs=raster_crs)
    
    for i in range(len(gdf_polys)):   
        poly_id = gdf_polys.loc[i, 'id']
        poly_descrip = gdf_polys.loc[i, 'descrip']
        
        gdf_bbox = create_bbox_polygon(gdf_polys.iloc[[i]], raster_crs)
        out_img, out_meta = clip_raster_by_polygon(raster, gdf_bbox)
        
        if output_file[-1] != '/':
            output_file = output_file+"/"
        output_file = output_folder + poly_descrip+"/"+poly_id+".tif"
        with rasterio.open(output_file, "w", **out_meta) as dest:
            dest.write(out_img)
        dest.close()
    raster.close()

def create_raster_samples_gdf(raster_path, gdf_polys):
    raster = rasterio.open(raster_path)
    raster_crs = raster.meta['crs']
    gdf_polys = gdf_polys.to_crs(crs=raster_crs)
    gdf_output = pd.DataFrame([])
    
    for i in range(len(gdf_polys)):
        poly_id = gdf_polys.loc[i, 'id']
        poly_class = gdf_polys.loc[i, 'class']

        gdf_bbox = create_bbox_polygon(gdf_polys.iloc[[i]], raster_crs)
        out_img, out_meta = clip_raster_by_polygon(raster, gdf_bbox)

        gdf_sample = image_array_to_gdf(out_img)
        gdf_sample['class'] = poly_class
        gdf_sample['img_id'] = poly_id
        if len(gdf_output) == 0:
            gdf_output = gdf_sample
        else:
            gdf_output = pd.concat([gdf_output, gdf_sample])

    return gdf_output