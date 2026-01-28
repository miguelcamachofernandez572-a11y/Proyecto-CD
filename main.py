import os
import json
import matplotlib.pyplot as plt
# importo las librerías
archivos = os.listdir("json/")  # esto me da una lista de archivos que hay en la carpeta 


def promedio(producto_buscado):
    # función que me calcula el promedio de un producto 
    precios = []
    for archivo in archivos:# recorro cad aarchivo de la carpeta , lo abro y lo convierto en un diccionario
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:
                if producto["nombre"] == producto_buscado and producto["disponible"]== True:
                    precios.append(producto["precio"])
    
    promedio = round(sum(precios)/len(precios)) # aqui hago la cuenta del promedio

    return promedio
# aqui guardo en un diccionario los productos con su precio promedio  
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
unidades = {
    "Pan": "bolsa",
    "Leche": "litro",
    "yogurt": "litro",
    "aceite": "litro",
    "Pañales": "paquete",
    "Toallitas húmedas": "paquete",
    "pollo": "kg",
    "picadillo": "kg",
    "huevo": "kg",
    "queso": "kg",
    "sopas": "kg",
    "arroz": "kg",
    "frijoles": "kg",
    "cereales": "kg",
    "galletas": "kg"
}


def grafico_precio_promedio_vs_pension_minima(diccionario):
    # función que me compara visualmente el precio promedio de un producto con la pension mínima de un jubilado
    keys = diccionario.keys()
    values = diccionario.values()

    barras=plt.bar(keys,values,color="#6a4d57")
    plt.axhline(y=3056,color="#9c9386",ls="--",label="Pensión mínima")#línea que marca la pensión mínima
    plt.legend()#  muestro la leyenda
    plt.title("Precio promedio de productos")
    plt.annotate("Pensión Mínima: 3056",(1,3000),(0,2800))
    plt.xticks(rotation=45) # giro los nombres para que se lean mejor
    plt.tight_layout()# ajusto el gráfico para que no se corte
    for barra, producto in zip(barras, keys):
        altura = barra.get_height()# valor de la barra
        unidad = unidades[producto]# unidad correspondiente
        plt.text(
        barra.get_x() + barra.get_width()/2, # posición X centrada
        altura + 50,# un poco arriba de la barra
        f"{altura} pesos/{unidad}",# texto mostrado
        ha="center", va="bottom", fontsize=8, color="black"
    )
    plt.show()# muestro el gráfico


def grafico_servicio_domicilio():
    # función para ver cuantas mipymes ofrecen servicio a domicilio
    disponible=0
    nodisponible=0
    for archivo in archivos: # recorro los archivos , los abro y los convierto en diccionario 
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            if "servicio_a_domicilio" in data:
                            if data["servicio_a_domicilio"]["valor"]==True:# reviso si existe el servicio a domicilio

                                disponible += 1
                            else:
                                nodisponible += 1
    plt.pie( # hago gráfico circular o de pastel
    [disponible, nodisponible],
    labels=["Disponible", "No disponible"],
    autopct='%1.1f%%',
    colors=["#6a4d57", "#9c9386"]
    )
    plt.title("Disponibilidad del servicio a domicilio", fontsize=15, fontweight='bold')
    plt.axis('equal') # esto es para que el círculo no se vea ovalado
    plt.show() # muestro el gráfico


