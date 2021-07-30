import tkinter
from functools import partial
from tkinter import ttk

from Employee.Payslip import paymentSlip


class employeeManagmentHomePage:

    def home_page1(self,new_window,mainwindow):
        mainwindow.withdraw()
        new_window.deiconify()
        new_window.configure(background='yellow')
        new_window.maxsize(width=500, height=600)
        new_window.minsize(width=500, height=600)


        tkinter.Label(new_window, text="FirstName * ",borderwidth=5).place(x=20,y=40)
        tkinter.Label(new_window, text="Suman", borderwidth=5).place(x=150, y=40)
        tkinter.Label(new_window, text="LastName * ",  borderwidth=5).place(x=20, y=80)
        tkinter.Label(new_window, text="Kumar * ",  borderwidth=5).place(x=150, y=80)
        tkinter.Label(new_window, text="EMPID * ",  borderwidth=5).place(x=20, y=120)
        tkinter.Label(new_window, text="115689 * ",  borderwidth=5).place(x=150, y=120)
        tkinter.Label(new_window, text="City * ",  borderwidth=5).place(x=20, y=160)
        tkinter.Label(new_window, text="Bnaglore * ",  borderwidth=5).place(x=150, y=160)
        tkinter.Label(new_window, text="Country * ",  borderwidth=5).place(x=20, y=200)
        tkinter.Label(new_window, text="India * ",  borderwidth=5).place(x=150, y=200)
        tkinter.Label(new_window, text="Gender * ",  borderwidth=5).place(x=20, y=240)
        tkinter.Label(new_window, text="Male * ",  borderwidth=5).place(x=150, y=240)
        tkinter.Label(new_window, text="age * ", borderwidth=5).place(x=20, y=280)
        tkinter.Label(new_window, text="24 * ", borderwidth=5).place(x=150, y=280)


       # username = tkinter.StringVar()
        #tkinter.Entry(new_window, textvariable=username,relief="raised",borderwidth=5).place(x=120,y=42)



        #tkinter.Label(new_window, text="Enter Password").place(x=20,y=80)

        #password = tkinter.StringVar()
        #bullet = "\u2022"
        #tkinter.Entry(new_window, textvariable=password, show=bullet).place(x=120,y=82)

        loginPage1 = partial(self.loginPage, new_window, mainwindow)
        home = tkinter.Button(new_window, text="Login",
                              width=20, fg='#FFC331', relief="raised",
                              command=loginPage1).pack()
        b = paymentSlip(new_window,mainwindow)

        Payslip1 = partial(b.slip)
        tkinter.Button(new_window, text="Payslip",
                       width=20, fg='#FFC331', relief="raised",
                       command=Payslip1).place(x=20, y=320)


        tkinter.Button(new_window, text="Job Profile",
                       width=20, fg='#FFC331', relief="raised",
                       command=loginPage1).place(x=20, y=360)

        tkinter.Button(new_window, text="Performance",
                       width=20, fg='#FFC331', relief="raised",
                       command=loginPage1).place(x=20, y=400)

        tkinter.Button(new_window, text="Attendence",
                       width=20, fg='#FFC331', relief="raised",
                       command=loginPage1).place(x=20, y=440)









    def loginPage(self,new_window,mainwindow):


        new_window.withdraw()
        mainwindow.deiconify()



