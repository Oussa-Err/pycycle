from user import User
class Formateur(User):
    def __init__(self,matricule, login, pwd):
        super().__init__(login, pwd)
        self.setMatricule(matricule)
    def __str__(self):
        return self.__matricule +'\t'+ self.__numIus +'\t'+ self.__login 
    
    def getMatricule(self):
        return self.__matricule
    def setMatricule(self, matricule):
        if len(matricule)>0:
            self.__matricule=matricule
        else:
            raise Exception("Matricule vide")
    def afficher(self):
        from form_formateur import FormFormateur
        FormFormateur()


    