# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KugEfeEWk_mCChr_vFt2oYCMRmVejJaO
"""

!pip install xarray 
!pip install dask
!pip install netCDF4
!pip install bottleneck



# Commented out IPython magic to ensure Python compatibility.
import xarray

# %matplotlib inline
# single file
dataDIR = '/content/drive/MyDrive/Colab Notebooks/CAM5-1-0.25degree_All-Hist_est1_v3_run1.cam.h2.2009-12-01-00000.nc'

DS = xarray.open_dataset(dataDIR)
DS

# clip by the shape file 
geo_lims = {'lat':[6,36],'lon':[68,98]}

ds_n = DS.sel(lat=slice(*geo_lims['lat']),lon=slice(*geo_lims['lon'])).load()

#save to new ncfile 
dataDIR = '/content/drive/MyDrive/Colab Notebooks/India_CAM5-1-0.25degree_All-Hist_est1_v3_run1.cam.h2.2009-12-01-00000.nc'
ds_n.to_netcdf(dataDIR)