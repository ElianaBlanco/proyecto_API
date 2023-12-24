import requests

def descargar_datos_como_csv(url: str, nombre_archivo: str):
    # Realizar el GET request para obtener los datos
    respuesta = requests.get(url)
    
    # Verificar si la descarga fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Guardar la respuesta en un archivo CSV
        with open(nombre_archivo, 'w') as archivo_csv:
            archivo_csv.write(respuesta.text)
            print(f"Los datos han sido descargados y guardados en '{nombre_archivo}'")
    else:
        print("Error al descargar los datos")

# Ejemplo de uso de la función para descargar los datos desde la URL
url_datos = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'  # Reemplaza 'https://ruta/datos.csv' con la URL real
nombre_archivo_csv = 'datos_descargados.csv'  # Nombre del archivo donde se guardarán los datos

descargar_datos_como_csv(url_datos, nombre_archivo_csv)
