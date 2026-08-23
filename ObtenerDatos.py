# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:52:31 2026

@author: aguir
"""

##ObtenerDatos
# Just stick some data there
# me crea el archivo en C/User/MarcelaAguirre
with open('email_addresses.txt', 'w') as f:
    f.write("joelgrus@gmail.com\n")
    f.write("joel@m.datasciencester.com\n")
    f.write("joelgrus@m.datasciencester.com\n")

from pathlib import Path

# 1. Define la ruta de la carpeta y del archivo
carpeta = Path(r'C:\Users\aguir\OneDrive\Desktop\Ciencias de Datos\obtenerDatos')
archivo = carpeta / 'email_addresses.txt'  # Esto junta la carpeta + el nombre
with open(archivo, 'w') as f:
    f.write("joelgrus@gmail.com\n")
    f.write("joel11@m.datasciencester.com\n")
    f.write("joelgrus@m.datasciencester.com\n")