playlist = {}

playlist['canciones'] = [] #lista vacia
#funcion principal
def app():
    

    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('¿Como deseas nombrar la playlist?\n\r')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            #si tenemos nombre
            agregar_playlist = False
            #agregar canciones
            agregar_canciones()


def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion:
        #Preguntar al usuario que cancion desean agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones para la playlist {nombre_playlist}\r\n'
        pregunta += 'Escribe "x" para dejar de agregar canciones.\r\n'

        cancion = input(pregunta)
        if cancion == 'x':
            #dejar de guardar canciones
            agregar_cancion = False

            #mostrar resumen de la playlist
            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion)
            #print(playlist)


def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones:.....\r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()