# AWS_WORKSHOP - Jeronimo Duque R y Juan Pablo Alzate A
## Gestión de Archivos en Amazon S3
**a)** Creación del Bucket
<img width="1842" height="479" alt="image" src="https://github.com/user-attachments/assets/bf6096fc-d01c-460e-a087-9b15aa1de7d8" />

**b)** Operaciones usando Bash / AWS CLI
- Cargar un archivo al bucket mediante línea de comandos y verificar que el archivo fue cargado correctamente en el bucket:<br>
  **1)** Crear un archivo de prueba. <br>
  ```bash
  nano archivo_test_s3_BASH.txt
  ```
  (Este archivo se crea en la carpeta AWS_WORKSHOP)

  **2)** Cargar el archivo desde consola.<br>
  ```bash
  aws s3 cp archivo_test_s3_BASH.txt s3://user-992245-ueia-so/
  ```

  **3)** Verificar que se cargo correctamente.
  <img width="1660" height="345" alt="image" src="https://github.com/user-attachments/assets/8c3966be-f6fa-4b5e-a215-a0077b672fcd" />

  


