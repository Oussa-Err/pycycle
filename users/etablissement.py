from sys import path
path.append("/home/karim/TSDI/tp_TSDI_PY")
import pickle
from users.user import User


class Etablissement(User):
    def __init__(self, nom, adress, tell, email):
        self.setNom(nom)
        self.setAdress(adress)
        self.setTell(tell)
        self.setEmail(email)
        self.__users = list()

    def getNom(self):
        return self.__nom

    def setNom(self, nom):
        if len(nom) > 0:
            self.__nom = nom
        else:
            raise Exception("nom vide")

    def getAdress(self):
        return self.__adress

    def setAdress(self, adress):
        if len(adress) > 0:
            self.__adress = adress
        else:
            raise Exception("adress vide")

    def getTell(self):
        return self.__tell

    def setTell(self, tell):
        if len(tell) > 0:
            self.__tell = tell
        else:
            raise Exception("tell vide")

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        if len(email) > 0:
            self.__email = email
        else:
            raise Exception("email vide")

    def getUsers(self):
        return self.__users

    def setUsers(self, users):
        self.__users = users

    def ajouter(self, user: User):
        self.__users.append(user)

    def exist(self, login: User):
        ex = False
        for user in self.__users:
            if User.getLogin() == login:
                ex = True
                break
        return ex

    def save(self):
        fichier = open("user.dat", "wb")
        pickle.dump(self.__users, fichier)
        fichier.close()

    def charger(self):
        fichier = open("user.dat", "rb")
        self.__users = pickle.load(fichier)
        fichier.close()

    def authentifier(self, login, pwd):
        self.charger()
        for user in self.__users:
            if user.getLogin() == login and user.getPwd() == pwd:
                user.afficher()
                break
