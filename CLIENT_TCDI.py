class Client:
    def __init__(self, id, nom, prenom, telephone):
        self.setId(id)
        self.setNom(nom)
        self.setPrenom(prenom)
        self.setTelephone(telephone)

    def setId(self, id):
        if id > 0:
            self.__id = id
        else:
            ex = Exception('id is not valid')
            raise ex

    def setNom(self, nom):
        if len(nom) > 3:
            self.__nom = nom
        else:
            ex = Exception('nom n\'est pas valide')
            raise ex

    def setPrenom(self, prenom):
        if len(prenom) > 3:
            self.__prenom = prenom
        else:
            ex = Exception('prenom non valid')
            raise ex

    def setTelephone(self, telephone):
        if len(telephone) > 5:
            self.__telephone = telephone
        else:
            ex = Exception('telephone non valide')
            raise ex

    def getId(self):
        return self.__id

    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getTelephone(self):
        return self.__telephone

    def __str__(self):
        return str(self.__id) + '\t' + self.__nom  + '\t' + self.__prenom + '\t' + str(self.__telephone)

