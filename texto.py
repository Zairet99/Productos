import requests
from bs4 import BeautifulSoup
import pandas as pd
# Guardar el script completo en un archivo .py local
script_code = """import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://scrapepark.org/spanish/"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
productos = soup.find_all("div", class_="col-sm-6 col-md-4 col-lg-4")

datos = []
for producto in productos:
    nombre = producto.find("div", class_="detail-box").find("h5").text.strip()
    precio_texto = producto.find("div", class_="detail-box").find("h6").text.strip()
    precio = float(precio_texto.replace("$", ""))

    if "usada" in nombre.lower():
        condicion = "Usada"
    else:
        condicion = "Nueva"

    datos.append({
        "nombre": nombre,
        "precio_usd": precio,
        "condicion": condicion
    })

df = pd.DataFrame(datos)
df.to_csv("patinetas_scrapepark.csv", index=False)
print("Scraping exitoso y archivo patinetas_scrapepark.csv creado.")
"""

with open("scraper.py", "w", encoding="utf-8") as f:
    f.write(script_code)
