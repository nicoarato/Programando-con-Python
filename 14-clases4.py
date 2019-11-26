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

#Crear una clase hijo HERENCIA

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, pieza):
        super().__init__(nombre,categoria,precio)
        self.__pieza = pieza
    
    def get_pieza():
        return self.__pieza
    def set_pieza(pieza):
        self.__pieza = pieza

    #reescribir un metodo , se debe llamar igual
    def mostrar_informacion(self):
        print(f'Nombre:  {self.get_nombre()} - Categoria:  {self.get_categoria()} - Precio:  {self.get_precio()} - Pieza : {self.__pieza}')

    #agregar un metodo especifico de hotel
    def get_pieza(self):
        return self.__pieza


hotel = Hotel('POO - Hotel', '5 estrellas', 200, 'SI')
hotel.mostrar_informacion()
pieza = hotel.get_pieza()
print(pieza)