from form_stagire import FormStagire
import tkinter as tk
from form_gestion_stagire import FormGestionStagire
from form_gestion_Admin import FormGestionAdmin
from form_Gestion_Formateur import FormGestionFormateur
class FormAdmin:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")
        self.root.title("admin")
        self.framebutten=tk.Frame(self.root)
        self.framebutten.pack(expand=1)
        self.framebutten2=tk.Frame(self.root)
        self.framebutten2.pack(expand=0)
        self.btnexit=tk.Button(self.framebutten2,text="exit")
        self.btnexit.pack(pady=55)

        self.btnGestStagire=tk.Button(self.framebutten,text="Gestion de stagire",width=20,command=self.Geststagire)
        self.btnGestStagire.pack(pady=55)
        self.btnGestFormateur=tk.Button(self.framebutten,text="Gestion de Formateur",width=20,command=self.GestFormateur)
        self.btnGestFormateur.pack()
        self.btnGestAdmin=tk.Button(self.framebutten,text="Gestion de Admin",width=20,command=self.GestAdmin)
        self.btnGestAdmin.pack(pady=55)


        self.root.mainloop()
    
    def Geststagire(self):
        self.root.destroy()
        FormGestionStagire()
        
    def GestAdmin(self):
        FormGestionAdmin()

    def GestFormateur(self):
        FormGestionFormateur()

