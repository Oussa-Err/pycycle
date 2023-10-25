from forms.form_stagire import FormStagire
import tkinter as tk
from forms.form_stagire import GestionStagire


class FormAdmin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("admin")
        self.btnGestStagire = tk.Button(
            self.root, text="Gestion de stagire", width=20, command=self.Geststagire)
        self.btnGestStagire.pack(pady=55)
        self.btnGestFormateur = tk.Button(
            self.root, text="Gestion de Formateur", width=20)
        self.btnGestFormateur.pack()
        self.btnGestAdmin = tk.Button(
            self.root, text="Gestion de Admin", width=20)
        self.btnGestAdmin.pack(pady=55)

        self.root.mainloop()

    def Geststagire(self):
        self.root.destroy()
        GestionStagire()
