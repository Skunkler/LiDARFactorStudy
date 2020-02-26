import arcpy, os, string, shutil, sys, time



input_dir = r'R:\Image_ClarkCounty\2016\ClarkCounty_Collection'
newfile = r'E:\LiDAR_factor\2016_Image_Samples\\'


booksectFile = r'H:\2017_3_inch_samples\proprietary_stack\Comprehensive_samples\LiDARFactor_tiles_Final2.shp'

sampleFileList = []

with arcpy.da.SearchCursor(booksectFile, 'BOOKSEC') as cursor:
    for row in cursor:
        ImageFile = ('{}').format(row[0])
        sampleFileList.append(ImageFile)

for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename[1:-4] in sampleFileList:

            aux_file = filename[:-4] + '.aux'
            tif_file = filename[:-4] + '.tif'
            tfw_file = filename[:-4] + '.tfw'
            rrd_file = filename[:-4] + '.rrd'

            print "copying " + filename + "\n"
            shutil.copy(root + '\\' + aux_file, newfile + '\\' + aux_file)
            shutil.copy(root + '\\' + tif_file, newfile + '\\' + tif_file)
            shutil.copy(root + '\\' + tfw_file, newfile + '\\' + tfw_file)
            shutil.copy(root + '\\' + rrd_file, newfile + '\\' + rrd_file)
            
            print "success copying over " + filename + "\n"
