import boto3
import os

# Cliente S3
s3 = boto3.client("s3")

# Configuración
bucket_name = "user-992245-ueia-so"

# RUTAS COMPLETAS
local_folder = "/home/duquejr/AWS_WORKSHOP/AWS_upload_3_py"



#SUBIR ARCHIVOS
for file_name in os.listdir(local_folder):
    local_path = os.path.join(local_folder, file_name)

    s3_key = f"AWS_upload_3_py/{file_name}"

    s3.upload_file(local_path, bucket_name, s3_key)
    print(f"Subido: {file_name}")

