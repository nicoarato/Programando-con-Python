def informacion():
    print("Imprimiendo texto")

#informacion()

#la indentacion es importante.


# Python3 program introducing f-string 
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.") 
  
  
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.") 

def info1(nombre, puesto = 'Desempleado'):
    print(f'Soy {nombre}, y soy {puesto}.')

info1('Pedro', 'Carpintero')
info1('Carlos', 'Programador')
info1('Nicolas', 'Ingeniero')

def info2(nombre):
    return nombre

empleado = info2('carlos')
info1(empleado)

def mostrar_nombre(nombre):
    print(nombre.upper())

mostrar_nombre('carlitos')