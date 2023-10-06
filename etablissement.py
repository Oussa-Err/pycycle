from user import User

class Etablissement:
    def __init__(self) -> None:
        self.__users = list()
    
    
    def getUsers(self):
        return self.__users
        
    
    def addUser(self, user: User):
        self.__users.append(user)

    def deleteUser(self, user: User):
        self.__users.remove(user)

    def updateUser(self, user: User):
        for i in self.__users:
            if (i.getLogin() == user.getLogin):
                i = user

    def __str__(self) -> str:
        s = ''
        for i in self.__users:
            s += i.__str__()  + '\n'         
        return s

