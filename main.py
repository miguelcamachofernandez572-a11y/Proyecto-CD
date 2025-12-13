import os
import json
import matplotlib.pyplot as plt

archivos = os.listdir("json/")



def promedio(producto_buscado):
    precios = []
    for archivo in archivos:
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:
                if producto["nombre"] == producto_buscado and producto.get("disponible", False):
                    precios.append(producto["precio"])
    
    promedio = round(sum(precios)/len(precios))
    return promedio
        
diccionario = {
    "Pan": promedio("Pan"),
    "Leche": promedio("Leche"),
    "Toallitas húmedas":promedio("Toallitas húmedas"),
    "Pañales":promedio("Pañales"),
    "yogurt":promedio("yogurt"),
    "pollo":promedio("pollo"),
    "picadillo":promedio("picadillo"),
    "huevo":promedio("huevo"),
    "queso":promedio("queso"),
    "sopas":promedio("sopas"),
    "arroz":promedio("arroz"),
    "frijoles":promedio("frijoles"),
    "aceite":promedio("aceite"),
    "cereales":promedio("cereales"),
    "galletas":promedio("galletas")
}

def grafico_precio_promedio_vs_pension_minima(diccionario):
    keys = diccionario.keys()
    values = diccionario.values()

    plt.bar(keys,values,color="#6a4d57")
    plt.axhline(y=3056,color="#9c9386",ls="--")
    plt.title("Precio promedio de productos")
    plt.annotate("Pensión Mínima: 3056",(1,3000),(0,2800),arrowprops={"arrowstyle":"->"})
    plt.show()
