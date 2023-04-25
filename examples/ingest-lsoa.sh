#!/bin/sh
# Create an index for b6 from a shapefile containing LSOA polygons
b6-ingest-gdal \
  --input=Lower_Layer_Super_Output_Areas__December_2011__Boundaries_Full_Clipped__BFC__EW_V3.shp \
  --id=LSOA11CD \
  --id-strategy=gb-ons-2011 \
  --copy-tags=name=LSOA11NM \
  "--add-tags=#boundary=lsoa" \
  --output=lsoa.index
