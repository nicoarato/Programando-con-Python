lenguajes = ['python', 'c++', 'php', 'java']
print(lenguajes)


print(lenguajes[3])

lenguajes.sort()
print(lenguajes)

aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'

print(aprendiendo)

#modificando valores

lenguajes[2] = 'javascript'

print(lenguajes)

#agregar elementos
lenguajes.append('Ruby')
print(lenguajes)

#eliminar en una posicion

del lenguajes[1]
print(lenguajes)

#eliminar en una posicion

lenguajes.pop(0)
print(lenguajes)

#eliminar ultima posicion

lenguajes.pop()
print(lenguajes)

#eliminar por nombre

lenguajes.remove('javascript')
print(lenguajes)