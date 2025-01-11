class Personaje:
    # Atrubutos de la clase
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza: ", self.fuerza)
        print("-Inteligencia: ", self.inteligencia)
        print("-Defensa: ", self.defensa)
        print("-Vida: ", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def dañar(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        if daño > 0:
            return daño
        else:
            return 0

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño

        if 0 >= enemigo.vida:
            enemigo.morir()

        else:
            print(self.nombre, "ah realizado", daño, "puntos de daño a", enemigo.nombre)
            print("vida de", enemigo.nombre, "es", enemigo.vida)

#Variable del constructor (nombre, fuerza, inteligencia, defensa, vida)
mi_personaje = Personaje("EstebanDido", 40, 50, 45, 100)
mi_enemigo = Personaje("Angel", 70, 100, 70, 100)
mi_personaje.imprimir_atributos()
mi_personaje.atacar(mi_enemigo)
# mi_personaje.morir()
# print(mi_personaje.esta_vivo())
# mi_personaje.subir_nivel(15, 5, 10)
# print("valores actualizados")
# mi_personaje.imprimir_atributos()



#Modificando valores de los atributos
# mi_personaje.nombre = "EstebanDido"
# mi_personaje.fuerza = 300
# mi_personaje.inteligencia = -2
# mi_personaje.defensa = 30
# mi_personaje.vida = 2

# print("El nombre de mi personaje es: ", mi_personaje.nombre)
# print("El nombre de mi personaje es: ", mi_personaje.fuerza)
# print("El nombre de mi personaje es: ", mi_personaje.inteligencia)
# print("El nombre de mi personaje es: ", mi_personaje.defensa)
# print("El nombre de mi personaje es: ", mi_personaje.vida)