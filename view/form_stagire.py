import tkinter as tk
from users.etablissement import Etablissement


class FormStagire:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("stagire")

        self.root.mainloop()


class GestionStagire:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title(" Gestion de Stagire")
        self.lblNumIus = tk.Label(self.root, text="numIus")
        self.lblNumIus.grid(row=0, column=0, pady=10, padx=60)
        self.entryNumIus = tk.Entry(self.root)
        self.entryNumIus.grid(row=0, column=1)
        self.lblLogin = tk.Label(self.root, text="login")
        self.lblLogin.grid(row=1, column=0, pady=10, padx=60)
        self.entryLogin = tk.Entry(self.root)
        self.entryLogin.grid(row=1, column=1)
        self.lblPwd = tk.Label(self.root, text="Password")
        self.lblPwd.grid(row=2, column=0, pady=10, padx=60)
        self.entryPWD = tk.Entry(self.root)
        self.entryPWD.grid(row=2, column=1)

        self.btnAdd = tk.Button(self.root, text="add")
        self.btnAdd.grid(row=3, column=0)
        self.btnShow = tk.Button(self.root, text="show")
        self.btnShow.grid(row=3, column=1, sticky="w")
        self.btnAdd = tk.Button(self.root, text="save")
        self.btnAdd.grid(row=3, column=1, sticky="e")
        self.btnAdd = tk.Button(self.root, text="exit")
        self.btnAdd.grid(row=3, column=5, padx=40)

        self.root.mainloop()

    def save(self):
        self.save1 = Etablissement.save(Stagire)

    def add(self):
        self.stagire.authentifier(self.entryNumIus.get(
        ), self.entryLogin.get(), self.entryPWD.get())
        self.add1 = Etablissement.ajouter()
