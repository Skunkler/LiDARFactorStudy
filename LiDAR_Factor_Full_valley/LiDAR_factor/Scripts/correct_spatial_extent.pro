PRO correct_spatial_extent

COMPILE_OPT idl2
e=envi(/headless)

files = file_search('E:\LiDAR_factor\principalComponents\PCAs', '*.img')
files2 = file_search('E:\LiDAR_factor\Segments_temp', '*.dat')

output = 'E:\LiDAR_factor\segmented_Final'


foreach file, files do begin
  foreach file2, files2 do begin
    file_input1 = file_basename(file, '_stacked.img') 
    file_input2 = file_basename(file2, '_stacked_segmentNeedsProj.dat')
    if(file_input1 eq file_input2) then begin 
      
    print, file_input1 + ' ' + file_input2 
    raster1 = e.openraster(file)
    raster2 = e.openraster(file2, SPATIALREF_OVERRIDE = raster1.spatialref)
    
    raster2.export, output + '\\' + file_input2 + '_SegmentRaster.tif', 'TIFF'
    
    raster1.close
    raster2.close
    endif
  
  endforeach
endforeach









e.close



END