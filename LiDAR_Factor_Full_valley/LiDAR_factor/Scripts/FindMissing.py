import os

input_1 = r'E:\LiDAR_factor\OutputTextureStats\tif_outputs'

input_2 = r'E:\LiDAR_factor\segmentedImagery\stacked'

outFile = open(r"E:\LiDAR_factor\FirstDirectory.csv", "w")

outFile2 = open(r"E:\LiDAR_factor\SecondDirectory.csv", "w")
                

FileList = []
for root, dirs, files in os.walk(input_1):
    for filename in files:
        if filename[-4:] == ".tif":
            outFile.write(filename[:6] + '\n')
outFile.close()


#print FileList

FileList2 = []
for root, dirs, files in os.walk(input_2):
    for filename in files:
        if filename[-4:] == ".tif":
            outFile2.write(filename[:6] +'\n')
outFile2.close()
        
            
            
