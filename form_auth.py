import tkinter as tk
from etabliss import Etabliss
class FormAuth:
    def __init__(self):
        self.e=Etabliss("chaymaa","chaymaa@gmail.com","22344","098890")
        self.root=tk.Tk()
        self.root.title("connection")
        self.root.geometry("300x200")
        self.lblLogin=tk.Label(self.root,text="login")
        self.lblLogin.grid(row=0,column=0)
        self.lblPwd=tk.Label(self.root,text="Pwd")
        self.lblPwd.grid(row=1,column=0)
        self.entryLogin=tk.Entry(self.root)
        self.entryLogin.grid(row=0,column=1)
        self.entryPwd=tk.Entry(self.root)
        self.entryPwd.grid(row=1,column=1)
        self.btnok=tk.Button(self.root,text="ok",command=self.okclick)
        self.btnok.grid(row=2,column=1)
        
        self.root.mainloop()
    def okclick(self):
        self.e.authentifier(self.entryLogin.get(),self.getPwd.get())

 