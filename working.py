import numpy as np
import rasterio
from shapely.geometry import Point, Polygon
import geopandas as gpd
import random
#import matplotlib.pyplot as plt
import gpd_lite_toolbox as glt

import numpy as np
import rasterio
from shapely.geometry import Point, Polygon
import geopandas as gpd
import random

import ee
import gee_subset
from gooey import Gooey

########################################
#    Uncomment this to generate GUI.   #
#									   #
#@gooey                                #
#def main():                           #
#	return None                        #
#                                      #
#if __name__ == '__main__':            #
#    main()                            #
########################################

file = r'/data/gadm36_PHL_1.geojson'

data = gpd.read_file(file)

data.tail()

def get_random_point_in_polygon():
    province = raw_input('select province to compute bounds: ')
    AOI = data[data.NAME_1 == province]
    AOI_bounds = AOI.bounds
    AOI_geometry = AOI.geometry
    return AOI_geometry


polygon = get_random_point_in_polygon()
print polygon