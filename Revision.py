class Vehicule:
    def __init__(self, marque, modele, anne):
        self.setMarque(marque)
        self.setModele(modele)
        self.setAnne(anne)

    def setMarque(self, marque):
        if len(marque) > 0:
            self.__marque = marque
        else:
            ex = Exception('marque is not valid')
            raise ex

    def setModele(self, modele):
        if len(modele) > 0:
            self.__modele = modele
        else:
            ex = Exception('modele is not valid')
            raise ex

    def setAnne(self, anne):
        if anne > 0:
            self.__anne = anne
        else:
            ex = Exception('anne is not valid')
            raise ex

    def getMarque(self):
        return self.__marque

    def getModele(self):
        return self.__modele

    def getAnne(self):
        return self.__anne

    def __str__(self):
        return self.__marque + '\t' + self.__modele + '\t' + str(self.__anne)

    def afficher_info(self):
        print(self)
