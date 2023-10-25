import tkinter as tk
from users.etablissement import Etablissement


class FormAuth:
    def __init__(self):
        self.etabl = Etablissement("espigc", "aaaaaa", "01111111", "zz")
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("authentifier")
        self.lbLogin = tk.Label(self.root, text="login")
        self.lbLogin.grid(row=0, column=0)
        self.entryLogin = tk.Entry(self.root)
        self.entryLogin.grid(row=0, column=1)
        self.lblPwd = tk.Label(self.root, text="password")
        self.lblPwd.grid(row=1, column=0)
        self.entryPwd = tk.Entry(self.root)
        self.entryPwd.grid(row=1, column=1)
        self.btnOk = tk.Button(self.root, text="Ok", command=self.okClick)
        self.btnOk.grid(row=2, column=4)

        self.root.mainloop()

    def okClick(self):
        self.etabl.authentifier(self.entryLogin.get(), self.entryPwd.get())
        self.root.destroy()
