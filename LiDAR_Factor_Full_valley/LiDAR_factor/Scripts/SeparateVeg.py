import arcpy
from arcpy import env

env.workspace = r'E:\LiDAR_factor\PolyTest.gdb'
env.overwriteOutput = True

TreeOutput = r'E:\LiDAR_factor\Tree_final.gdb'
TurfOutput = r'E:\LiDAR_factor\Turf_final.gdb'



fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    arcpy.MakeFeatureLayer_management(fc, "lyr")
    
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 4")
    arcpy.CopyFeatures_management("lyr", TreeOutput + '\\' + fc + "_trees")
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 1")
    arcpy.CopyFeatures_management("lyr", TurfOutput + '\\' + fc + "_turf")
    arcpy.SelectLayerByAttribute_management("lyr", "CLEAR_SELECTION")
    
