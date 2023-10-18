from user import User
class Admin (User):
    def __init__(self, login, pwd):
        super().__init__(login, pwd)
    def __str___(self):
        return super.__str__()
    def afficher(self):
        print("Interface Admin")
    
        
    
