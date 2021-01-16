import tkinter as tk
from tkinter import ttk 
from DataBaseManager import *
from RecommendationModelManager import *
import sys
import _thread as thread
from time import sleep
import queue
from utils import *


class App(tk.Tk):
    def __init__(self, title="Aplikacja"):
        super().__init__() 
        self.title(title)  
        self.geometry("200x210")
        self.center()
        self.container = tk.Frame(master=self,
                    relief=tk.RAISED,
                    borderwidth=1)
        tk.Label(self,text = 'Restaurants recommendations', bg = 'light blue', width = '300', height ='2', font = ('Calibri', 18)).pack(pady=5,padx=10)
        self.container.pack(side="top", fill="both", expand = True)
        self.container.columnconfigure(0, weight=1, minsize=200)
        self.container.rowconfigure(0, weight=1, minsize=200) 
        
        self.dbManager = DataBaseManager()
        self.recommendationManager = RecommendationModelManager()

        self.show_frame(WelcomePage)


    def run(self):
        self.mainloop()
    
    def center(self):
        self.update()
        wx = self.winfo_width()*2
        wy = self.winfo_height()*2
        sx = self.winfo_screenwidth()
        sy = self.winfo_screenheight()
        x = (sx - wx) // 2 
        y = (sy - wy) // 2 

        self.geometry("{}x{}+{}+{}".format(wx, wy, x, y))

    def show_frame(self, cont,error=None,user=None, information=None):
        if error is not None:
            frame = cont(self.container, self,error=error)
        elif user is not None:
            if information is not None:
                frame = cont(self.container, self, user=user, information=information)
            else:
                frame = cont(self.container, self, user=user)
        else:
            frame = cont(self.container, self)

        
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def close_app(self):
        sys.exit()

class WelcomePage(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        tk.Label(self,text = '').pack()
        tk.Button(self,text = 'Sign in', height = '2', width = '30', command = lambda: self.controller.show_frame(LoginPage)).pack()
        tk.Label(self,text = '').pack()
        tk.Button(self,text = 'Register', height = '2', width = '30', command = lambda: self.controller.show_frame(RegisterPage)).pack()
        tk.Label(self,text = '').pack()
        tk.Button(self,text = 'Exit', height = '2', width = '30', command = lambda: self.controller.close_app()).pack()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller,error=None):
        self.controller = controller
        tk.Frame.__init__(self,parent)
        tk.Label(self, text = 'Fill login data').pack(pady=2)
        tk.Label(self, text = '').pack()
        
        tk.Label(self, text = 'Login: ').pack()
        login_entry = tk.Entry(self, width = '30')
        login_entry.pack()
        tk.Label(self, text = '').pack()
        tk.Label(self, text = 'Password: ').pack()
        password_entry = tk.Entry(self, width = '30')
        password_entry.pack()
        tk.Label(self, text = '').pack()
        if(error is not None):
            tk.Label(self, text="Error: "+error, fg="red").pack(pady=5,padx=5)
        
        save_button = tk.Button(self, text = 'Login', height = '2', width = '30', command=lambda: self.login_user(login_entry.get(), password_entry.get()))
        save_button.pack()
        back_button = tk.Button(self, text = 'Back', height = '2', width = '30', command = self.go_back)
        back_button.pack(side='bottom')

    def login_user(self,userName,password):
        if self.verify_login_data(userName, password):
            if userName=='admin':
                self.controller.show_frame(AdminPage,user=userName)
            else:
                self.controller.show_frame(MainPage, user=userName)
        else:
            self.controller.show_frame(LoginPage,error="Incorrect username or password")


    def verify_login_data(self, username, password):
        return self.controller.dbManager.login_user(username,password)
    
    def go_back(self):
        self.controller.show_frame(WelcomePage)
        
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller, error=None):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        tk.Label(self, text = 'Fill up data').pack()
        tk.Label(self, text = '').pack()
        tk.Label(self, text = 'E-mail: ').pack()
        email_entry = tk.Entry(self)
        email_entry.pack()
        tk.Label(self, text = 'Name: ').pack()
        name_entry = tk.Entry(self)
        name_entry.pack()
        tk.Label(self, text = 'Login: ').pack()
        login_entry = tk.Entry(self)
        login_entry.pack()
        tk.Label(self, text = 'Password: ').pack()
        password_entry = tk.Entry(self)
        password_entry.pack()
        tk.Label(self, text = 'Telephon number: ').pack()
        tel_entry = tk.Entry(self)
        tel_entry.pack()
        tk.Label(self, text = '').pack()
        if(error is not None):
            tk.Label(self, text="Error: "+error, fg="red").pack()

        tk.Button(self, text = 'Register', width = 10, height = 1, command=lambda: self.controller.show_frame(SuccessfulRegistrationPage) 
                                                                                if self.register_user(login_entry.get(), password_entry.get(), name_entry.get(), email_entry.get(), tel_entry.get()) 
                                                                                else self.controller.show_frame(RegisterPage,error="Incorrect data. Try again")).pack()
        tk.Button(self, text = 'Back', height = 1, width = 10, command = self.go_back).pack(side='bottom')


 
    def register_user(self,userName,password, name, email, tel):
        return self.controller.dbManager.register_user(userName,password, name, email, tel)

    def go_back(self):
        self.controller.show_frame(WelcomePage)

