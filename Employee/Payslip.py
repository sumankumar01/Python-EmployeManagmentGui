import tkinter
from functools import partial


class paymentSlip:


    def __init__(self,new_window,mainwindow):
        self.new_window=new_window
        self.mainwindow=mainwindow

    def slip(self):
        self.new_window.withdraw()
        payslipWindow = tkinter.Toplevel(self.new_window)

        payslipWindow.deiconify()
        payslipWindow.maxsize(width=500, height=600)
        payslipWindow.minsize(width=500, height=600)



        loginPage1 = partial(self.loginPage, payslipWindow, self.mainwindow)
        home = tkinter.Button(payslipWindow, text="Login",
                              width=5, fg='#FFC331', relief="raised",
                              command=loginPage1).place(x=10, y=20)

        pay = partial(self.payslipPage, payslipWindow, self.new_window)
        home = tkinter.Button(payslipWindow, text="Home",
                              width=5, fg='#FFC331', relief="raised",
                              command=pay).place(x=60, y=20)

    def loginPage(self,payslipWindow,mainwindow):


        payslipWindow.withdraw()
        mainwindow.deiconify()

    def payslipPage(self,payslipWindow,new_window):


        payslipWindow.withdraw()
        new_window.deiconify()
