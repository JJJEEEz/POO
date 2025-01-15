class Personaje:
    # Atrubutos de la clase
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza: ", self.__fuerza)
        print("-Inteligencia: ", self.__inteligencia)
        print("-Defensa: ", self.__defensa)
        print("-Vida: ", self.__vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0
    
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def dañar(self, enemigo):
        daño = self.__fuerza - enemigo.__defensa
        if daño > 0:
            return daño
        else:
            return 0

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida - daño

        if 0 >= enemigo.__vida:
            enemigo.morir()

        else:
            print(self.__nombre, "ah realizado", daño, "puntos de daño a", enemigo.__nombre)
            print("vida de", enemigo.__nombre, "es", enemigo.__vida)
    
    def get_vida(self):
        return self.__vida
    
    def set_vida(self, vida):
        self.__vida = vida
        # if self.__vida <= 0:
        #     self.morir()


#Variable del constructor (nombre, fuerza, inteligencia, defensa, vida)
mi_personaje = Personaje("EstebanDido", 40, 50, 45, 100)
mi_enemigo = Personaje("Angel", 70, 100, 70, 100)

print(mi_personaje.get_vida())
mi_personaje.set_vida(-5)
print(mi_personaje.get_vida())
mi_personaje.Personaje__vida = -5
mi_personaje.imprimir_atributos()

# # mi_personaje.vida
# mi_personaje.__vida

# mi_personaje.vida = 0
# mi_personaje.imprimir_atributos()

# mi_personaje.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)
# mi_personaje.morir()
# print(mi_personaje.esta_vivo())
# mi_personaje.subir_nivel(15, 5, 10)
# print("valores actualizados")
# mi_personaje.imprimir_atributos()



#Modificando valores de los atributos
# mi_personaje.__nombre = "EstebanDido"
# mi_personaje.__fuerza = 300
# mi_personaje.__inteligencia = -2
# mi_personaje.__defensa = 30
# mi_personaje.__vida = 2

# print("El nombre de mi personaje es: ", mi_personaje.__nombre)
# print("El nombre de mi personaje es: ", mi_personaje.__fuerza)
# print("El nombre de mi personaje es: ", mi_personaje.__inteligencia)
# print("El nombre de mi personaje es: ", mi_personaje.__defensa)
# print("El nombre de mi personaje es: ", mi_personaje.__vida)