class SuccessfulRegistrationPage(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
        self.controller = controller  
        tk.Label(self, text = 'Your account is created successfully!', fg='green', font=('Calibri, 11')).pack()
        tk.Label(self, text = '').pack()
        tk.Button(self, text = 'Back', width = 10, height = 1, command = self.go_back).pack(side='bottom')

    def go_back(self):
        self.controller.show_frame(WelcomePage)  
        
class MainPage(tk.Frame):
    def __init__(self, parent, controller,user):        
        tk.Frame.__init__(self,parent)
        self.controller = controller
        userName  = controller.dbManager.get_user_name()
        tk.Label(self, text = 'Welcome {}!'.format(userName), fg='black', font=('Calibri, 11')).pack(pady=20)
        tk.Label(self, text = '').pack()
        tk.Button(self, text = 'Check restaurants recommendations', height = '2', width = '30', command= lambda: self.controller.show_frame(RecommendationListPage,user=userName)).pack()
        tk.Label(self, text = '').pack()
        tk.Button(self, text = 'Add rating', height = '2', width = '30', command = lambda: self.controller.show_frame(AddRatingPage,user=userName)).pack()
        tk.Label(self, text = '').pack()
        tk.Button(self, text = 'Logout', height = '2', width = '30', command = self.go_back).pack()

    def go_back(self):
       self.controller.show_frame(WelcomePage)  

class RecommendationListPage(tk.Frame):
    def __init__(self, parent, controller, user):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.user = user
        self.restuarantsData = controller.dbManager.get_restuarant_data()   
        self.fill_recommendations_tab( user)
        tk.Button(self, text = 'Back', height = '2', width = '30', command = self.go_back).pack(side='bottom')

    def get_recommendation_list_content(self):
        userModelID = self.controller.dbManager.get_user_modelID()
        recommendedData = self.controller.recommendationManager.get_recommendations(userModelID,self.restuarantsData)
        return self.controller.dbManager.get_recommended_restaurants(recommendedData)

    def fill_recommendations_tab(self,userName, listLength=5):
        newFrame = tk.Frame(self)
        newFrame.pack()
        ttk.Label(newFrame, text ="Recommendation list of restaurants for you, {}".format(userName),font=MEDIUM_FONT).grid(column = 0,  row = 0, padx = 10, pady = 10, columnspan = 3)
        ttk.Label(newFrame, text ="Name", font=SMALL_FONT, justify=tk.CENTER).grid(column = 0, row = 1, padx = 0, pady = 2)
        ttk.Label(newFrame, text ="Category" ,font=SMALL_FONT, justify=tk.CENTER).grid(column = 1, row = 1, padx = 0, pady = 2)
        ttk.Label(newFrame, text ="Stars",font=SMALL_FONT, justify=tk.CENTER).grid(column = 2, row = 1, padx = 2, pady = 2)
        recommendationList = self.get_recommendation_list_content()
        listLength = listLength if len(recommendationList)>= listLength else len(recommendationList)
        for i in range(2, listLength+2):
            restaurant = recommendationList.iloc[i-1]
            ttk.Label(newFrame, text ="{}".format(restaurant['name']) ,font=SMALL_FONT, justify=tk.LEFT).grid(column = 0, row = i, padx = 0, pady = 2)
            ttk.Label(newFrame, text ="{}".format(restaurant['categories']) ,font=SMALL_FONT, justify=tk.LEFT).grid(column = 1, row = i, padx = 0, pady = 2)
            ttk.Label(newFrame, text ="{}".format(restaurant['stars']) ,font=SMALL_FONT, justify=tk.CENTER, relief=tk.RAISED).grid(column = 2, row = i, padx = 2, pady = 2) 
    
    def go_back(self):
       self.controller.show_frame(MainPage,user=self.user)       



class AddRatingPage(tk.Frame):
    def __init__(self, parent, controller, user):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.user = user
        back_button = tk.Button(self, text = 'Back', height = '2', width = '30', command = self.go_back)
        back_button.pack(side='bottom')
    def go_back(self):
       self.controller.show_frame(MainPage,user=self.user)       


class AdminPage(tk.Frame):
    def __init__(self, parent, controller, user, error=None, information=None):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.user = user
        tk.Label(self, text ="Administration Page",font=MEDIUM_FONT).pack()
        update_model_button = tk.Button(self, text = 'Update model', height = '2', width = '30', command = self.update_recommendation_model)
        update_model_button.pack(pady=20)
        if(error is not None):
            tk.Label(self, text="Error: "+error, fg="red").pack()
        if(information is not None):
            tk.Label(self, text=information, bg='white', fg="green").pack()
        back_button = tk.Button(self, text = 'Back', height = '2', width = '30', command = self.go_back)
        back_button.pack(side='bottom')

    def go_back(self):
       self.controller.show_frame(WelcomePage)       
    
    def update_recommendation_model(self):
        if(self.controller.recommendationManager.update_model()):
            self.controller.show_frame(AdminPage,user=self.user, information="Model successfully updated")
        else: 
            self.controller.show_frame(AdminPage,user=self.user, error="Error during model updating")




