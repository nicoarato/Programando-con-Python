def app():
    #crear archivo
    archivo = open('archivo.txt', 'w') #w es escritura, si no existe lo creará

    #generar numeros en archivo
    for i in range(0,20):
        archivo.write('Esta es la linea' + str(i) + "\r\n")

    #cerrar archivo
    archivo.close()


app()