import boto3
import os

# Crear cliente S3
s3 = boto3.client("s3")

# Nombre del bucket
bucket_name = "user-992245-ueia-so"

# Nombre del archivo en S3
s3_key = "archivo_test_s3_PYTHON.txt"

# Carpeta destino
download_folder = "/home/duquejr/AWS_WORKSHOP/download_python"

# Crear carpeta si no existe
os.makedirs(download_folder, exist_ok=True)

# Ruta final donde se descargara el archivo
download_path = os.path.join(download_folder, s3_key)

# Descargar archivo
s3.download_file(bucket_name, s3_key, download_path)

print("Archivo descargado correctamente")
print(f"Ubicación: {download_path}")