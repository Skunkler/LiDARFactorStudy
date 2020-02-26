import os, string, shutil, time, sys

file1 = open(r"E:\LiDAR_factor\modelFinal\FinalTraining2.csv", "a")

file2 = open(r"E:\LiDAR_factor\modelFinal\12427.csv", "r")

file3 = open(r"E:\LiDAR_factor\modelFinal\12433.csv", "r")
file4 = open(r"E:\LiDAR_factor\modelFinal\12434.csv", "r")
file5 = open(r"E:\LiDAR_factor\modelFinal\12510.csv", "r")

file6 = open(r"E:\LiDAR_factor\modelFinal\12515.csv", "r")

file7 = open(r"E:\LiDAR_factor\modelFinal\13836.csv", "r")

file8 = open(r"E:\LiDAR_factor\modelFinal\16224.csv", "r")
file9 = open(r"E:\LiDAR_factor\modelFinal\16226.csv", "r")

file1.write(",ID,b1,b2,b3,b4,b5,b6,b7,b8,desc\n")

lines9 = file9.readlines()
lines8 = file8.readlines()
lines7 = file7.readlines()
lines6 = file6.readlines()
lines5 = file5.readlines()
lines4 = file4.readlines()

lines3 = file3.readlines()

lines2 = file2.readlines()

count = 0
for line in lines2:
    if line.split(',')[0] != '':
        count = line.split(',')[0]
        ID = line.split(',')[1]
        b1 = line.split(',')[2]
        b2 = line.split(',')[3]
        b3 = line.split(',')[4]
        b4 = line.split(',')[5]
        b5 = line.split(',')[6]
        b6 = line.split(',')[7]
        b7 = line.split(',')[8]
        b8 = line.split(',')[9]
        desc = line.split(',')[10][:-1]

        outputLine = count +','+ID+','+b1+','+b2+','+b3+','+b4+','+b5+','+b6+','+b7+','+b8+','+desc+'\n'
        file1.write(outputLine)      
finalCount = int(count.replace('"', ''))
print finalCount

for line2 in lines3:
    if line2.split(',')[0] != '':
        finalCount += 1
        count = str(finalCount)
        ID = line.split(',')[1]
        b1 = line.split(',')[2]
        b2 = line.split(',')[3]
        b3 = line.split(',')[4]
        b4 = line.split(',')[5]
        b5 = line.split(',')[6]
        b6 = line.split(',')[7]
        b7 = line.split(',')[8]
        b8 = line.split(',')[9]
        desc = line.split(',')[10][:-1]

        outputLine = count +','+ID+','+b1+','+b2+','+b3+','+b4+','+b5+','+b6+','+b7+','+b8+','+desc+'\n'
        file1.write(outputLine)

finalCount = int(count.replace('"', ''))
print finalCount

for line2 in lines4:
    if line.split(',')[0] != '':
        finalCount += 1
        count = str(finalCount)
        ID = line.split(',')[1]
        b1 = line.split(',')[2]
        b2 = line.split(',')[3]
        b3 = line.split(',')[4]
        b4 = line.split(',')[5]
        b5 = line.split(',')[6]
        b6 = line.split(',')[7]
        b7 = line.split(',')[8]
        b8 = line.split(',')[9]
        desc = line.split(',')[10][:-1]

        outputLine = count +','+ID+','+b1+','+b2+','+b3+','+b4+','+b5+','+b6+','+b7+','+b8+','+desc+'\n'
        file1.write(outputLine)

finalCount = int(count.replace('"', ''))
print finalCount

for line2 in lines5:
    if line.split(',')[0] != '':
        finalCount += 1
        count = str(finalCount)
        ID = line.split(',')[1]
        b1 = line.split(',')[2]
        b2 = line.split(',')[3]
        b3 = line.split(',')[4]
        b4 = line.split(',')[5]
        b5 = line.split(',')[6]
        b6 = line.split(',')[7]
        b7 = line.split(',')[8]
        b8 = line.split(',')[9]
        desc = line.split(',')[10][:-1]

        outputLine = count +','+ID+','+b1+','+b2+','+b3+','+b4+','+b5+','+b6+','+b7+','+b8+','+desc+'\n'
        file1.write(outputLine)

finalCount = int(count.replace('"', ''))
print finalCount

for line2 in lines6:
    if line.split(',')[0] != '':
        finalCount += 1
        count = str(finalCount)
        ID = line.split(',')[1]
        b1 = line.split(',')[2]
        b2 = line.split(',')[3]
        b3 = line.split(',')[4]
        b4 = line.split(',')[5]
        b5 = line.split(',')[6]
        b6 = line.split(',')[7]
        b7 = line.split(',')[8]
        b8 = line.split(',')[9]
        desc = line.split(',')[10][:-1]

        outputLine = count +','+ID+','+b1+','+b2+','+b3+','+b4+','+b5+','+b6+','+b7+','+b8+','+desc+'\n'
        file1.write(outputLine)

finalCount = int(count.replace('"', ''))
print finalCount

for line2 in lines7:
    if line.split(',')[0] != '':
        finalCount += 1
        count = str(finalCount)
        ID = line.split(',')[1]
        b1 = line.split(',')[2]
        b2 = line.split(',')[3]
        b3 = line.split(',')[4]
        b4 = line.split(',')[5]
        b5 = line.split(',')[6]
        b6 = line.split(',')[7]
        b7 = line.split(',')[8]
        b8 = line.split(',')[9]
        desc = line.split(',')[10][:-1]

        outputLine = count +','+ID+','+b1+','+b2+','+b3+','+b4+','+b5+','+b6+','+b7+','+b8+','+desc+'\n'
        file1.write(outputLine)

finalCount = int(count.replace('"', ''))
print finalCount

for line2 in lines8:
    if line.split(',')[0] != '':
        finalCount += 1
        count = str(finalCount)
        ID = line.split(',')[1]
        b1 = line.split(',')[2]
        b2 = line.split(',')[3]
        b3 = line.split(',')[4]
        b4 = line.split(',')[5]
        b5 = line.split(',')[6]
        b6 = line.split(',')[7]
        b7 = line.split(',')[8]
        b8 = line.split(',')[9]
        desc = line.split(',')[10][:-1]

        outputLine = count +','+ID+','+b1+','+b2+','+b3+','+b4+','+b5+','+b6+','+b7+','+b8+','+desc+'\n'
        file1.write(outputLine)

finalCount = int(count.replace('"', ''))
print finalCount

for line2 in lines9:
    if line.split(',')[0] != '':
        finalCount += 1
        count = str(finalCount)
        ID = line.split(',')[1]
        b1 = line.split(',')[2]
        b2 = line.split(',')[3]
        b3 = line.split(',')[4]
        b4 = line.split(',')[5]
        b5 = line.split(',')[6]
        b6 = line.split(',')[7]
        b7 = line.split(',')[8]
        b8 = line.split(',')[9]
        desc = line.split(',')[10][:-1]

        outputLine = count +','+ID+','+b1+','+b2+','+b3+','+b4+','+b5+','+b6+','+b7+','+b8+','+desc+'\n'
        file1.write(outputLine)

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
