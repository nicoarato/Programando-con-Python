class Restaurant:

    def __init__(self, nombre, categoria, precio):
        #default: public ; 
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio # nomenclatura => PUBLIC _PROTECTED  __PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre:  {self.__nombre} - Categoria:  {self.__categoria} - Precio:  {self.__precio}')

    #getters y setters
    def get_precio(self):
        return self.__precio
    
    def get_nombre(self):
        return self.__nombre
    
    def get_categoria(self):
        return self.__categoria

    def set_precio(self, precio):
        self.__precio = precio


#instanciar la clase

restaurant = Restaurant('Pizzeria tato', 'comida italiana', 50)
Precio = restaurant.get_precio()
print(Precio)
restaurant.set_precio(100)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas quito', 'fast food', 20)
Precio2 = restaurant.get_precio()
print(Precio2)
restaurant2.set_precio(200)

restaurant2.mostrar_informacion()


