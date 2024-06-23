# majdooron ko bulawa
from tkinter import *


class Gui(Tk):
    def __init__(self, x, y, title, u="A", p="I"):
        super().__init__()
        self.geometry(f"{x}x{y}")
        self.title(title)
        self.font1 = "ComicSansMS 10 italic"
        self.u = u
        self.p = p
        self.var=""

    def pg1(self):
        def login():
            if username.get() == self.u:
                if password.get() == self.p:
                    f.forget()
                    return self.pg2()
                else:
                    print("Password is wrong.")
            else:
                print("Username is wrong.")

        self.title("Home")
        username = StringVar()
        password = StringVar()
        f = Frame(self, bg="white", relief=SUNKEN, padx=10, pady=10, borderwidth=2)
        f.pack(side=LEFT, anchor="nw")
        l1 = Label(f, text="User name:", font=self.font1)
        l1.pack(anchor="w", pady=10)
        e1 = Entry(self, textvariable=username, borderwidth=2)
        e1.pack(after=l1)
        l2 = Label(f, text="Password:", font=self.font1)
        l2.pack(anchor="w", pady=10)
        e2 = Entry(self, textvariable=password, borderwidth=2)
        e2.pack(after=l2)
        b1 = Button(f, text="Login", font=self.font1, command=login)
        b1.pack(anchor="w", padx=2, pady=10)
        return login()

    def sidebar(self):
        f = Frame(self, bg="white", relief=SUNKEN, width=25, borderwidth=2)
        f.pack(side=LEFT, fill=Y)
        l1 = Label(f, text='''Hello there. 
This application can be used to 
analyse your test scores over 
a period of time.''', font=self.font1, bg="white", width=25)
        l1.pack()

    def pg2(self):
        def a():
            self.var = "insert"

        def b():
            self.var = "read"

        def c():
            self.var = "update"

        def d():
            self.var = "graph"

        f = Frame(self, bg="white", relief=SUNKEN, padx=10, pady=10, borderwidth=2)
        f.pack(side=LEFT, anchor="nw")
        l1 = Label(f, text=f"To insert data:", font=self.font1)
        l1.pack(anchor="n", pady=10)
        b1 = Button(f, text="Insert", font=self.font1, command=a)
        b1.pack(anchor="n", padx=2, pady=10, after=l1)
        l2 = Label(f, text=f"To read data:", font=self.font1)
        l2.pack(anchor="n", pady=10)
        b2 = Button(f, text="Read", font=self.font1, command=b)
        b2.pack(anchor="n", padx=2, pady=10, after=l2)
        l3 = Label(f, text=f"To update data:", font=self.font1)
        l3.pack(anchor="n", pady=10)
        b3 = Button(f, text="Update", font=self.font1, command=c)
        b3.pack(anchor="n", padx=2, pady=10, after=l3)
        l4 = Label(f, text=f"To see graph:", font=self.font1)
        l4.pack(anchor="n", pady=10)
        b4 = Button(f, text="Graph", font=self.font1, command=d)
        b4.pack(anchor="n", padx=2, pady=10, after=l4)
        print(self.var)
        return self.var

    def func(self, todo):
        if todo == "insert":
            self.pg3()
        elif todo == "read":
            self.pg4()
        elif todo == "update":
            self.pg5()

        return todo

    def pg3(self):
        pass

    def pg4(self):
        pass

    def pg5(self):
        pass
