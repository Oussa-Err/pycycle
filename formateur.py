from user import User
class formateur (User):
    def __init__(self,login,pwd,matricule):
        super(login,pwd)
        self.setMatricule(matricule)

    def setMatricule(self,matricule):
        if matricule > 0:
         self.__matricule = matricule

    def getMatricule(self):
       return self.__matricule
    
    def __str__(self):
       return super().__str__() + '\t' + str(self.__matricule)

        



    