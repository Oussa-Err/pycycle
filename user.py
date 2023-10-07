class User:
  def __init__(self,login,pwd):
      self.setLogin(login)
      self.setPwd(pwd)

  def setLogin(self,login):
        if len(login)>0:
            self.__login = login
        else:
            raise Exception("login valide")
        
  def setPwd(self,pwd):
     if len(pwd)>0:
        self.__pwd = pwd
     else:
         raise Exception("pwd valide")
     
  def getLogin(self):
      return self.__login
  
  def getPwd(self):
      return self.__pwd
  
  def __str__(self):
      return self.__login + '\t' + self.__pwd 
  