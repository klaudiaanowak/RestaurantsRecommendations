import tkinter as tk
from tkinter import ttk 

LARGE_FONT= ("Verdana", 12)

class App(tk.Tk):
    def __init__(self, title="Aplikacja"):
        super().__init__() 
        self.title(title)  
        self.center()
        self.container = tk.Frame(master=self,
                    relief=tk.RAISED,
                    borderwidth=1)

        self.container.pack(side="top", fill="both", expand = True)
        self.container.columnconfigure(0, weight=1, minsize=100)
        self.container.rowconfigure(0, weight=1, minsize=100) 

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
    def show_frame(self, cont,error=None):
        if error is not None:
            frame = cont(self.container, self,error=error)
            print("I am here: err ",error)

        else:
            frame = cont(self.container, self)
            print("I am here:")
        
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Restaurant recommendations", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        tabControl = ttk.Notebook(self) 
  
        tab1 = ttk.Frame(tabControl) 
        tab2 = ttk.Frame(tabControl) 
        
        tabControl.add(tab1, text ='Recommendation list') 
        tabControl.add(tab2, text ='Add rating') 
        tabControl.pack(expand = 1, fill ="both") 
        
        ttk.Label(tab1,  
                text ="Recommendation list of restaurants").grid(column = 0,  
                                    row = 0, 
                                    padx = 10, 
                                    pady = 10)   
        ttk.Label(tab2, 
                text ="Add new rating").grid(column = 0, 
                                            row = 0,  
                                            padx = 10, 
                                            pady = 10) 

class LoginPage(tk.Frame):

    def __init__(self, parent, controller,error=None):
        print("ERror: ",error)
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
                    command=lambda: controller.show_frame(MainPage) if self.verify_login_data(login_input.get(), password_input.get()) else controller.show_frame(LoginPage,error="Incorrect username or password"))
        save_button.pack()

    def verify_login_data(self, username, password):
        return True

