import tkinter
from functools import partial
from tkinter import messagebox, ttk, END
from PIL import Image, ImageTk

from Employee.Database import Db
from Employee.EmpMangmentHome import employeeManagmentHomePage


class LoginClass:

    def validateLogin(self,mainwindow,username, password):

        login_username=Db(username.get(),password.get())
        status,record=login_username.logindb()
        print('{} ---->{}'.format(username.get(),password.get()))
        if username.get() == "":
            messagebox.showinfo("Login System", "Please enter the Username")
        elif password.get() == "":
            messagebox.showinfo("Login System", "Please enter the Password")
        elif username.get() == "" and password.get() == "":
            messagebox.showinfo("Login System", "Please enter the Username and Password")
        elif username.get() == str(record[0]) and password.get() == record[1] and status==1:
            mainwindow.withdraw()
            password.set("")
            new_window = tkinter.Toplevel(mainwindow)



            #new_window.withdraw()
            #new_window.destroy()
            b=employeeManagmentHomePage()
            b.home_page1(new_window,mainwindow)
            #mainwindow.deiconify()









        else:
            messagebox.showinfo("Login System", "Please enter the correct Username and Password")
        return

    def switch(self,mainwindow,winsignup):
        #winsignup.destroy()
        winsignup.withdraw()
        #new_window = tkinter.Toplevel(mainwindow)
        # new_window.destroy()
        #tkinter.Toplevel(self.mainwindow)
        #new_window.withdraw()
        mainwindow.deiconify()

        # clear data function
    def SignUp(self, mainwindow):
        def action():
            if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or add.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
            elif password.get() != very_pass.get():
                messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
            else:
                login_username = Db(user_name.get(), '')
                status = login_username.validateUser()
                print(status)
                try:

                    if status != -1:
                        messagebox.showerror("Error", "User Name Already Exits", parent=winsignup)
                    else:
                        row, record = login_username.register(first_name.get(),last_name.get(),user_name.get(),city.get(),var.get(),age.get(),password.get())

                        messagebox.showinfo("Success", "Ragistration Successfull", parent=mainwindow)
                        clear()
                        self.switch()

                except Exception as es:
                    messagebox.showerror("Error", f"Error Du to : {str(es)}", parent=winsignup)




        def clear():
            first_name.delete(0, END)
            last_name.delete(0, END)
            age.delete(0, END)
            var.set("Male")
            city.delete(0, END)
            add.delete(0, END)
            user_name.delete(0, END)
            password.delete(0, END)
            very_pass.delete(0, END)

        mainwindow.withdraw()
        winsignup = tkinter.Tk()

        winsignup.title("Docter Appointment App")
        winsignup.maxsize(width=500, height=600)
        winsignup.minsize(width=500, height=600)

        # heading label
        heading = tkinter.Label(winsignup, text="Signup", font='Verdana 20 bold')
        heading.place(x=80, y=60)

        # form data label
        first_name = tkinter.Label(winsignup, text="First Name :", font='Verdana 10 bold')
        first_name.place(x=80, y=130)

        last_name = tkinter.Label(winsignup, text="Last Name :", font='Verdana 10 bold')
        last_name.place(x=80, y=160)

        age = tkinter.Label(winsignup, text="Age :", font='Verdana 10 bold')
        age.place(x=80, y=190)

        Gender = tkinter.Label(winsignup, text="Gender :", font='Verdana 10 bold')
        Gender.place(x=80, y=220)

        city = tkinter.Label(winsignup, text="City :", font='Verdana 10 bold')
        city.place(x=80, y=260)

        add = tkinter.Label(winsignup, text="Address :", font='Verdana 10 bold')
        add.place(x=80, y=290)

        user_name = tkinter.Label(winsignup, text="User Name :", font='Verdana 10 bold')
        user_name.place(x=80, y=320)

        password = tkinter.Label(winsignup, text="Password :", font='Verdana 10 bold')
        password.place(x=80, y=350)

        very_pass = tkinter.Label(winsignup, text="Verify Password:", font='Verdana 10 bold')
        very_pass.place(x=80, y=380)

        # Entry Box ------------------------------------------------------------------

        first_name = tkinter.StringVar()
        last_name = tkinter.StringVar()
        age = tkinter.IntVar(winsignup, value='0')
        var = tkinter.StringVar()
        city = tkinter.StringVar()
        add = tkinter.StringVar()
        user_name = tkinter.StringVar()
        password = tkinter.StringVar()
        very_pass = tkinter.StringVar()

        first_name = tkinter.Entry(winsignup, width=40, textvariable=first_name)
        first_name.place(x=200, y=133)

        last_name = tkinter.Entry(winsignup, width=40, textvariable=last_name)
        last_name.place(x=200, y=163)

        age = tkinter.Entry(winsignup, width=40, textvariable=age)
        age.place(x=200, y=193)

        Radio_button_male = ttk.Radiobutton(winsignup, text='Male', value="Male", variable=var).place(x=200, y=220)
        Radio_button_female = ttk.Radiobutton(winsignup, text='Female', value="Female", variable=var).place(x=200,
                                                                                                            y=238)

        city = tkinter.Entry(winsignup, width=40, textvariable=city)
        city.place(x=200, y=263)

        add = tkinter.Entry(winsignup, width=40, textvariable=add)
        add.place(x=200, y=293)

        user_name = tkinter.Entry(winsignup, width=40, textvariable=user_name)
        user_name.place(x=200, y=323)

        password = tkinter.Entry(winsignup, width=40, textvariable=password)
        password.place(x=200, y=353)

        very_pass = tkinter.Entry(winsignup, width=40, show="*", textvariable=very_pass)
        very_pass.place(x=200, y=383)

        # button login and clear

        #action1 = partial(self.action, winsignup)

        btn_signup = tkinter.Button(winsignup, text="Signup", font='Verdana 10 bold', command=action)
        btn_signup.place(x=200, y=413)

        #clear1 = partial(self.clear, winsignup)

        btn_login = tkinter.Button(winsignup, text="Clear", font='Verdana 10 bold', command=clear)
        btn_login.place(x=280, y=413)

        switch1 = partial(self.switch,mainwindow,winsignup)

        sign_up_btn = tkinter.Button(winsignup, text="Switch To Login", command=switch1)
        sign_up_btn.place(x=350, y=20)

        winsignup.mainloop()





    def mainscreen(self):
        mainwindow = tkinter.Tk()

        mainwindow.title("Login to payroll management system")
        mainwindow.geometry('640x480+40+100')
        mainwindow.configure(background='grey')
        img = ImageTk.PhotoImage(Image.open("C://Users//kumar//Downloads//loginimage.JPG"))

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tkinter.Label(mainwindow, image=img)
        panel.place(x=0, y=0)
        # The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side='left', fill=tkinter.Y, expand=True)


        tkinter.Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        tkinter.Label(text="").pack()
        rightframe = tkinter.Frame(mainwindow)
        rightframe.pack(side='top')
        tkinter.Label(rightframe,text="Enter Username", bg="red", width="20").pack()
        tkinter.Label(rightframe, text="").pack()
        username=tkinter.StringVar()
        tkinter.Entry(rightframe, textvariable=username, width="20").pack(ipady=3)

        tkinter.Label(rightframe, text="").pack()

        tkinter.Label(rightframe,text="Enter Password", bg="red",  width="20").pack(ipady=3)
        tkinter.Label(rightframe, text="").pack()
        password = tkinter.StringVar()
        bullet = "\u2022"
        tkinter.Entry(rightframe, textvariable=password,show=bullet, width="20").pack()
        tkinter.Label(rightframe, text="").pack()
        # create Login Button
        validateLogin = partial(self.validateLogin,mainwindow,username, password)
        tkinter.Button(rightframe,text="login",
               width=20, fg='#FFC331', relief="raised", command=validateLogin).pack()
        # create a register button
        SignUp1 = partial(self.SignUp, mainwindow)
        tkinter.Button(rightframe,text="Register",
               width=20, fg='#FFC331', relief="raised", command=SignUp1).pack()


        mainwindow.mainloop()





if __name__ == '__main__':
     login=LoginClass()
     login.mainscreen()
