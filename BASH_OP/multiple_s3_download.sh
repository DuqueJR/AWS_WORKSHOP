#!/bin/bash

# Descargar archivos desde S3


#Carpeta local en donde se van a descargar 
DOWNLOAD_F="/home/duquejr/AWS_WORKSHOP/multiple_download"
# Bucket
BUCKET_NAME="user-992245-ueia-so"
# Carpeta de descarga en el bucket
FOLDER_B="multiple_download"

echo ""
echo "Descargando archivos desde S3..."

aws s3 sync "s3://$BUCKET_NAME/$FOLDER_B/" "$DOWNLOAD_F"

# Verificar si la descarga fue exitosa
if [ $? -eq 0 ]; then
    echo "Descarga completada correctamente."
else
    echo "ERROR durante la descarga."
    exit 1
fi


