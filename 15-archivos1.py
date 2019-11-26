def app():

    with open('archivo.txt') as archivo: #default 'r'
        for contenido in archivo:
            print(contenido.rstrip()) #rstrip saca saltos de linea



app()