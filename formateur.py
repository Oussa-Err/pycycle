from user import User
class Formateur(User):
    def __init__(self,login,pwd,matricule):
         super().__init__(login,pwd)
         self.setMatricule(matricule)
    def setMatricule(self,marticule):
        if len(marticule)>0:
            self.__matricule=marticule
        else :
            raise Exception("matricule vide")
    def __str__(self):
        return super.__str__()+'\t'+self.__matricule
    def afficher(self):
        print("Interface Formateur")