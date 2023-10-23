def calculate_index(path_band_1, path_band_2, index_name, out_file_path, path_band_3=""):
    band_1 = rasterio.open(path_band_1)
    band_2 = rasterio.open(path_band_2)
    b1 = band_1.read()
    b2 = band_2.read()
    if path_band_3 != "":
        band_3 = rasterio.open(path_band_3)
        b3 = band_3.read()
    np.seterr(divide='ignore', invalid='ignore')
    
    # Calculate index
    if (index_name == 'ndvi') | (index_name == 'gndvi') | (index_name == 'ui') | (index_name == 'ndbi') | (index_name == 'ndbi') | (index_name == 'ndmi') | (index_name == 'ndwi'):
        index_value = (b2.astype(float)-b1.astype(float))/(b2+b1)
    elif index_name == 'evi':
        index_value = 2.5 * ((b2.astype(float) - b1.astype(float)) / (b2 + 6 * b1 - 7.5 * b3 + 1))
    elif index_name == 'savi':
        index_value = (b2.astype(float)-b1.astype(float))/(b2+b1+0.428) * (1.428)
    elif index_name == 'msi':
        index_value =  b2.astype(float) / b1
    elif index_name == 'bu':
        index_value = ((b2.astype(float)-b1.astype(float))/(b2+b1)) - ((b1.astype(float)-b3.astype(float))/(b1+b3))

    print(index_name, '- shape:', index_value.shape)
    # Write the NDVI imagea
    meta = band_1.meta
    meta.update(driver='GTiff')
    meta.update(dtype=rasterio.float32)

    with rasterio.open(out_file_path, 'w', **meta) as dst:
        dst.write(index_value.astype(rasterio.float32))
    
    band_1.close()
    band_2.close()
    dst.close()