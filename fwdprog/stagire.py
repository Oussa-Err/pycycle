from user import User
from form_stagire import FormStagire
class Stagire(User):
    def __init__(self,numIus,login, pwd):
        super().__init__(login, pwd)
        self.setNumIus(numIus)
    def __str__(self):
        return self.__numIus +'\t'+ self.__login 

    def getNumIus(self):
        return self.__numIus 
    def setNumIus(self,numIus):
        if len(numIus)>0:
            self.__numIus=numIus
        else:
            raise Exception("numIus vide")
    def afficher(self):
        FormStagire()
