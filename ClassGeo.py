import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import *

class LatlonPointer(): 
    def __init__(self):
        self.lat = None
        self.lon = None
        self.shapefile = None

    def finder(self,returnval):
        zipcode=self.shapefile
        if(np.isnan(self.lat)==True):
            return 0
        else:
            lat=np.float64(self.lon)
            lon= np.float64(self.lat)
            co = Point(lat,lon)
            df=zipcode.intersects(co)
            
            ind=df[df==True]
            if len(ind)>0:
                ind= ind.index[0]
                return zipcode[returnval][ind]

