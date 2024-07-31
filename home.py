import tkinter as tk
import sqlite3 as sql
import tkinter.messagebox as msgbox

form = tk.Tk()
form.geometry("1000x500")
form.title("Login\t\t\t\t\tU15IG22S0306\tHarish Patil")

lblh = tk.Label(form, text="HOME PAGE", font=("Arial", 20, "bold"))
lblh.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

# Label and entry field for UUCMS
lbluucms = tk.Label(form, text="UUCMS No", font=("Arial", 22, "bold"))
lbluucms.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
etuucms = tk.Entry(form, width=30, font=("Arial", 22, 'bold'))
etuucms.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Label and entry field for Password
lblpas = tk.Label(form, text="Password", font=("Arial", 22, "bold"))
lblpas.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
etpas = tk.Entry(form, width=30, font=("Arial", 22, "bold"), show="*")
etpas.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

# Function to check valid credentials
def login():
    u = etuucms.get()
    p = etpas.get()
    # Connecting to the database
    con = sql.connect('ex.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE uucms=? AND password=?", (u, p))
    pas = cur.fetchone()
    con.close()
    if pas:
        msgbox.showinfo("Success", "Logged in successfully")
    else:
        msgbox.showerror("Error", "Invalid UUCMS/Password")

def register():
    from reg import disp  # Ensure the 'reg' module and 'disp' function exist

# Button for login
btnlog = tk.Button(form, text="Login", fg='red', font=("Arial", 22, "bold"), command=login)
btnlog.grid(row=3, column=1, padx=10, pady=5)

# Button to register
btnreg = tk.Button(form, text="Register", fg='red', font=("Arial", 22, "bold"), command=register)
btnreg.grid(row=3, column=2, columnspan=1, padx=10, pady=5)

form.mainloop()
