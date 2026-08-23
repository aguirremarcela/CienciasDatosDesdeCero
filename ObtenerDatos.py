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
 #tipo de dato str (texto)   
def get_domain(email_address: str) -> str:
    """Split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]

print(get_domain("joel@m.datasciencester.com"))#me da el dominio m.datasciencester.com

#me cuenta la cantidad de dominio que hay de cada tipo 
from collections import Counter

with open(archivo, 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)
print(dict(domain_counts)) #{'gmail.com': 1, 'm.datasciencester.com': 2}
#Metodo
def process(date: str, symbol: str, closing_price: float) -> None:
    # Imaginge that this function actually does something.
    assert closing_price > 0.0

#Archivos delimitados
#Es comun que un archivo tengo mucho mas dato por linea
#Suelen esta separados por comas o tabuladores
#Para esto es necesario analizarlo con el modulo csv de Python.
carpeta = Path(r'C:\Users\aguir\OneDrive\Desktop\Ciencias de Datos\obtenerDatos')
archivo = carpeta / 'tab_delimited_stock_prices.txt'


with open(archivo, 'w') as f:
    f.write("""6/20/2014\tAAPL\t90.91
6/20/2014\tMSFT\t41.68
6/20/2014\tFB\t64.5
6/19/2014\tAAPL\t91.86
6/19/2014\tMSFT\t41.51
6/19/2014\tFB\t64.34
""")



import csv
with open(archivo) as f:
    tab_reader = csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date,symbol,closing_price)
 
archivo1 = carpeta / 'colon_delimited_stock_prices.txt'
with open(archivo1, 'w') as f:
    f.write("""date:symbol:closing_price
6/20/2014:AAPL:90.91
6/20/2014:MSFT:41.68
6/20/2014:FB:64.5
""")


#HTML
#Aca tuve que cambiar el interprete porque no me tomaba el html 

from bs4 import BeautifulSoup
import requests
# Pongo el archivo HTML en GitHub. Para encajar
# la URL en el libro tuve que dividirla en dos líneas.
# Recuerde que las cadenas de texto whitespace-separated se concatenan.
url = ("https://raw.githubusercontent.com/"
"joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

#el texto de la primer etiqueta 
first_paragraph = soup.find('p') 
print(first_paragraph)
#todos los text con la eiqueta p
all_paragraphs = soup.find_all('p')

#O aquel que p tenga un id 
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]
# Tambien se puede  buscar  aquella etiqueta que tenga una determinada class
important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]
important_div = soup('div', {'class' : 'signature'})

print(important_paragraphs)
print(important_paragraphs2)
print(important_div)


##si queremos encontrar todos los
#elementos <span> contenidos dentro de un elemento <div>, podríamos hacer
#lo siguiente:
    
spans_inside_divs = [span
                     for div in soup('div')     # for each <div> on the page
                     for span in div('span')]   # find each <span> inside it



url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")
all_urls = [a['href']
for a in soup('a')
if a.has_attr('href')]
print(len(all_urls))