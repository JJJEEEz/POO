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
        return max(0, self.fuerza - enemigo.defensa)
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)
        
        print("\n", self.nombre, "ah realizado", daño, "puntos de daño a", enemigo.nombre)
        print("vida de", enemigo.nombre, "es", enemigo.vida, "\n")

class Guerrero(Personaje):

    # Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        # Personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida)
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    # Sobrescribir impresión de atributos

    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada: ", self.espada)
    
    # Sobrescribir el calculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
    # Escoger navaja
    def escoger_navaja(self):
        opcion = int(input("Escoge tuna vaja:\n(1) Navaja suiza, daño 10.\n (2) Navaja pioja, daño 6.\n>>>"))
        if (opcion == 1):
            self.espada = 10
        elif(opcion == 2):
            self.espada = 6
        else:
            print("Ingresa un valor valido.")
            # Vuelva a ejecutar el método escoger_navaja
            self.escoger_navaja()

class Mago(Personaje):

    # Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        # Personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida)
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    # Sobrescribir impresión de atributos

    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-libro: ", self.libro)
    
    # Sobrescribir el calculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
    # Escoger navaja
    def escoger_libro(self):
        opcion = int(input("Escoge tu libro:\n(1) El principito, daño 10.\n (2) Crepusculo, daño 6.\n>>>"))
        if (opcion == 1):
            self.mago = 10
        elif(opcion == 2):
            self.mago = 6
        else:
            print("Ingresa un valor valido.")
            # Vuelva a ejecutar el método escoger_navaja
            self.escoger_libro()
    
# Crear todos los objetos
persona = Personaje("Angel", 20, 15, 10, 100)
arturoSuarez = Guerrero("Arturo Suárez", 20, 15, 10, 100, 5)
gandalf = Mago("Gandalf", 20, 15, 10, 100, 5)
#atributos antes de la tragedia
persona.imprimir_atributos()
print("\n")
arturoSuarez.imprimir_atributos()
print("\n")
gandalf.imprimir_atributos()
print("\n")
# Ataques sin piedad
persona.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(persona)
#atributos despues de la tragedia
print("\n")
persona.imprimir_atributos()
print("\n")
arturoSuarez.imprimir_atributos()
print("\n")
gandalf.imprimir_atributos()
print("\n")


#print("El valor de espada es:", arturoSuarez.espada)

#Variable del constructor (nombre, fuerza, inteligencia, defensa, vida)
# mi_personaje = Personaje("EstebanDido", 40, 50, 45, 100)
# mi_enemigo = Personaje("Angel", 70, 100, 70, 100)
# mi_personaje.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)

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