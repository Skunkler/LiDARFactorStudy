import arcpy
from arcpy import env

env.workspace = r'D:\LiDAR_Factor_Full_valley\diff_images_2014_2016\FinalOutput.gdb'

output = r'D:\LiDAR_Factor_Full_valley\diff_images_2014_2016\FinalCalc.gdb'

fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    if fc != 'Merged_Final':
        print 'dissolving ' + fc
        arcpy.Dissolve_management(fc, output + '\\' + fc + '_dis', ['gridcode'])


"""env.workspace = output

fcs = arcpy.ListFeatureClasses()

fc_list = []

for fc in fcs:
    fc_list.append(fc)

arcpy.Merge_management(fc_list, output + '\\' + 'Merged_Final')
"""
