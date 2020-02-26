import os, shutil, sys, string

outfile = open(r"E:\LiDAR_factor\SQLFiles.csv","w")

for root, dirs, files in os.walk(r"E:\LiDAR_factor\Classified_final"):
    for filename in files:
        if filename[-4:] == ".tif":
            stringVal = '"{fileBook}"'.format(fileBook = filename[1:6])
            outfile.write(stringVal + '\n')
