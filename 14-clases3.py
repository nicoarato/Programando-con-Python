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

#Crear una clase hijo

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre,categoria,precio)

hotel = Hotel('POO - Hotel', '5 estrellas', 200)
hotel.mostrar_informacion()