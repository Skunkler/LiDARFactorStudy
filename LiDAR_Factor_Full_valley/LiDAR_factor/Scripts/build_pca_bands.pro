PRO BUILD_PCA_BANDS

COMPILE_OPT idl2
e=envi(/headless)

files = FILE_SEARCH('E:\LiDAR_factor\OutputTextureStats\tif_outputs', '*.tif')

outdir = 'E:\LiDAR_factor\principalComponents\PCA_bands'


foreach file, files do begin
  print, "calculating pca for file " + file_basename(file, '*.tif')
  raster = e.openraster(file)
  
  subset = ENVISubsetRaster(raster, BANDS=[4,5,6])
  
  task = ENVITask('ForwardPCATransform')
  
  task.INPUT_RASTER = subset
  task.OUTPUT_RASTER_URI = outdir + '\\' + file_basename(file, '*.tif') + '_pcaText.dat'
  task.execute
  
  print, "completed calculating PCA for Texture metrics"
  
endforeach












e.close



END
