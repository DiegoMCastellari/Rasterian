from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

""" with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read() """

# Setting up
setup(
    name="rasterian",
    version='0.0.1',
    author="Diego M Castellari",
    author_email="<diegomcastellari@gmail.com>",
    description='Rasterian - Raster Analysis Package',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'geopandas==0.14.0',
        'matplotlib==3.8.0',
        'numpy==1.26.1',
        'pandas==2.1.1',
        'rasterio==1.3.9',
        'scikit_learn==1.3.2',
        'scikit-image==0.22.0'
        ],
    keywords=['python', 'raster', 'analysis', 'satellite', 'remote sensing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)