import arcpy
from arcpy import env

env.workspace = r'D:\RetroStudy\2016\polys_temp.gdb'
ws = env.workspace

env.overwriteOutput = True

fcs = arcpy.ListFeatureClasses()

codeblock1 = """def switchTurf(valInput):
  return 4"""

codeblock2 = """def ShadowOne(valInput):
  return 4"""

codeblock3 = """def ShadowTwo(valInput):
  return 3"""

for fc in fcs:
    print fc
    #make selected feature
    arcpy.MakeFeatureLayer_management(fc, "lyr")
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 4 AND Shape_Area <= 10")
    arcpy.DeleteFeatures_management("lyr")
    
    #select turf < 30 ft
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 4 AND Shape_Area <= 30")
    arcpy.MakeFeatureLayer_management("lyr", "lyr_smallTurf")
    
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 4")
    
    arcpy.SelectLayerByLocation_management("lyr_smallTurf", "WITHIN_A_DISTANCE", "lyr", "1", "NEW_SELECTION")
    arcpy.CalculateField_management("lyr_smallTurf", "gridcode", "switchTurf(!gridcode!)", "PYTHON_9.3", codeblock1)

    arcpy.SelectLayerByAttribute_management("lyr", "CLEAR_SELECTION")
    arcpy.SelectLayerByAttribute_management("lyr", "CLEAR_SELECTION")
    
    #select shadow class
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 2")
    arcpy.MakeFeatureLayer_management("lyr", "lyr_shadow")
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 4")
    arcpy.SelectLayerByLocation_management("lyr_shadow", "WITHIN_A_Distance", "lyr", "1", "NEW_SELECTION")
    arcpy.CalculateField_management("lyr_shadow", "gridcode", "ShadowOne(!gridcode!)", "PYTHON_9.3", codeblock2)

    arcpy.SelectLayerByLocation_management("lyr_shadow", "WITHIN_A_Distance", "lyr", "1", "NEW_SELECTION", "INVERT")
    
    arcpy.CalculateField_management("lyr_shadow", "gridcode", "ShadowTwo(!gridcode!)", "PYTHON_9.3", codeblock3)

    """arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 1 AND Shape_Area > 30")
    
    arcpy.MakeFeatureLayer_management("lyr", "lyr_largeTurf")
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "gridcode = 4")
    arcpy.MakeFeatureLayer_management("lyr", "lyr_trees")
    inputs_List = ["lyr_trees", "lyr_largeTurf", "lyr_shadow"]


    arcpy.CreateFeatureclass_management(ws, fc + "_output")
    
    arcpy.SelectLayerByAttribute_management("lyr_shadow", "CLEAR_SELECTION")
    arcpy.SelectLayerByAttribute_management("lyr_smallTurf", "CLEAR_SELECTION")
    
    arcpy.Append_management("lyr_trees", ws + '\\' + fc + "_output", "NO_TEST")
    arcpy.Append_management("lyr_largeTurf", ws + '\\' + fc + "_output", "NO_TEST")
    arcpy.Append_management("lyr_shadow", ws + '\\' + fc + "_output", "NO_TEST")
    arcpy.Append_management("lyr_smallTurf", ws + '\\' + fc + "_output", "NO_TEST")
    
    arcpy.CopyFeatures_management(ws + '\\' + fc + "_output", "E:\LiDAR_factor\Polys_OutputCleanedTest.gdb\\" + fc)"""

    
    
    
