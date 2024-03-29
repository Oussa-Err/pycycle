from form_seach import FormSearch
import tkinter.messagebox as msg
import tkinter as tk
from stagire import Stagire
from etablissement import Etablissement
from tkinter import tix


class FormGestionStagire:
    def __init__(self):
          self.root=tk.Tk()
          self.etab1=Etablissement("espigc","khemissat","01111111","gmail@gmail.com")
          self.etab1.charger()
          self.root.geometry("500x500")
          self.root.title(" Gestion de Stagire")
          self.frameLableEntry=tk.Frame(self.root)
          self.frameLableEntry.pack(expand=1)
          self.frameBUtten=tk.Frame(self.root)
          self.frameBUtten.pack(expand=1)

          self.lblNumIus=tk.Label(self.frameLableEntry,text="numIus")
          self.lblNumIus.grid(row=0,column=0,pady=10)
          self.entryNumIus=tk.Entry(self.frameLableEntry)
          self.entryNumIus.grid(row=0,column=1)
          self.lblLogin=tk.Label(self.frameLableEntry,text="login")
          self.lblLogin.grid(row=1,column=0,pady=10)
          self.entryLogin=tk.Entry(self.frameLableEntry)
          self.entryLogin.grid(row=1,column=1)
          self.lblPwd=tk.Label(self.frameLableEntry,text="Password")
          self.lblPwd.grid(row=2,column=0,pady=10)
          self.entryPWD=tk.Entry(self.frameLableEntry)
          self.entryPWD.grid(row=2,column=1)

          self.btnAdd=tk.Button(self.frameBUtten,text="add",command=self.add)
          self.btnAdd.grid(row=1,column=0,padx=10)
          self.btnShow=tk.Button(self.frameBUtten,text="show")
          self.btnShow.grid(row=1,column=1,padx=10)
          self.btnAdd=tk.Button(self.frameBUtten,text="save",command=self.save)
          self.btnAdd.grid(row=1,column=2,padx=10)
          self.btnAdd=tk.Button(self.frameBUtten,text="back",command=self.back)
          self.btnAdd.grid(row=1,column=3,padx=10)
          self.btndelete=tk.Button(self.frameBUtten,text="delete")
          self.btndelete.grid(row=1,column=4,padx=10)
          self.btnserch =tk.Button(self.frameBUtten,text="search",command=self.search)
          self.btnserch.grid(row=1,column=5,padx=10)
          self.root.mainloop()

    def save(self):
         self.etab1.save()

    def add(self):
          try:
              self.etab1.ajouter(Stagire(self.entryNumIus.get(),self.entryLogin.get(),self.entryPWD.get()))
              self.clear()
              self.entryNumIus.focus()
          except Exception as ex:
              msg.showwarning("warning ",ex)

    def clear(self):
         self.entryLogin.delete(0,len(self.entryLogin.get()))
         self.entryNumIus.delete(0,len(self.entryNumIus .get()))
         self.entryPWD.delete(0,len(self.entryPWD.get()))

    def search(self):
         FormSearch()

    def back(self):
         from form_admin import FormAdmin
         self.root.destroy()
         FormAdmin()

    def show(self):
         window = tix.Tk()
         window.title('list des stagiaire')
         window.geometry("300x200")
         scrolledWindow = tix.ScrolledWindow(window)
         scrolledWindow.pack(expand=1, fill='both')         
         i = 0
         for item in self.etab1.getUsers():
               if isinstance(item, Stagire):
                    entry_login = tix.Entry(scrolledWindow.window)
                    entry_login.grid(row=i, column=0)
                    entry_login.insert(0, item.getLogin())

                    entry_pwd = tix.Entry(scrolledWindow.window)
                    entry_pwd.grid(row=i, column=1)
                    entry_pwd.insert(0, item.getPwd())

                    entry_numI = tix.Entry(scrolledWindow.window)
                    entry_numI.grid(row=i, column=2)
                    entry_numI.insert(0, item.getNumIus())

                    i += 1
         window.mainloop()