def conv_3x3_mean(band, N):
    band_1 = band[0]
    len_array = len(band_1)
    img_conv = []

    for c in range(len_array):
        if c == 0:
            conv_1 = np.convolve(band_1[c], np.ones(N), mode='same')
            conv_2 = np.convolve(band_1[c+1], np.ones(N), mode='same')
            conv = (conv_1 + conv_2) /6
        elif c == (len_array-1):
            conv_0 = np.convolve(band_1[c-1], np.ones(N), mode='same')
            conv_1 = np.convolve(band_1[c], np.ones(N), mode='same')
            conv = (conv_0 + conv_1) /6
        else:
            conv_0 = np.convolve(band_1[c-1], np.ones(N), mode='same')
            conv_1 = np.convolve(band_1[c], np.ones(N), mode='same')
            conv_2 = np.convolve(band_1[c+1], np.ones(N), mode='same')
            conv = (conv_0 + conv_1 + conv_2) / 9
        
        img_conv.append(conv)
    img_conv = np.array([img_conv]).round(2)
    return img_conv

def create_convolution_band (path_image, output_folder_path):

    opened_img = rasterio.open(path_image)
    image = opened_img.read()

    meta = opened_img.meta
    meta.update(count = 1, driver='GTiff')
    meta.update(dtype=rasterio.float32)

    for i in range(len(image)): 

        band_conv = conv_3x3_mean(np.array([image[0]]), 3)

        with rasterio.open(output_folder_path+"convoolution_"+str(i)+".tif", 'w', **meta) as dst:
            dst.write(band_conv.astype(rasterio.float32))
    
    opened_img.close()
    dst.close()