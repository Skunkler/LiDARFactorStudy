pro test_segments

COMPILE_OPT idl2

e=envi(/headless)

file=filepath('o12515_stacked.tif', root='E:\', subdirectory=['LiDAR_factor', 'OutputTextureStats', 'tif_outputs'])

raster = e.openraster(file)

output= 'E:\LiDAR_factor\outputsegExtractionTest2\'




Task = ENVITask('FXSegmentation')
Task.INPUT_RASTER = raster
Task.SEGMENT_BANDS = [0,1,2,3,4,5,6,7]
Task.SEGMENT_ALGORITHM = Edge
Task.KERNEL_SIZE = 7
Task.SEGMENT_VALUE = 45
Task.MERGE_VALUE = 50
Task.OUTPUT_RASTER_URI = output + file_basename(file, '.tif') + '_segmentNeedsProj9.dat'
Task.execute

;file2 = output + file_basename(file, '.tif') + '_segmentNeedsProj.dat'
;raster2 = e.openraster(file2, SPATIALREF_OVERRIDE = raster.spatialref)
;raster2.export, output + file_basename(file, '.tif') + 'segment9.tif', 'TIFF'
;raster2.close
raster.close



e.close




END