import tkinter as tk
from stagire import Stagire
from etablissement import Etablissement
class FormSearch:
    def __init__(self):
          self.root=tk.Tk()
          self.etab1=Etablissement("espigc","khemissat","01111111","gmail@gmail.com")
          self.etab1.charger()
          self.root.geometry("200x200")
          self.root.columnconfigure(1,weight=1)
          self.frameLableEntry=tk.Frame(self.root)
          self.frameLableEntry.pack(expand=1)
          self.frameBUtten=tk.Frame(self.root)
          self.frameBUtten.pack(expand=1)
          self.lblLogin=tk.Label(self.frameLableEntry,text="login")
          self.lblLogin.grid(row=1,column=0,pady=10)
          self.entryLogin=tk.Entry(self.frameLableEntry)
          self.entryLogin.grid(row=1,column=1)
          self.btnAdd=tk.Button(self.frameBUtten,text="exit",command=self.exit)
          self.btnAdd.grid(row=0,column=1,padx=10)
          self.btnserch =tk.Button(self.frameBUtten,text="search")
          self.btnserch.grid(row=0,column=2,padx=10)
    def exit(self):
         self.root.destroy()


