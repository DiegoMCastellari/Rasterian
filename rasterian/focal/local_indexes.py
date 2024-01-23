import numpy as np
from .local_math import *

sat_message = "Posible satelite values: landsat_7, landsat_8 or sentinel_2.-"

### COMMON INDEXES
# -->  NDVI GNDVI NDMI EVI AVI SAVI MSI GCI NBRI BSI NDWI NDSI NDGI NDBI UI BU BAEM

# Normalized Difference Vegetation Index (NDVI):
# NDVI = (NIR – Red) / (NIR + Red)
def index_ndvi(image, satelite):
    if satelite == 'landsat_7':
        b1 = image[3 - 1]
        b2 = image[4 - 1]
    elif satelite == 'landsat_8':
        b1 = image[4 - 1]
        b2 = image[5 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[4 - 1]
        b2 = image[8 - 1]
    else:
        print(sat_message)
        return "ERROR"
    
    index_value = index_norm(b1, b2)
    return index_value

# Green Normalized Difference Vegetation Index (GNDVI):
# GNDVI = (NIR-GREEN) /(NIR+GREEN)
def index_gndvi(image, satelite):
    if satelite == 'landsat_7':
        b1 = image[2 - 1]
        b2 = image[4 - 1]
    elif satelite == 'landsat_8':
        b1 = image[3 - 1]
        b2 = image[5 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[3 - 1]
        b2 = image[8 - 1]
    else:
        print(sat_message)
        return "ERROR"
    
    index_value = index_norm(b1, b2)
    return index_value

# Enhanced Vegetation Index (EVI):
# EVI = G * ((NIR - R) / (NIR + C1 * R – C2 * B + L))
def index_evi(image, satelite):

    if satelite == 'landsat_7':
        b1 = image[3 - 1]
        b2 = image[4 - 1]
        b3 = image[1 - 1]
    elif satelite == 'landsat_8':
        b1 = image[4 - 1]
        b2 = image[5 - 1]
        b3 = image[2 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[4 - 1]
        b2 = image[8 - 1]
        b3 = image[2 - 1]
    else:
        print(sat_message)
        return "ERROR"
    
    index_value = 2.5 * ((b2.astype(float) - b1.astype(float)) / (b2 + 6 * b1 - 7.5 * b3 + 1))
    return index_value

# Advanced Vegetation Index (AVI):
# AVI = [NIR * (1-Red) * (NIR-Red)] 1/3
def index_avi(image, satelite):

    if satelite == 'landsat_7':
        b1 = image[3 - 1]
        b2 = image[4 - 1]
    elif satelite == 'landsat_8':
        b1 = image[4 - 1]
        b2 = image[5 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[4 - 1]
        b2 = image[8 - 1]
    else:
        print(sat_message)
        return "ERROR"

    np.seterr(divide='ignore', invalid='ignore')
    index_value = (b2.astype(float) * (1 - b1.astype(float)) * (b2 - b1)) ** (1. / 3)
    return index_value

# Soil Adjusted Vegetation Index (SAVI):
# SAVI = ((NIR – R) / (NIR + R + L)) * (1 + L)
def index_savi(image, satelite):
    np.seterr(divide='ignore', invalid='ignore')
    if satelite == 'landsat_7':
        b1 = image[3 - 1]
        b2 = image[4 - 1]
        index_value = (b2.astype(float) - b1.astype(float)) / (b2 + b1 + 0.5) * (1.5)
    elif satelite == 'landsat_8':
        b1 = image[4 - 1]
        b2 = image[5 - 1]
        index_value = (b2.astype(float) - b1.astype(float)) / (b2 + b1 + 0.5) * (1.5)
    elif satelite == 'sentinel_2':
        b1 = image[4 - 1]
        b2 = image[8 - 1]
        index_value = (b2.astype(float) - b1.astype(float)) / (b2 + b1 + 0.428) * (1.428)
    else:
        print(sat_message)
        return "ERROR"
    
    return index_value

# Normalized Difference Moisture Index (NDMI):
# NDMI = (NIR – SWIR) / (NIR + SWIR)
def index_ndmi(image, satelite):
    if satelite == 'landsat_7':
        b1 = image[5 - 1]
        b2 = image[4 - 1]
    elif satelite == 'landsat_8':
        b1 = image[6 - 1]
        b2 = image[5 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[11 - 1]
        b2 = image[8 - 1]
    else:
        print(sat_message)
        return "ERROR"
    
    index_value = index_norm(b1, b2)
    return index_value

# Moisture Stress Index (MSI):
# MSI = MidIR / NIR
def index_msi(image, satelite):

    if satelite == 'landsat_7':
        b1 = image[4 - 1]
        b2 = image[5 - 1]
    elif satelite == 'landsat_8':
        b1 = image[5 - 1]
        b2 = image[6 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[8 - 1]
        b2 = image[11 - 1]
    else:
        print(sat_message)
        return "ERROR"

    index_value = index_ratio(b1, b2)
    return index_value

# Green Coverage Index (GCI):
# GCI = (NIR) / (Green) – 1
def index_gci(image, satelite):

    if satelite == 'landsat_7':
        b1 = image[2 - 1]
        b2 = image[4 - 1]
    elif satelite == 'landsat_8':
        b1 = image[3 - 1]
        b2 = image[5 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[3 - 1]
        b2 = image[9 - 1]
    else:
        print(sat_message)
        return "ERROR"

    index_value = index_norm(b1, b2) - 1
    return index_value

# Normalized Burned Ratio Index (NBRI):
# NBRI = (NIR – SWIR) / (NIR+ SWIR)
def index_nbri(image, satelite):

    if satelite == 'landsat_7':
        b1 = image[7 - 1]
        b2 = image[4 - 1]
    elif satelite == 'landsat_8':
        b1 = image[7 - 1]
        b2 = image[5 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[12 - 1]
        b2 = image[8 - 1]
    else:
        print(sat_message)
        return "ERROR"

    index_value = index_norm(b1, b2)
    return index_value

# Bare Soil Index (BSI):
# BSI = ((Red+SWIR) – (NIR+Blue)) / ((Red+SWIR) + (NIR+Blue))
def index_bsi(image, satelite):

    if satelite == 'landsat_7':
        b1 = image[3 - 1]
        b2 = image[5 - 1]
        b3 = image[1 - 1]
        b4 = image[4 - 1]
    elif satelite == 'landsat_8':
        b1 = image[4 - 1]
        b2 = image[6 - 1]
        b3 = image[2 - 1]
        b4 = image[5 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[4 - 1]
        b2 = image[11 - 1]
        b3 = image[2 - 1]
        b4 = image[8 - 1]
    else:
        print(sat_message)
        return "ERROR"

    index_value = ((b2 + b1) - (b4 + b3)) / ((b2 + b1) + (b4 + b3))
    return index_value

# Normalized Difference Water Index (NDWI):
# NDWI = (NIR – SWIR) / (NIR + SWIR)
def index_ndwi(image, satelite):
    if satelite == 'landsat_7':
        b1 = image[4 - 1]
        b2 = image[2 - 1]
    elif satelite == 'landsat_8':
        b1 = image[5 - 1]
        b2 = image[3 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[8 - 1]
        b2 = image[3 - 1]
    else:
        print(sat_message)
        return "ERROR"
    
    index_value = index_norm(b1, b2)
    return index_value

# Normalized Difference Snow Index (NDSI):
# NDSI = (Green-SWIR) / (Green+SWIR)
def index_ndsi(image, satelite):
    if satelite == 'landsat_7':
        b1 = image[5 - 1]
        b2 = image[2 - 1]
    elif satelite == 'landsat_8':
        b1 = image[6 - 1]
        b2 = image[3 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[11 - 1]
        b2 = image[3 - 1]
    else:
        print(sat_message)
        return "ERROR"
    
    index_value = index_norm(b1, b2)
    return index_value

# Normalized Difference Glacier Index (NDGI):
# NDGI = (NIR-Green)/(NIR+Green)
def index_ndgi(image, satelite):
    if satelite == 'landsat_7':
        b1 = image[3 - 1]
        b2 = image[2 - 1]
    elif satelite == 'landsat_8':
        b1 = image[4 - 1]
        b2 = image[3 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[4 - 1]
        b2 = image[3 - 1]
    else:
        print(sat_message)
        return "ERROR"
    
    index_value = index_norm(b1, b2)
    return index_value

# NDBI: Normalized Difference Built-up Index (Índice de Diferencia Normalizada Edificada)
# NDBI= (SWIR-NIR)/ (SWIR+NIR)
def index_ndbi(image, satelite):

    if satelite == 'landsat_7':
        b1 = image[4 - 1]
        b2 = image[5 - 1]
    elif satelite == 'landsat_8':
        b1 = image[5 - 1]
        b2 = image[6 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[8 - 1]
        b2 = image[11 - 1]
    else:
        print(sat_message)
        return "ERROR"

    index_value = index_norm(b1, b2)
    return index_value

# Urban Index
# UI = SWIR2 - NIR / SWIR2 + NIR
def index_ui(image, satelite):
    if satelite == 'landsat_7':
        b1 = image[4 - 1]
        b2 = image[7 - 1]
    elif satelite == 'landsat_8':
        b1 = image[5 - 1]
        b2 = image[7 - 1]
    elif satelite == 'sentinel_2':
        b1 = image[8 - 1]
        b2 = image[12 - 1]
    else:
        print(sat_message)
        return "ERROR"

    index_value = index_norm(b1, b2)
    return index_value

# Build Up index
# BU = NDBI - NDVI
def index_bu(image, satelite):
    index_value_ndvi = index_ndvi(image, satelite)
    index_value_ndbi = index_ndbi(image, satelite)
    index_value = index_value_ndbi - index_value_ndvi
    return index_value

# built-up area extraction method (BAEM)
# BAEM = NDBI - NDVI - MNDWI
def index_baem(image, satelite):
    index_value_bu = index_bu(image, satelite)
    index_value_ndwi = index_ndwi(image, satelite)
    index_value = index_value_bu - index_value_ndwi
    return index_value


# GLOBAL FUNCTION

def calculate_index(image, index_name, satellite):

    if index_name == 'ndvi':
        index_value = index_ndvi(image, satellite)
    elif index_name == 'gndvi':
        index_value =index_gndvi(image, satellite)
    elif index_name == 'evi':
        index_value =index_evi(image, satellite)
    elif index_name == 'avi':
        index_value =index_avi(image, satellite)
    elif index_name == 'savi':
        index_value =index_savi(image, satellite)
    elif index_name == 'ndmi':
        index_value =index_ndmi(image, satellite)
    elif index_name == 'msi':
        index_value =index_msi(image, satellite)
    elif index_name == 'gci':
        index_value =index_gci(image, satellite)
    elif index_name == 'nbri':
        index_value =index_nbri(image, satellite)
    elif index_name == 'bsi':
        index_value =index_bsi(image, satellite)
    elif index_name == 'ndwi':
        index_value =index_ndwi(image, satellite)
    elif index_name == 'ndsi':
        index_value =index_ndsi(image, satellite)
    elif index_name == 'ndgi':
        index_value =index_ndgi(image, satellite)
    elif index_name == 'ndbi':
        index_value =index_ndbi(image, satellite)
    elif index_name == 'ui':
        index_value =index_ui(image, satellite)
    elif index_name == 'bu':
        index_value =index_bu(image, satellite)
    elif index_name == 'baem':
        index_value =index_baem(image, satellite)

    return index_value