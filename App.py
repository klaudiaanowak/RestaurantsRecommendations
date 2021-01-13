import tkinter as tk
from tkinter import ttk 
from DataBaseManager import *
from RecommendationModelManager import *

LARGE_FONT= ("Verdana", 12)
MEDIUM_FONT= ("Verdana", 11)
SMALL_FONT= ("Verdana", 8)


class App(tk.Tk):
    def __init__(self, title="Aplikacja"):
        super().__init__() 
        self.title(title)  
        self.center()
        self.container = tk.Frame(master=self,
                    relief=tk.RAISED,
                    borderwidth=1)

        self.container.pack(side="top", fill="both", expand = True)
        self.container.columnconfigure(0, weight=1, minsize=200)
        self.container.rowconfigure(0, weight=1, minsize=200) 
        
        self.dbManager = DataBaseManager()
        self.recommendationManager = RecommendationModelManager()

        self.show_frame(LoginPage)


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

    def show_frame(self, cont,error=None,user=None):
        if error is not None:
            frame = cont(self.container, self,error=error)
        elif user is not None:
            frame = cont(self.container, self, user=user)
        else:
            frame = cont(self.container, self)
        
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller, user):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.restuarantsData = controller.dbManager.get_restuarant_data()

        label = tk.Label(self, text="Restaurant recommendations", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        tabControl = ttk.Notebook(self) 
  
        tab1 = ttk.Frame(tabControl) 
        tab2 = ttk.Frame(tabControl) 
        
        tabControl.add(tab1, text ='Recommendation list') 
        tabControl.add(tab2, text ='Add rating') 
        tabControl.pack(expand = 1, fill ="both") 
        userName  = controller.dbManager.get_user_name()
        self.fill_recommendations_tab(tab1, userName)
        ttk.Label(tab2, 
                text ="Add new rating").grid(column = 0, row = 0, padx = 10, pady = 10) 
                
    def get_recommendation_list_content(self):
        userModelID = self.controller.dbManager.get_user_modelID()
        recommendedData = self.controller.recommendationManager.get_recommendations(userModelID,self.restuarantsData)
        return self.controller.dbManager.get_recommended_restaurants(recommendedData)

    def fill_recommendations_tab(self,tab,userName, listLength=5):
        mainLabel = ttk.Label(tab, text ="Recommendation list of restaurants for you, {}".format(userName),font=MEDIUM_FONT).grid(column = 0,  row = 0, padx = 10, pady = 10, columnspan = 3)
        ttk.Label(tab, text ="Name", font=SMALL_FONT, justify=tk.CENTER).grid(column = 0, row = 1, padx = 0, pady = 2)
        ttk.Label(tab, text ="Category" ,font=SMALL_FONT, justify=tk.CENTER).grid(column = 1, row = 1, padx = 0, pady = 2)
        ttk.Label(tab, text ="Stars",font=SMALL_FONT, justify=tk.CENTER).grid(column = 2, row = 1, padx = 2, pady = 2)
        recommendationList = self.get_recommendation_list_content()
        listLength = listLength if len(recommendationList)>= listLength else len(recommendationList)
        for i in range(2, listLength+2):
            restaurant = recommendationList.iloc[i-1]
            ttk.Label(tab, text ="{}".format(restaurant['name']) ,font=SMALL_FONT, justify=tk.LEFT).grid(column = 0, row = i, padx = 0, pady = 2)
            ttk.Label(tab, text ="{}".format(restaurant['categories']) ,font=SMALL_FONT, justify=tk.LEFT).grid(column = 1, row = i, padx = 0, pady = 2)
            ttk.Label(tab, text ="{}".format(restaurant['stars']) ,font=SMALL_FONT, justify=tk.CENTER, relief=tk.RAISED).grid(column = 2, row = i, padx = 2, pady = 2) 



class LoginPage(tk.Frame):

    def __init__(self, parent, controller,error=None):
        self.controller = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Login Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label_login = tk.Label(self, text="Login: ").pack(pady=5,padx=5)

        login_input = tk.Entry(self) # input field
        login_input.pack(pady=5,padx=5)

        tk.Label(self, text="Password: ").pack(pady=5,padx=5)
        password_input = tk.Entry(self)
        password_input.pack(pady=5,padx=5)
        if(error is not None):
            error_label = tk.Label(self, text="Error: "+error, fg="red").pack(pady=5,padx=5)

        save_button = tk.Button(self, text="Login",
                    command=lambda: controller.show_frame(MainPage, user=login_input.get()) if self.verify_login_data(login_input.get(), password_input.get()) else controller.show_frame(LoginPage,error="Incorrect username or password"))
        save_button.pack()

    def verify_login_data(self, username, password):
        return self.controller.dbManager.login_user(username,password)
        

