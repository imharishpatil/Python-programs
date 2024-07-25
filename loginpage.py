#program to create a login page in python
#USERNAME=system   PASSWORD=tiger
import tkinter as tk
import tkinter.messagebox as msgbox
form=tk.Tk()
form.geometry("1000x500")
lbluname=tk.Label(form,text="Username",font=("Arial",22,"bold"))
lbluname.grid(row=0,column=0)
etuname=tk.Entry(form,width=30,font=("Arial",22,'bold'))
etuname.grid(row=0,column=1)
lblpas=tk.Label(form,text="Password",font=("Arial",22,"bold"))
lblpas.grid(row=1,column=0)
etpas=tk.Entry(form,width=30,font=("Areal",22,"bold"))
etpas.grid(row=1,column=1)
def disp():
    u=etuname.get()
    p=etpas.get()
    if u=="system" and p=="tiger":
        msgbox.showinfo("Message","Loged in successfully...")
    else:
        msgbox.showinfo("Message","Invalid Username/Password...")
btnadd=tk.Button(form,text="Login",fg='red',font=("Areal",22,"bold"),command=disp)
btnadd.grid(row=2,column=1)
form.mainloop()