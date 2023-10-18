from user import User
class Stagaire(User):
    def __init__(self,login,pswrd,numIns):
        super().__init__(login,pswrd)
        self.setNumIns(numIns)
    def setNumIns(self,numIns):
        if len(numIns)>0:
            self.__numIns=numIns
        else :
            raise Exception("NumIns vide")
    def __str__(self):
        return super.__str__()+'\t'+self.__numIns
    
    def afficher(self):
        print("Interface Stagaire")