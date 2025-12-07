import json
import os

def cargar_json(ruta_archivo):
    
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def promedio_precios(lista_rutas):
    
    precios = []
    for ruta in lista_rutas:
        datos = cargar_json(ruta)
        
        for producto in datos["productos"]:
            if producto.get("disponible", False):  
                precios.append(producto["precio"])
    if len(precios) == 0:
        return 0
    return sum(precios) / len(precios)

# --- Ejemplo de uso ---
carpeta = r"C:\miguel\Proyecto CD\json"
archivos = [os.path.join(carpeta, f"mipyme{i}.json") for i in range(1, 26)]

promedio = promedio_precios(archivos)
print("El precio promedio de los productos disponibles es:", promedio)