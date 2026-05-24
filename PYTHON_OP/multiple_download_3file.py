import boto3
import os

# Cliente S3
s3 = boto3.client("s3")

# Configuración
bucket_name = "user-992245-ueia-so"

# carpeta en s3 donde esta los archivos
s3_folder = "AWS_upload_3_py/"

# Carpeta local en donde se descargan 
download_folder = "/home/duquejr/AWS_WORKSHOP/AWS_download_3_py"


# 1. Listar archivos en S3
response = s3.list_objects_v2(
    Bucket=bucket_name,
    Prefix=s3_folder
)

# Validar que existan archivos
if "Contents" not in response:
    print("No se encontraron archivos en S3.")
    exit()

# 2. Descargar archivos
for obj in response["Contents"]:
    s3_key = obj["Key"]

    # Evitar descargar la “carpeta” como objeto
    if s3_key.endswith("/"):
        continue

    file_name = s3_key.split("/")[-1]
    download_path = os.path.join(download_folder, file_name)

    s3.download_file(bucket_name, s3_key, download_path)

    print(f"Descargado: {file_name}")

print(f"Archivos guardados en: {download_folder}")