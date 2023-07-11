
from Revision import Vehicule
from Revision1 import Voiture, Camion

try:
    Vehicule('Camaro', 'yahoo', 2023).afficher_info()
    Voiture('Toyota', 'landCruiser', 2031, 4).afficher_info()
    Camion('dacia', 'sandero', 2001, 500).afficher_info()

except Exception as ex:
    print(ex)


