from Revision import Vehicule

class Voiture(Vehicule):
    def __init__(self, modele, marque, anne, nombre_portes):
        super().__init__(modele, marque, anne)
        self.setNombre_portes(nombre_portes)

    def getNombre_portes(self):
        return self.__nombre_portes

    def setNombre_portes(self, nombre_portes):
        if nombre_portes > 0:
            self.__nombre_portes = nombre_portes
        else:
            ex = Exception("nombre de portes n'est pas valide")
            raise ex

    def __str__(self):
        return super().__str__() + '\t' + str(self.__nombre_portes)






class Camion(Vehicule):
    def __init__(self, modele, marque, anne, charge_max):
        super().__init__(modele, marque, anne)
        self.setCharge_max(charge_max)

    def getCharge_max(self):
        return self.__charge_max

    def setCharge_max(self, charge_max):
        if charge_max > 0:
            self.__charge_max = charge_max
        else:
            ex = Exception("charge maximum n'est pas valide")
            raise ex

    def __str__(self):
        return super().__str__() + '\t' + str(self.__charge_max)

    @staticmethod(counter)
    def counter(cls):
        print('')


    @classmethod(f)