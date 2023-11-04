import geopandas as gdf

""" 
def process_urban_area (gdf, file_name):
    gdf.geometry = gdf.buffer(25)
    gdf.geometry = gdf.buffer(-15)
    gdf = gdf.dissolve(by='raster_val')
    gdf = gdf.explode()
    gdf = gdf.loc[gdf.area > gdf.area.min()*1.4]
    gdf.geometry = gdf.buffer(5)
    gdf.geometry = gdf.buffer(-4)
    gdf.to_file("./results/shp_urban_areas/"+file_name+".shp")
    print("----- FINISH:", file_name)
 """