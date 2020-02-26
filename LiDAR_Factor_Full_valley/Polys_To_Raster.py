import arcpy, os, sys, string
from arcpy import env

env.workspace = r'D:\LiDAR_Factor_Full_valley\diff_images_2014_2016\FinalCalculations'

output = r'D:\LiDAR_Factor_Full_valley\diff_images_2014_2016\FinalOutput.gdb'

rasters = arcpy.ListRasters()

for raster in rasters:
    try:
        print 'converting raster ' + raster
        
        arcpy.RasterToPolygon_conversion(raster, output + '\\' + raster[:-4])
    except:
        print "failed to convert " + raster



print 'merging features'

env.workspace = output

fcs = arcpy.ListFeatureClasses()

Merge_List = []

for fc in fcs:
    Merge_List.append(fc)

arcpy.Merge_management(Merge_List, output + '\\' + 'Merged_Final')

