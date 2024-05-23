# RASTERIAN
Satellite raster data processing and analysis python module.
The module can be use to create and correct raster data, make local and global calculations, classify pixels and vectorize it to polygons.
Raster data can be read from and saved to files; but all the processing use and return numpy arrays for a faster result.

# Page: 
- [Rasterian Page](https://diegomcastellari.github.io/views/rasterian/main.html)        
- [Rasterian Documentation](https://diegomcastellari.github.io/views/rasterian/documentation.html)

## Python Dependencies
- Numpy (numpy==1.26.1)
- Pandas (pandas==2.1.1)
- Geopandas (geopandas==0.14.0)
- Rasterio (rasterio==1.3.9)
- Scikit-Image (scikit-image==0.22.0)
- Scikit-Learn (scikit_learn==1.3.2)
- Matplotlib (matplotlib==3.8.0)

# Installation
Download the rasterian-0.0.1.tar.gz file in the dist folder.    
Into the python enviroment, run:     
```python 
pip install rasterian-0.0.1.tar.gz
```

# Examples of use
Into the examples folder, there are some examples of use:    
- 01 - How to stack bands in one unique raster
- 02 - How to apply filters
- 03 - How to calculate indexes    

##### Next example: labels extration and raster supervised classification

       