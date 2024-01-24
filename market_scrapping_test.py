import requests
from bs4 import BeautifulSoup
import re

url = "https://mercadomadrid.com.co/?sede=1"

try:
    response = requests.get(url)
    response.raise_for_status()  # Lanzar una excepción si hay un error HTTP

    soup = BeautifulSoup(response.content, "html.parser")

    categories = {}

    # Expresión regular para los elementos de las categoría
    regex = re.compile(r"lname-cat-\d+")

    # Todos los elementos que cumplen la expresión regular
    nombres_categorias = soup.find_all("span", class_=regex)

    menu_items = soup.find_all("div", class_="item-lmenu item-ltext")

    for item in menu_items:
        link = item.find("a")["href"]
        text = item.find("span").text
        # Every element of the dict has the category name as a key and the link as the value
        categories[text] = link

except requests.exceptions.RequestException as e:
    print(f"Error al obtener el contenido de la URL '{url}': {e}")
    # Puedes agregar aquí el manejo de errores específicos según tus necesidades
except Exception as e:
    print(f"Error inesperado: {e}")
    # Puedes agregar aquí el manejo de errores específicos según tus necesidades
else:
    # El código en este bloque else se ejecutará si no hay excepciones
    print("Operación exitosa. Puedes continuar con el procesamiento de 'categories'.")




# Lista para almacenar los documentos HTML
lista_html = []

# Iterar a través de los enlaces del diccionario
for name, link in categories.items():
    try:
        # Hacer la solicitud HTTP al enlace
        response = requests.get(link)
        response.raise_for_status()  # Lanzar una excepción si hay un error HTTP

        # Obtener el contenido HTML
        html = response.content

        # Agregar el HTML a la lista
        lista_html.append(html)

        print(f"Documento HTML para '{name}' ha sido guardado.")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el documento HTML para '{name}': {e}")

# Ahora, la lista_html contiene el HTML de cada enlace en tu diccionario
# Puedes procesar estos documentos HTML según tus necesidades.



# for category in categories:
#     print(category.text)

# for product in soup.find_all("div", class_="product"):
#     name = product.find("h2").text
#     price = product.find("span", class_="price").text
#     print(f"Nombre del producto: {name}")
#     print(f"Precio del producto: {price}")
