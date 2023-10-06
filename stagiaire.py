from user import User
class Stagiaire(User):
    def __init__(self,numIns,login,pwd):
        self.setnumIns(numIns)

    def setnumIns(self,numIns):
     try:
        if (len(numIns)>0):
            self.__numIns = numIns  
     except:
       raise Exception("numIns valide")
    


