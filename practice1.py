from tkinter import *
import sqlite3

window = Tk()
window.geometry("400x200")


def login():
    print("")

    def login_database():
        pass

    window.destroy()
    # login window
    login_window = Tk()
    login_window.geometry("400x250")
    l1 = Label(login_window, text="User name", font="times 20")
    l1.grid(row=1, column=1)

    l2 = Label(login_window, text="User password", font="times 20")
    l2.grid(row=2, column=1)

    # login window input
    username_text = StringVar()
    e1 = Entry(login_window, textvariable=username_text)
    e1.grid(row=1, column=2)

    userpass_text = StringVar()
    e2 = Entry(login_window, textvariable=userpass_text)
    e2.grid(row=2, column=2)

    b1 = Button(login_window, text="Login", width=20)
    b1.grid(row=4, column=2)


def signup():
    print("")

    def signup_database():
        conn = sqlite3.connect("users.db")
        mycursor = conn.cursor()
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name text, email text, password text )")
        mycursor.execute("INSERT INTO test Values(Null, ?,?,?)",
                         (e1.get(), e2.get(), e3.get()))
        l4 = Label(signup_window, text="account created", font="times 15")
        l4.grid(row=6, column=2)
        conn.commit()
        conn.close()

    window.destroy()

    # signup window
    signup_window = Tk()
    signup_window.geometry("400x250")
    l1 = Label(signup_window, text="User name", font="times 20")
    l1.grid(row=1, column=1)

    l2 = Label(signup_window, text="User email", font="times 20")
    l2.grid(row=2, column=1)

    l3 = Label(signup_window, text="User password", font="times 20")
    l3.grid(row=3, column=1)

    # inputs and text
    name_text = StringVar()
    e1 = Entry(signup_window, textvariable=name_text)
    e1.grid(row=1, column=2)

    email_text = StringVar()
    e2 = Entry(signup_window, textvariable=email_text)
    e2.grid(row=2, column=2)

    password_text = StringVar()
    e3 = Entry(signup_window, textvariable=password_text)
    e3.grid(row=3, column=2)

    b1 = Button(signup_window, text="Sign up",
                width=20, command=signup_database)
    b1.grid(row=4, column=2)


# Principal window and options
l1 = Label(window, text="Welcome, Please chose one option", font="times 20")
l1.grid(row=1, column=2, columnspan=2)

b1 = Button(window, text="Log in", width=20, command=login)
b1.grid(row=2, column=2)

b2 = Button(window, text="Sign up", width=20, command=signup)
b2.grid(row=2, column=3)


window.mainloop()
