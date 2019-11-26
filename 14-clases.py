class Restaurant:
    def agregar_restaurant(self, nombre):
        self.nombre = nombre

    def mostrar_informacion(self):
        print(f'Nombre:  {self.nombre}')

#instanciar la clase

restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria tato')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesas quito')
restaurant2.mostrar_informacion()