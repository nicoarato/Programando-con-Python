nombre = input('Cual es tu nombre?\r\n')
print(f'Hola {nombre}')

edad = input('Cual es tu edad? : ')
#convertir a entero
edad = int(edad)


if edad >= 18:
    print('Ya podes votar!')
else:
    print('Todavía no votas...')


