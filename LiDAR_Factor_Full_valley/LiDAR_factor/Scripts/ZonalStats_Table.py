import arcpy, os
from arcpy import env

env.workspace = r'E:\LiDAR_factor\segmentedImagery\stacked'
env.overwriteOutput = True

arcpy.CheckOutExtension("Spatial")

rasters = arcpy.ListRasters()
table = r'H:\2017_3_inch_samples\proprietary_stack\Comprehensive_Samples\LiDARFactor_tiles_Final2.shp'
arcpy.MakeFeatureLayer_management(table, "lyr")

output = r'E:\LiDAR_factor\ZoneStats_tables'

for raster in rasters:
    
    BookSec_query = ' "BOOKSECT" = \'' +raster[1:6]+'\''
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", BookSec_query)
    arcpy.gp.ZonalStatisticsAsTable_sa(table, "BOOKSECT", raster, output + '\\' + raster[:-4] + '.dbf', 'DATA', 'ALL')

print "finished running zonal stats on all zones"
MergeList = []
for root, dirs, files in os.walk(output):
    for filename in files:
        if filename[-4:] == '.dbf':
            MergeList.append(root + '\\' + filename)

print "merging final tables together"
arcpy.Merge_management(MergeList, output + '\\FinalZonalStats.dbf') 


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "LiDARFactor_tiles_Final2"
#arcpy.gp.ZonalStatisticsAsTable_sa("LiDARFactor_tiles_Final2", "BOOKSECT", "E:/LiDAR_factor/segmentedImagery/stacked/o17917_stack_1.tif", "E:/LiDAR_factor/test/test2", "DATA", "ALL")
