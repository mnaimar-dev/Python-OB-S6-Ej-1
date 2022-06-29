# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

    # - Color
    # - Ruedas
    # - Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

    # - Velocidad
    # - Cilindrada
    
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
    
class Vehiculo:
        color = input('Ingresa el color: ')
        ruedas = input('Ingresa el número de ruedas: ')
        puertas = input('Ingresa el número de puertas: ')

class Coche(Vehiculo):
    velocidad = input('Ingresa la velocidad: ')
    cilindrada = input('Ingresa la cilindrada: ')


amarok = Coche()

print('Color: ', amarok.color)
print('Ruedas: ', amarok.ruedas)
print('Puertas: ', amarok.puertas)
print('Velocidad: ', amarok.velocidad)
print('Cilindrada: ', amarok.cilindrada)