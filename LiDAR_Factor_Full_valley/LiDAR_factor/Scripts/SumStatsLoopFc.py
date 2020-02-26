# Created by Judy Brandt in support of the Las Vegas Valley 4-band imagery vegetation analysis project 2010
# This script loops through feature classes in a single workspace. It summarizes the data from a veg dataset
# And puts it in a table.  It then takes that table appends it to another table which becomes a compilation of the
# statistics of all of the datasets in the workspace.

# Import system modules
import sys, string, os, arcpy, time, datetime
from arcpy import env 


# Create the Geoprocessor object, workspace and logpath variables, set env to allow overwriting of the output
ws = raw_input(" Enter the workspace path: ")
#logpath = "E:\2016_ClarkCounty_imageryclassification\logs"
env.workspace = ws
arcpy.env.overwriteOutput = True

#  temp workspace variable ===================
tempsp = r"D:\LiDAR_factor\tempStats.gdb"

#------PUT IN NAME OF LOGFILE!!!!!!  ********************************************************
"""scriptName = sys.argv[0]
logName = sys.argv[0].split("\\")[len(sys.argv[0].split("\\")) - 1][0:-3]
logfile = logpath + "\\" + logName + ".log"
outfile = open(logfile ,'w')

#------OPEN LOG FILE AND PUT IN NAME OF PYTHON SCRIPT!!!!!!********************************************************
outfile.write('\n' + "WORKSPACE: " + ws  + '\n' + scriptName + "----------------------------------------" '\n')
outfile.close()"""


#Loop through the list of feature classes
fcs = arcpy.ListFeatureClasses("", "")


for fc in fcs:

    #  important name variables ======================    
    
    #BookSec = fc[6:]
    BookSec = fc[6:11]
        
    # create a tuple of local time data
    timeYearMonDay = datetime.date.today()
    timeHour = time.localtime()[3]
    timeMin = time.localtime()[4]
    
    #Record the fc and the time processing starts in the log file
    #outfile = open(logfile,'a') 
    print fc
    #outfile.write(fc +  " " + str(timeYearMonDay) +  " " + str(timeHour) + ":" + str(timeMin) +  '\n')

    #  temp dataset variables ===================

    Sumstats = tempsp + "\\sum_section"
    
    # output dataset variable - final output table =======================
    
    SumTable = ws + "\\sum_section"    

#----------------------------------------------------------------------------------------------------------------------------
        #GEOPROCESSING CODE GOES BELOW HERE
#----------------------------------------------------------------------------------------------------------------------------    
    try:
        #if the final output table does not exist...
        if not arcpy.Exists(SumTable):
            print fc
                        # Process: Summary Statistics...into a new table
            print "Summary Statistics..."
            arcpy.Statistics_analysis(fc, SumTable, "Shape_Area SUM", "")


            # Add field
            print  "add a field to the temp table"
            arcpy.AddField_management(SumTable,  "BOOKSEC", "TEXT")

            # Calculate the new field in the new table  - populate it with the tile name the "BOOKSEC" field value
            print  "Calculate the new field in the temp table"
            arcpy.CalculateField_management(SumTable, "BOOKSEC", '"' + BookSec + '"',"PYTHON_9.3", "")
            #arcpy.CalculateField_management(fc_diss_layer,"FRONT_YD", "!Shape_Area!", "PYTHON_9.3", "")

        #if the final output table does exist...
        elif arcpy.Exists(SumTable):

                        # Process: Summary Statistics...into a new temp table
            print "Summary Statistics..."
            arcpy.Statistics_analysis(fc, Sumstats, "Shape_Area SUM", "")


            # Add field to the new temp table
            print  "add a field"
            arcpy.AddField_management(Sumstats,  "BOOKSEC", "TEXT")

            # Calculate the new field in the new temp table  - populate it with the tile name the "BOOKSEC" field value
            print  "Calculate the field"
            arcpy.CalculateField_management(Sumstats, "BOOKSEC", '"' + BookSec + '"',"PYTHON_9.3", "")

            # Append final sum table with the data from the temp table
            print "Append sum table..."
            arcpy.Append_management(Sumstats, SumTable, "NO_TEST")              

    except:
        print "Process: Failed for: " + fc
        print arcpy.GetMessages(2)
        ouch = arcpy.GetMessages(2)
        #outfile.write(ouch + '\n' )        
        #outfile.write("Process: Failed for: " + fc + "  " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n' )          

#----------------------------------------------------------------------------------------------------------------------------    
#----------------------------------------------------------------------------------------------------------------------------    

    #outfile.close()

# create a tuple of local time data
"""timeYearMonDay = datetime.date.today()
timeHour = time.localtime()[3]
timeMin = time.localtime()[4]


print "Process done! " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin)
outfile= open(logfile,'a')
outfile.write("Process Complete "  + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n' )
outfile.close()"""
