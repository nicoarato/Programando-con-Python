balance = 5

if balance > 3:
    print('Se puede pagar')
else:
    print('No puedes pagar nada')

likes = 200
if likes == 200:
    print('buenos likes')


# con letras
lenguaje = 'python'

if lenguaje == 'python':
    print('Excelente decision')

#Evaluar boolean
usuario_aut = True
if usuario_aut :
    print('Acceso correcto')
else:
    print('Acceso denegado')

#en la list

lenguajes = ['python', 'c++', 'php', 'java']
leng = 'php'
if  leng in lenguajes:
    print(f'{leng} Está en la lista')
else:
    print(f'{leng} No Existe en la lista')

#ELIF

ocupacion = 'maestro'

if ocupacion == 'Estudiante':
    print('Tienes un 50% de descuento')
elif ocupacion == 'Jubilado':
    print('Tienes un 75% de descuento')
elif ocupacion == 'desempleado':
    print('Tienes un 80% de descuento')
elif ocupacion == 'maestro':
    print('Tienes un 90% de descuento')
else:
    print('Tienes un 0% de descuento')

# AND y OR
usuario_log = True
usuario_admin = False
if usuario_log and usuario_admin:
    print('usuario admin')
elif usuario_log:
    print('Acceso al sistema')
else:
    print('Iniciar sesión')