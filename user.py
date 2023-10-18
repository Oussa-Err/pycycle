class User :
    def __init__(self,login,pswrd):
        self.setLogin(login)
        self.setPswrd(pswrd)
    def setLogin(self,login):
        if len(login)>0:
            self.__login=login
        else :
            raise Exception("login vide")
    def setPswrd(self,pswrd):
        if len(pswrd)>0:
            self.__pswrd=pswrd
        else:
            raise Exception("pswrd vide") 
    def getLogin(self):
        return self.__login
    def getPswrd(self):
        return self.__pswrd
    def __str__(self):
        return self.__login  + '\t' +  self.__pswrd
    def afficher():
        pass
    