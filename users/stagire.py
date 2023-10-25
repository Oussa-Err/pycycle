import pickle
from user import User
from users.etablissement import Etablissement
from form_stagire import FormStagire


class Stagire(User):
    def __init__(self, numIus, login, pwd):
        super().__init__(login, pwd)
        self.setNumIus(numIus)

    def __str__(self):
        return self.__numIus + '\t' + self.__login

    def getNumIus(self):
        return self.__numIus

    def setNumIus(self, numIus):
        if len(numIus) > 0:
            self.__numIus = numIus
        else:
            raise Exception("numIus vide")

    def afficher(self):
        FormStagire()

    def save(self):
        fichier = open("stagire.dat", "wb")
        pickle.dump(self.__users, fichier)
        fichier.close()

    def charger(self):
        fichier = open("stagire.dat", "rb")
        self.__users = pickle.load(fichier)
        fichier.close()

    def authentifier(self, numIus, login, pwd):
        self.charger()
        for user in self.__users:
            if user.getLogin() == login and user.getPwd() == pwd and user.getNumIus() == numIus:
                user.afficher()
                break
