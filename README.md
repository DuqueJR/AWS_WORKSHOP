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

  Por consola: <br>
  ```bash
  aws s3 ls s3://user-992245-ueia-so/
  ```

  (Retorno: 2026-05-23 21:08:55         95 archivo_test_s3_BASH.txt)

<br><br>
- Descargar el archivo en la máquina local en una carpeta diferente a la ubicación original y verificar que el archivo fue descargado correctamente:<br>
  **1)** Moverse a la carpeta donde se quiere descargar para facilitar la descarga.<br>
  ```bash
   cd AWS_downloads/
  ```

   **2)** Copiar el archivo desde el bucket a la carpeta actual. 
  ```bash
   aws s3 cp s3://user-992245-ueia-so/archivo_test_s3_BASH.txt .
  ```
   **3)** Verificar que se haya copiado correctamente. 

  ```bash
   ls
  ```
  (Retorno: archivo_test_s3_BASH.txt)

<br><br>

-  Explicar qué cambia en el proceso de carga y descarga cuando se manejan múltiples archivos: <br><br>
  Cuando se manejan múltiples archivos, el proceso de carga y descarga requiere automatización mediante ciclos for desde bash o comandos como sync que permite sincronizar una carpeta en la maquina local con un direccion del bucket, ya que realizar las operaciones manualmente archivo por archivo se vuelve ineficiente. Además, se hace necesaria una mejor organización, verificación masiva y optimización de transferencias para administrar correctamente todos los archivos.

<br><br>
- Presentar un ejemplo práctico de carga y descarga de múltiples archivos:
  **1)** Crear una carpeta con multiples archivos.
  ```bash
  mkdir multple_upload
  cd multple_upload/
  for i in {1..10}; do touch test_mupload_$i; done
  ```

  **2)** Crear y ejecutar un scrip que con el metodo sync permita subir los archivos de la maquina local al bucket.<br>
  (Este archivo esta en el repo en la carpeta BASH_OP)<br>

  **3)** Ejecutar el script y observar el resultado con los archivos cargados. 
  (Retorno: )
  <img width="1054" height="539" alt="image" src="https://github.com/user-attachments/assets/d4cfd953-d73e-44a5-9310-04616ce02ed8" />

  **4)** Verificar la carga en el bucket.
  <img width="1653" height="726" alt="image" src="https://github.com/user-attachments/assets/75b7db12-12ff-4f4c-beeb-4bb3ee3bb4b6" />


  (Los archivos son todos txt vacios)<br>

  **Para descargar**<br>
  **1)** Crear scrip que con el metodo sync permita subir los archivos de la maquina local al bucket.<br>
  (Este archivo esta en el repo en la carpeta BASH_OP)<br>

   **2)** Ejecutar el script
  <img width="1098" height="286" alt="image" src="https://github.com/user-attachments/assets/d72ffbb1-bf94-44b7-9e7a-d1bf9b211850" />


  **3)** Verificar la carga en la carpeta local.
  
  <img width="813" height="78" alt="image" src="https://github.com/user-attachments/assets/74615230-d261-4539-9ce8-55862c365426" />


<br><br> 

**c)** Operaciones usando boto3 (Python)
- Cargar un archivo al bucket utilizando boto3 y Verificar que el archivo fue cargado correctamente.<br>
  **1)** Crear un scrip de python que permita subir el archivo al bucket.<br>
  (El archivo esta en el repositorio en la carpeta  PYTHON_OP)

  **2)** Ejecutar el script.<br>
  (El archivo que se va a cargar esta en la ruta /home/duquejr/AWS_WORKSHOP/archivo_test_s3_PYTHON.txt)
  <img width="523" height="37" alt="image" src="https://github.com/user-attachments/assets/664c8377-fdbc-484c-954a-74c9f23c8bbd" />

  **3)**Verificar la carga en el bucket.
  <img width="1659" height="432" alt="image" src="https://github.com/user-attachments/assets/dc634083-0993-46d7-8d1b-1d52fe2043c7" />

<br><br>
- Descargar el archivo en la máquina local en una carpeta diferente a la ubicación original y verificar que el archivo fue descargado correctamente:<br>
 **1)** Crear un scrip de python que permita descargar el archivo en la maquina local.<br>
  (El archivo esta en el repositorio en la carpeta  PYTHON_OP)

  **2)** Ejecutar el script.<br>
  <img width="604" height="62" alt="image" src="https://github.com/user-attachments/assets/4ac32342-6d74-40bb-ba1e-164e22d5895d" /><br>
  (Se descarga en la carpeta de este mismo repositorio python_download)<br>

  

  **3)** Verificar la carga en la carpeta local.<br>
  <img width="483" height="66" alt="image" src="https://github.com/user-attachments/assets/373a50a5-a726-468e-847f-f9c8abc85882" />

<br><br>
  -  Explicar qué cambia en el proceso de carga y descarga cuando se manejan múltiples archivos: <br><br>
  Cuando se trabaja con múltiples archivos en Python usando boto3 en Amazon Web Services S3, el proceso de carga y descarga requiere automatización mediante estructuras como ciclos for, ya que realizar las operaciones archivo por archivo se vuelve ineficiente, además de que se deben construir rutas dinámicas (keys) para organizar los archivos dentro del bucket, y se vuelve necesario realizar verificaciones masivas en lugar de comprobaciones individuales, lo que implica mayor control sobre el flujo de datos, manejo de colecciones de archivos y optimización del proceso de transferencia en general.

<br><br>
- Realizar una prueba cargando y descargando tres archivos de texto.:<br>
 **1)** Crear un scrip de python que permita cargar los tres archivos de la maquina local al bucket.<br>
  (El archivo esta en el repositorio en la carpeta  PYTHON_OP)

  **2)** Ejecutar el script.<br>
  <img width="585" height="80" alt="image" src="https://github.com/user-attachments/assets/d6d1417d-548c-4765-89a4-35da9cae2401" />

  (Se toman de la carpeta de este mismo repositorio python_upload_3_file)<br>

  

  **3)** Verificar la carga en el bucket.<br>
<img width="1775" height="553" alt="image" src="https://github.com/user-attachments/assets/e47855c9-e266-40b9-ad99-5780baca3e53" />


<br>

 **Para descargar** <br>
 **1)** Crear un scrip de python que permita descargar los tres archivos del bucket a la carpeta local.<br>
  (El archivo esta en el repositorio en la carpeta  PYTHON_OP)

  **2)** Ejecutar el script.<br>
  <img width="599" height="98" alt="image" src="https://github.com/user-attachments/assets/a174f7fe-059a-4ac6-a856-e4646d328d4d" />


  (Se descargan la carpeta de este mismo repositorio python_download_3_file)<br>

  

  **3)** Verificar en la carpeta local.<br>
  <img width="602" height="53" alt="image" src="https://github.com/user-attachments/assets/a13000ce-3bda-41e0-bf99-ab21b296aee2" />





  
