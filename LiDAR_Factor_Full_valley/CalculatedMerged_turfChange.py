import arcpy
from arcpy import env

env.workspace = r'D:\LiDAR_Factor_Full_valley\diff_images_2014_2016\FinalOutput.gdb'

output = r'D:\LiDAR_Factor_Full_valley\diff_images_2014_2016\outMerged.gdb'

env.overwriteOutput = True
fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    if fc != 'Merged_Final':
        print 'grabbing turf from ' + fc
        arcpy.MakeFeatureLayer_management(fc, 'fc_lyr')
        arcpy.SelectLayerByAttribute_management('fc_lyr', 'NEW_SELECTION', 'gridcode = 1')
        arcpy.CopyFeatures_management('fc_lyr', output + '\\' + fc)

env.workspace = output


fcs = arcpy.ListFeatureClasses()

FC_List = []
for fc in fcs:
    FC_List.append(fc)

print 'Merging layers'
arcpy.Merge_management(FC_List, output + '\\' + 'Merged_fcs')

print 'Dissolving layers'
arcpy.Dissolve_management(output + '\\' + 'Merged_fcs', output + '\\' + 'Merged_dis')
