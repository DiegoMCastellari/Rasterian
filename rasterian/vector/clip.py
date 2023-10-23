def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

def clip_raster_by_polygon (raster_path, polygon_path, tag):
    in_file = raster_path 
    crs_epsg = 32621

    gdf_muestras = gpd.read_file(polygon_path)
    gdf_muestras = pd.concat([gdf_muestras, gdf_muestras.bounds], axis=1)
    gdf_muestras.head()

    for i in range(len(gdf_muestras)):

        if tag == 'muestras':
            out_file = r"./muestras/"+sat_img_folders+"/"+gdf_muestras.loc[i,'class']+"_"+str(gdf_muestras.loc[i,'id'])+"_"+str(i)+".tif"   
        elif tag == 'aoi':
            out_file = "./aoi/"+sat_img_folders+"/area_de_estudio_"+sat_img_folders+".tif" 
        minx, miny = gdf_muestras.loc[i,'minx'], gdf_muestras.loc[i,'miny']
        maxx, maxy = gdf_muestras.loc[i,'maxx'], gdf_muestras.loc[i,'maxy']

        bbox = box(minx, miny, maxx, maxy)
        geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(crs_epsg))
        # geo = geo.to_crs(crs=data.crs.data)
        coords = getFeatures(geo)

        dataset = rasterio.open(in_file)
        out_img, out_transform = mask(dataset, shapes=coords, crop=True)
        
        out_meta = dataset.meta.copy()
        # epsg_code = int(dataset.crs.data['init'][5:])
        out_meta.update({
            "driver": "GTiff",
            "height": out_img.shape[1],
            "width": out_img.shape[2],
            "transform": out_transform
            }
        )
        with rasterio.open(out_file, "w", **out_meta) as dest:
            dest.write(out_img)

    dataset.close()
    dest.close()