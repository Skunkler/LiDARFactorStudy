import arcpy, os, sys, string
from arcpy import env

env.workspace = r'D:\2016_ClarkCounty_imageryclassification\analysis\Trees_Final.gdb'

fcs = arcpy.ListFeatureClasses()

List_trees = []
List_turf = []

BLS_File = open(r'D:\LiDAR_Factor_Full_valley\BLS_2014.bls','w')
#BLS_File_2016 = open(r'D:\LiDAR_Factor_Full_valley\BLS_2016.bls','w')

BLS_File.write('PortInput1\tPortInput2\n')
#BLS_File_2016.write('Input1\n')

image_request_list = []
for fc in fcs:
    line = 'o' + fc[6:11] + '.tif'
    image_request_list.append(line)



for root, dirs, files in os.walk(r'R:\Image_ClarkCounty\2014\ClarkCounty_Collection'):
    for filename in files:
        if filename[-4:] == '.tif':
            for x in range(0, len(image_request_list)):
                if image_request_list[x] == filename:
                    List_2014.append(root + '\\' + filename)

List_2014.sort()

for root, dirs, files in os.walk(r'R:\Image_ClarkCounty\2016\ClarkCounty_Collection'):
    for filename in files:
        if filename[-4:] == '.tif' and 'jpg' not in root:
            for i in range(0, len(image_request_list)):
                if image_request_list[i] == filename:
                    List_2016.append(root + '\\' + filename)

List_2016.sort()



for i in range(0,len(List_2014)):
    line = List_2014[i].replace('\\', '/') + '\t' + List_2016[i].replace('\\', '/') + '\n'
    BLS_File.write(line)
    #line2 = List_2016[i].replace('\\', '/')
    #BLS_File_2016.write(line2 + '\n')
BLS_File.close()
