import arcpy
from arcpy import env

env.workspace = r'E:\LiDAR_factor\Classified_final'

env.overwriteOutput = True

rasters = arcpy.ListRasters()

dsc = arcpy.Describe(r'E:\LiDAR_factor\o13912_ne.tif')
coord_sys = dsc.spatialReference


for raster in rasters:
    try: 
        print "projecting " + raster
        arcpy.DefineProjection_management(raster, coord_sys)
        print "succuess projecting " + raster + " to " + str(coord_sys)
    except:
        print arcpy.GetMessages(2)
