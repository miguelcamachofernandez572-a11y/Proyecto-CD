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
                if producto["nombre"] == producto_buscado and producto["disponible"]== True:
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
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
grafico_precio_promedio_vs_pension_minima(diccionario)

def grafico_servicio_domicilio():
    disponible=0
    nodisponible=0
    for archivo in archivos:
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            if "servicio_a_domicilio" in data:
                            if data["servicio_a_domicilio"]["valor"]==True:
                                disponible += 1
                            else:
                                nodisponible += 1
    plt.pie(
    [disponible, nodisponible],
    labels=["Disponible", "No disponible"],
    autopct='%1.1f%%',
    colors=["#6a4d57", "#9c9386"]
    )
    plt.title("Disponibilidad del servicio a domicilio", fontsize=15, fontweight='bold')
    plt.axis('equal')
    plt.show()
grafico_servicio_domicilio()

def grafico_precios_marca_producto(producto_buscado="pollo"):
    lista=[]
    for archivo in archivos:
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:
                if producto["nombre"].lower().strip() == producto_buscado.lower().strip() and producto["disponible"]== True:
                    precio=producto["precio"]
                    unidad_de_medida=str(producto["unidad de medida"])
                    marca=str(producto["marca"])
                    lista.append({"marca": marca, "precio": precio, "unidad_de_medida": unidad_de_medida})
    lista=sorted(lista,key=lambda x: x["precio"])
    marcas=[]
    precios=[]
    unidades=[]
    for p in lista :   
        marcas.append(p["marca"])
        precios.append(p["precio"])
        unidades.append(p["unidad_de_medida"])
    barras=plt.bar(marcas,precios,color="#9c9386")
    plt.bar_label(barras,unidades,label_type="edge")
    plt.title("Precios de " + producto_buscado + " ordenados")
    plt.xlabel("Marca")
    plt.ylabel("Precio")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()

grafico_precios_marca_producto(producto_buscado="pollo")
                        