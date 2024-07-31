import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

# Connecting to the database
con = sql.connect('ex.db')
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        uucms VARCHAR(12) PRIMARY KEY,
        name VARCHAR(20),
        gender VARCHAR(7),
        course VARCHAR(5),
        sem VARCHAR(4),
        password VARCHAR(8)
    )
""")

form2 = tk.Tk()
form2.title("Registration\t\t\t\t\tU15IG22S0306\tHarish Patil")
form2.geometry("1500x750")

# Heading
lblh = tk.Label(form2, text="REGISTRATION", font=("Arial", 20, "bold"))
lblh.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="n")

# Frame for entry fields and buttons
entry_frame = tk.Frame(form2)
entry_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

# Configure grid in the entry frame to center-align widgets
entry_frame.columnconfigure(0, weight=1)
entry_frame.columnconfigure(1, weight=2)

# Label and entry field for the UUCMS number
lbluno = tk.Label(entry_frame, text="UUCMS", font=("Arial", 13, "bold"))
etuno = tk.Entry(entry_frame, width=30, font=("Arial", 13))
lbluno.grid(row=0, column=0, padx=10, pady=5, sticky="e")
etuno.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Label and entry field for the student name
lblname = tk.Label(entry_frame, text="Name", font=("Arial", 13, "bold"))
etname = tk.Entry(entry_frame, width=30, font=("Arial", 13))
lblname.grid(row=1, column=0, padx=10, pady=5, sticky="e")
etname.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Label and menu list to select the course
lblcrs = tk.Label(entry_frame, text="Course", font=("Arial", 13, "bold"))
crs = tk.StringVar(entry_frame)
crs.set("Select")
menucrs = tk.OptionMenu(entry_frame, crs, "BA", "BCOM", "BSC", "BCA", "BBA")
lblcrs.grid(row=2, column=0, padx=10, pady=5, sticky="e")
menucrs.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Label and menu list to select the semester
lblsem = tk.Label(entry_frame, text="Semester", font=("Arial", 13, "bold"))
sem = tk.StringVar(entry_frame)
sem.set("Select")
menusem = tk.OptionMenu(entry_frame, sem, "I", "II", "III", "IV", "V", "VI")
lblsem.grid(row=3, column=0, padx=10, pady=5, sticky="e")
menusem.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Label and entry field for password
lblpas = tk.Label(entry_frame, text="Password", font=("Arial", 13, "bold"))
etpas = tk.Entry(entry_frame, width=30, font=("Arial", 13), show='*')
lblpas.grid(row=4, column=0, padx=10, pady=5, sticky="e")
etpas.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Label and radio buttons for gender
lblgen = tk.Label(entry_frame, text="Gender", font=("Arial", 13, "bold"))
gendervar = tk.StringVar()
gendervar.set(None)
rbmale = tk.Radiobutton(entry_frame, text="Male", value="male", font=("Arial", 10, "bold"), variable=gendervar)
rbfemale = tk.Radiobutton(entry_frame, text="Female", value="female", font=("Arial", 10, "bold"), variable=gendervar)
lblgen.grid(row=5, column=0, padx=10, pady=5, sticky="e")
rbmale.grid(row=5, column=1, padx=5, pady=5, sticky="w")
rbfemale.grid(row=5, column=1, padx=70, pady=5, sticky="w")

# Buttons for save and display
btnsave = tk.Button(form2, text="Save", fg='red', font=("Arial", 13, "bold"), command=lambda: save())
btnsave.grid(row=6, column=0, padx=10, pady=5, sticky="e")

btndisp = tk.Button(form2, text="Display", fg='red', font=("Arial", 13, "bold"), command=lambda: disp())
btndisp.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Frame for Treeview
tree_frame = tk.Frame(form2)
tree_frame.grid(row=7, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

def save():
    uucms = etuno.get()
    name = etname.get()
    gender = gendervar.get()
    course = crs.get()
    semester = sem.get()
    password = etpas.get()
    
    if uucms and name and gender and course != "Select" and semester != "Select" and password:
        try:
            cur.execute("INSERT INTO student (uucms, name, gender, course, sem, password) VALUES (?, ?, ?, ?, ?, ?)",
                        (uucms, name, gender, course, semester, password))
            con.commit()
            messagebox.showinfo("Success", "Data saved")
        except sql.IntegrityError:
            messagebox.showerror("Error", "UUCMS number already exists")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields correctly")

def disp():
    # Clear the previous TreeView content
    for widget in tree_frame.winfo_children():
        widget.destroy()

    # Create the TreeView
    t = ttk.Treeview(tree_frame, columns=("UUCMS", "name", "gender", "course", "semester", "password"), show="headings")
    t.heading("UUCMS", text="UUCMS NO")
    t.heading("name", text="NAME")
    t.heading("gender", text="GENDER")
    t.heading("course", text="COURSE")
    t.heading("semester", text="SEMESTER")
    t.heading("password", text="PASSWORD")
    t.column("UUCMS", anchor="center")
    t.column("name", anchor="center")
    t.column("gender", anchor="center")
    t.column("course", anchor="center")
    t.column("semester", anchor="center")
    t.column("password", anchor="center")
    t.pack(fill=tk.BOTH, expand=True)

    # Fetch data from the database
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    for row in rows:
        t.insert("", "end", values=row)

# Configure the grid row and column weights
form2.grid_rowconfigure(7, weight=1)
form2.grid_columnconfigure(0, weight=1)
form2.grid_columnconfigure(1, weight=1)

form2.mainloop()

# Close the connection
con.close()
