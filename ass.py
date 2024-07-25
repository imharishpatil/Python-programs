import tkinter as tk
import tkinter.messagebox as msgbox
impo
form=tk.Tk()
form.state("zoomed")
form.title("harish's window")
form.configure(bg="#393e46")
lbluname=tk.Label(form,text="Username",fg="#eeeeee",bg="#393e46",font=("Arial",22,"bold"))
lbluname.place(relx=0.3,rely=0.27)
etuname=tk.Entry(form,width=30,fg="#eeeeee",bg="#222831",font=("Arial",22,'bold'))
etuname.place(relx=0.3,rely=0.32)
lblpas=tk.Label(form,text="Password",fg="#eeeeee",bg="#393e46",font=("Arial",22,"bold"))
lblpas.place(relx=0.3,rely=0.4)
etpas=tk.Entry(form,width=30,fg="#eeeeee",bg="#222831",font=("Areal",22,"bold"))
etpas.place(relx=0.3,rely=0.45)
def disp():
    u=etuname.get()
    p=etpas.get()
    if u=="system" and p=="tiger":
        msgbox.showinfo("Message","Loged in successfully...")
    else:
        msgbox.showinfo("Message","Invalid Username/Password...")
btnadd=tk.Button(form,text="Login",bg='#00adb5',fg="#eeeeee",font=("Areal",22,"bold"),command=disp)
btnadd.place(relx=0.45,rely=0.6)
form.mainloop()