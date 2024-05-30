#@title FIND SHAREABLE LINKS FROM FOLDER LIST IN COLAB

from subprocess import getoutput
import os
from google.colab import drive

# Instalar xattr desde la terminal de Colab
!apt-get install xattr > /dev/null

drive.mount('/content/drive', force_remount=True)

carpetas_objetivo = ['01) Carpeta', '02) Carpeta', '03) Carpeta']
carpeta_compartida = '/content/drive/Shareddrives/Carpeta/Subcarpeta/'

def get_shareable_link(file_path):
  fid = getoutput("xattr -p 'user.drive.id' " + "'" + file_path + "'")
  return [f'https://docs.google.com/spreadsheets/d/{fid}/edit#gid=0',]

for i, carpeta in enumerate(carpetas_objetivo):
    try:
        ruta_carpeta = os.path.join(carpeta_compartida, carpeta)
        archivos = os.listdir(ruta_carpeta)
        for archivo in archivos:
            if 'Mayo' in archivo:
              archivo_ruta = os.path.join(ruta_carpeta, archivo)
              link = get_shareable_link(archivo_ruta)
              print(f'{link} #{carpeta}')
    except FileNotFoundError:
        print(f'No se encontro {carpeta}')