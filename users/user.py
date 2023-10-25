class User:
    def __init__(self, login, pwd):
        self.setLogin(login)
        self.setPwd(pwd)

    def __str__(self):
        return self.__login

    def getLogin(self):
        return self.__login

    def setLogin(self, login):
        if len(login) > 0:
            self.__login = login
        else:
            raise Exception("login vide")

    def getPwd(self):
        return self.__pwd

    def setPwd(self, pwd):
        if len(pwd) > 0:
            self.__pwd = pwd
        else:
            raise Exception("pwd vide")

    def afficher(self):
        print("interface user")
