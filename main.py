from fastapi import FastAPI, Query
from pydantic import BaseModel
import Categorias


app = FastAPI()


# connection = pymysql.connect(
#   host='localhost', user='root', password='',
#   database='integracionapi', charset='utf8mb4',
#   cursorclass=pymysql.cursors.DictCursor
# )


# Categorias


@app.get("/categorias/")
def traer_categorias():
  return Categorias.traer_categorias()


# Productos


@app.get("/productos/")
async def traer_productos():
  # codigo para leer de DB y crear objeto para mostrar
  return "productos"


# Proveedores


@app.get("/proveedores/")
async def traer_proveedores():
  # codigo para leer de DB y crear objeto para mostrar
  return "proveedores"


# Compras


@app.get("/compras/")
async def traer_compras():
  # codigo para leer de DB y crear objeto para mostrar
  return "compras"


# Facturas


@app.get("/facturas/")
async def traer_facturas():
  # codigo para leer de DB y crear objeto para mostrar
  return "facturas"


