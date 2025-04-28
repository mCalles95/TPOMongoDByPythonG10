from pymongo import MongoClient
import json

# Leer configuración desde el archivo JSON
with open("./config/config.json", "r") as config_file:
    config = json.load(config_file)

# Conexión a la base de datos MongoDB
client = MongoClient(config["mongo_uri"])
db = client[config["database"]]
collection = db["animales"]  # Cambia "shows" si el nombre de la colección es diferente

# Consulta: cantidad de shows por edificio
resultado = collection.aggregate([
    {"$group": {"_id": "$habitat_id", "cantidad_animales": {"$sum": 1}}}
])

# Convertir el cursor en una lista para evitar problemas de consumo
resultado = list(resultado)

# Mostrar resultados
print("Cantidad de animales por habitat")
for habitat in resultado:
    cantidad = habitat.get("cantidad_animales", 0)  # Manejar valores None
    print(f"Habitat: {habitat['_id']}, Cantidad de animales: {cantidad}")