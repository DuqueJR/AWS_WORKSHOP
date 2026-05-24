import boto3

# Crear cliente S3
s3 = boto3.client("s3")

# Nombre del bucket
bucket_name = "user-992245-ueia-so"

# Archivo local
local_file = "/home/duquejr/AWS_WORKSHOP/archivo_test_s3_PYTHON.txt"

#Nombre en S3
s3_key = "archivo_test_s3_PYTHON.txt"

# Subir archivo
s3.upload_file(local_file, bucket_name, s3_key)

print("Archivo subido correctamente a S3")