def grafico_precios_marca_producto(producto_buscado="pollo"):
    # función para ver cuales son las marcas mas baratas de un producto 
    lista=[]
    for archivo in archivos:# recorro los archivos , los abro y los convierto en diccionario 
        with open(f"json/{archivo}", encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:
                if producto["nombre"].lower().strip() == producto_buscado.lower().strip() and producto["disponible"] == True:
                    precio = producto["precio"]# guardo el precio
                    unidad_de_medida = str(producto["unidad de medida"])# guardo la unidad de medida
                    marca = str(producto["marca"])# guardo la marca del producto
                    lista.append({"marca": marca, "precio": precio, "unidad_de_medida": unidad_de_medida})

    dic = {}# en este diccionario me voy a quedar con el producto mas barato de cada marca
    for p in lista:
        marca = p["marca"]
        if marca not in dic or p["precio"] <= dic[marca]["precio"]:
            dic[marca] = p

    lista = sorted(dic.values(), key=lambda x: x["precio"])# ordeno por precio
    # listas para graficar
    marcas = []
    precios = []
    unidades = []
    for p in lista:
        marcas.append(p["marca"])
        precios.append(p["precio"])
        unidades.append(p["unidad_de_medida"])

    barras = plt.barh(marcas, precios, color="#9c9386") # hago gráfico de barras horizontal
    plt.bar_label(barras, unidades, label_type="edge") # pongo la unidad al lado de cada barra
    plt.title("Gráfico de las marcas de " + producto_buscado )
    plt.ylabel("Marca")
    plt.xlabel("Precio")
    plt.grid(axis="x", linestyle="--", alpha=0.6)  # líneas de guía en el eje X
    plt.show()


def grafico_disponibilidad_mypimes():
    # función para ver cuántos productos disponibles tiene cada mipyme
    disponibilidad={}
    for archivo in archivos: # recorro los archivos , los abro y los convierto en diccionario 
        contador=0
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:
                if producto["disponible"]==True:
                    contador+=1 # sumo si esta disponible 
                    
        nombre = archivo.replace(".json", "") # me quedo con  el nombre del archivo sin .json
        disponibilidad[nombre] = contador # guardo cuantos productos disponibles tiene
    claves_ordenadas = sorted(disponibilidad.keys(), key=lambda x: int(x.replace("mipyme", "")))
    valores_ordenados = [disponibilidad[k] for k in claves_ordenadas]

    plt.plot( # Hago un gráfico de línea 
        claves_ordenadas,valores_ordenados,
        color="#6a4d57",   
        linewidth=3,# para que la linea sea mas gruesa          
        marker="*",# para que los puntos tengan forma de estrella         
        markersize=15 
        )
    plt.title(
        "Gráfico de disponibilidad de productos de las mipymes",    
    fontsize=16,                    
    fontweight="bold"
    )
    plt.xlabel("Mipymes", fontsize=12)      
    plt.ylabel("Artículos Disponibles ($)", fontsize=12)
    plt.xticks(rotation=45, ha="right")# giro el nombre de las mipymes   
    plt.tight_layout()# ajusto el gráfico para que no se corte
    plt.grid(axis="y", linestyle="--", alpha=0.6)# pongo lineas horizontales de guía
    plt.show()
def comparacion_precio_mipymes(producto_comparar):
    # funcíon que me compara el precio de un producto en diferentes mipymes
    precios={}
    pension_minima=3056
    cambio_a_usd=409
    precios_en_usd=[]
    for archivo in archivos: # recorro los archivos , los abro y los convierto en diccionario
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:# busco el producto y veo si está disponible
                if producto_comparar == producto["nombre"] and producto["disponible"]== True:
                    nombre=archivo.replace(".json","")# me quedo con  el nombre de la mipyme sin .json
                    precios[nombre] = producto["precio"]# me quedo con el precio del producto que busco
    claves_ordenadas = sorted(precios.keys(), key=lambda x: int(x.replace("mipyme", "")))# ordeno las mipymes por número
    
    valores_ordenados = [precios[k] for k in claves_ordenadas]
    # convierto los precios de pesos a usd
    for x in valores_ordenados:
        nuevo_precio=x/cambio_a_usd
        precios_en_usd.append(nuevo_precio)
        
    plt.scatter(claves_ordenadas,precios_en_usd,s=300,color="#9c9386",marker="*")
    # hago un gráfico de puntos donde los cambio nuevamente por estrellas le asigno un color y aumento el tamaño de las estrellas
    plt.title("Precio del " + producto_comparar + " en usd en todas las mipymes")
     # Pongo una línea que muestra la pensión promedio en usd
    plt.axhline(y=pension_minima/cambio_a_usd,color="black",linestyle="--",linewidth=2,label="Pensión mínima en USD")
    plt.legend()# muestro la leyenda de la linea
    plt.text(# escribo cuanto es la pension promedio en usd
         x=3, y=7.5, 
    s=f"{7.5:.2f} usd",
    ha="center", va="top", fontsize=10, color="black", backgroundcolor="white")
    plt.xlabel("Mipymes",fontsize=12)
    plt.ylabel("Precio en usd($)",fontsize=12)
    plt.xticks(rotation=45, ha="right")# giro los nombres de las tiendas
    plt.grid(True, linestyle="--", alpha=0.5)# pongo estas lineas de fondo
    plt.show()

#llamado
grafico_precio_promedio_vs_pension_minima(diccionario)    
comparacion_precio_mipymes(producto_comparar="pollo")
grafico_precios_marca_producto(producto_buscado="pollo")
grafico_disponibilidad_mypimes()            
grafico_servicio_domicilio()            
    