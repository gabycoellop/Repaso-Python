personas={'nombre':'Rosa', 'edad':30,'ciudad': 'Valencia'}

print(len(personas))
print(personas['edad'])#30
print(personas['nombre'])
print(personas['ciudad'])

personas['nombre']="Jose"
print(['nombre'])
print(personas.keys())#obtengo todas las claves
print(personas.values())#obtener todos los valores
print(personas.items())#obtener valor y clave
print(personas.get('dsafasdgt'))#el get para hacer una busqueda de un valor por su key
print(personas.pop('edad'))#elimina un elemento por su clave
print(personas)
print(personas.update({'pais':'España'}))#añade un elemento nuevo
print(personas)

for k,v in personas.items():
    print(f"key: {k}, value{v}")
