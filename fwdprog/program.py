import tkinter as tk

root = tk.Tk()
root.title('my prog')
root.geometry('400x400')

root.columnconfigure(1,weight=1)
root.rowconfigure(2,weight=1)

firset_label=tk.Label(root,text='firest')
firset_label.grid(sticky='we',padx=5,pady=5)

firset_inp=tk.Entry(root)
firset_inp.grid(row=0,column=1,sticky=tk.E+tk.W)

gategories=['work','gym','rest','bills']
gatego_label=tk.Label(root,text='gategories : ')
gatego_label.grid(row=1,column=0,sticky=tk.E+tk.W,padx=5,pady=5)

gatego_inp=tk.Listbox(root,height=1)
gatego_inp.grid(row=1,column=1,sticky=tk.E+tk.W,padx=5,pady=5)

for gategory in gategories:
    gatego_inp.insert(tk.END,gategory)
message=tk.Text(root)
message.grid(row=2,column=0,columnspan=2,sticky='news')

save_btn=tk.Button(root,text="save")
save_btn.grid(row=3,column=1,sticky=tk.E,padx=5,pady=5)



root.mainloop()