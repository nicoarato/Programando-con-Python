pregunta = 'Agrega un número y te digo si es par...\n\r'
pregunta += '(Escribe "cerrar " para salir de la aplicacion.\n\r)'


preguntar = True

while preguntar:

    #mezclando con operadores
    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print(f'El numero {numero} es par')
        else:
            print(f'El numero {numero} es impar')
