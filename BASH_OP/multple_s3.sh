#!/bin/bash

# Bucket
BUCKET_NAME="user-992245-ueia-so"

# Carpeta local que contiene los archivos
LOCAL_FOLDER="/home/duquejr/AWS_WORKSHOP/multple_upload"

# Carpeta de descarga en el bucket
FOLDER_B="multiple_download"


echo "INICIO DEL PROCESO"


# Verificar que exista la carpeta local


if [ ! -d "$LOCAL_FOLDER" ]; then
    echo "ERROR: La carpeta '$LOCAL_FOLDER' no existe."
    exit 1
fi


# Subir todos los archivos al bucket S3


echo ""
echo "Subiendo archivos a S3..."

aws s3 sync "$LOCAL_FOLDER" "s3://$BUCKET_NAME/$FOLDER_B/"

# Verificar si la subida fue exitosa
if [ $? -eq 0 ]; then
    echo "Carga completada correctamente."
else
    echo "ERROR durante la carga."
    exit 1
fi

# ------------------------------------------
# Mostrar archivos cargados en S3
# ------------------------------------------

echo ""
echo "Archivos almacenados en S3:"

aws s3 ls "s3://$BUCKET_NAME/$FOLDER_B/"
