pro automateSegs
compile_opt IDL2
e = envi(/headless)

input = "D:\colorBalance_Tests\test_stack"
files = file_search(input, '*.tif')
 foreach file, files do begin
  print, file
  raster = e.openraster(file)
  output= 'D:\colorBalance_Tests\raseter_segs\'
  
  Task = ENVITask('FXSegmentation')
  Task.INPUT_RASTER = raster
  Task.SEGMENT_BANDS = [0,1,2,3,4,5,6,7]
  Task.SEGMENT_ALGORITHM = Edge
  Task.KERNEL_SIZE = 7
  Task.SEGMENT_VALUE = 45
  Task.MERGE_VALUE = 50
  Task.OUTPUT_RASTER_URI = output + file_basename(file, '.tif') + '_segment.dat'
  Task.execute
  
  
  
  
  
 endforeach


END