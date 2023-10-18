from user import User
import pickle


class Etabliss:
    def __init__(self, nom, adresse, tel, email):
        self.setNom(nom)
        self.setAdresse(adresse)
        self.setTel(tel)
        self.setEmail(email)
        self.__users = list()

    def getNom(self):
        return self.__nom

    def getAdresse(self):
        return self.__adresse

    def getTel(self):
        return self.__tel

    def getEmail(self):
        return self.__email

    def getUsers(self):
        return self.__users

    def setNom(self, nom):
        if len(nom) > 0:
            self.__nom = nom
        else:
            raise Exception("nom vide")

    def setAdresse(self, adresse):
        if len(adresse) > 0:
            self.__adresse = adresse
        else:
            raise Exception("adresse vide")

    def setTel(self, tel):
        if len(tel) > 0:
            self.__Tel = tel
        else:
            raise Exception("tel vide")

    def setEmail(self, email):
        if len(email) > 0:
            self.__email = email
        else:
            raise Exception("email vide")

    def ajouterUser(self, user: User):
        self.__users.append(user)

    def supprimerUser(self, user: User):
        self.__users.remove(user)

    def enregistrementUser(self):
        fichier = open("users.date", "wb")
        pickle.dump(self.__users, fichier)
        fichier.close()

    def charger(self):
        fichier = open("users.date", "rb")
        self.__users = pickle.load(fichier)
        fichier.close()

    def authentifier(self, login, pwd):
        self.charger()
        for user in self.__users:
            if user.getLogin() == login and user.getPswrd() == pwd:
                user.afficher()
                break
