#diccionario simple
cancion = {
    #llave y valor
    'artista' : 'Metallica',
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}

print(cancion['artista'])
print(cancion['lanzamiento'])

#mezclar con string
artista = cancion['artista']
print(f'Estoy escuchando {artista}')

#agregar nuevos valores
cancion['playlist'] = 'Heavymetal'
print(cancion)

#reemplazar valor existente
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

#eliminar un valor
del cancion['lanzamiento']
print(cancion)

#iniciar un diccionario vacio
jugador = {}
print(jugador)

#darle valores
jugador['nombre'] = 'Juan'
jugador['puntaje'] = 0
print(jugador)

#incrementa puntaje
jugador['puntaje']= 100
print(jugador)

#acceder a un valor
print(jugador.get('puntaje', 'No existe ese valor'))

#iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']

print(jugador)