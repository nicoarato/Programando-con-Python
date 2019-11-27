#libreia para archivos
import os

CARPETA = 'contactos/'
EXTENSION = '.txt'

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria



def app():

    crear_directorio()
    #muestra el menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion a realizar
    preguntar = True

    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)
        if opcion == 1:
            print('Agregar contacto')
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print('Editar contacto')
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción NO válida, intente de nuevo.')

def agregar_contacto():
    print('Escribe los datos del nuevo contacto')
    nombre_contacto = input('Nombre del contacto \r\n')

    #revisar si existe el archivo
    existe = existe_contacto(nombre_contacto)


    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            #resto de campos
            telefono_contacto = input('Telefono:  \r\n')
            categoria_contacto = input('Categoria:  \r\n')

            #instancio la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #mensaje de exito
            print('\r\n Contacto creado correctamente....\r\n')
    else:
        print('El usuario ya existe')

    #reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            print('\r\n')
            for linea in contacto:
                print(linea.rstrip())
            #imprime separador
            print('\r\n')
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
        app()

def editar_contacto():
    nombre_anterior = input('Nombre del contacto que quiere editar: \r\n')
    #revisar si existe el archivo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            #resto de campos
            nombre_contacto = input('Agrega el Nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el Nuevo Telefono:  \r\n')
            categoria_contacto = input('Agrega la Nueva Categoria:  \r\n')

            #instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #escribir el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            print('\r\n Contacto editado correctamente \r\n')

    else:
        print('No se puede editar')

def eliminar_contacto():
    nombre = input('Seleccione el contacto a eliminar: \r\n')

    try:
        os.remove(CARPETA+nombre + EXTENSION)
        print('\r\n Eliminado correctamente..')
    except:
        print('No existe ese contacto')
    
    #reiniciar app
    app()

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contactos')
    print('5) Eliminar Contactos')


def crear_directorio():
    if not os.path.exists(CARPETA):
        #crear la carpeta
        os.makedirs(CARPETA)
    else:
        print('La carpeta existe')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)



app()