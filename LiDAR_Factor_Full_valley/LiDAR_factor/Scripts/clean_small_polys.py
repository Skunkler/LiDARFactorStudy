import arcpy
from arcpy import env

env.workspace = r'E:\LiDAR_factor\Turf_final.gdb'

env.overwriteOutput = True

fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    print fc
    arcpy.MakeFeatureLayer_management(fc, "lyr")
    #arcpy.MakeFeatureLayer_management(fc, "lyr2")
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "Shape_Area <= 10")
    #arcpy.SelectLayerByAttribute_management("lyr2", "NEW_SELECTION", "Shape_Area > 10")
    #arcpy.SelectLayerByLocation_management("lyr", "WITHIN_A_DISTANCE", "lyr2", "1", "NEW_SELECTION", "INVERT")
    arcpy.DeleteFeatures_management("lyr")
    arcpy.SelectLayerByAttribute_management("lyr", "CLEAR_SELECTION")
    #arcpy.SelectLayerByAttribute_management("lyr2", "CLEAR_SELECTION")
