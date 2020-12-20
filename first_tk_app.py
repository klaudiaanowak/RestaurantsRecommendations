from App import *


app = App("Restaurants recommendations")
app.columnconfigure(0, weight=1, minsize=100)
app.rowconfigure(0, weight=1, minsize=100)

ramka = tk.Frame(master=app,
            relief=tk.RAISED,
            borderwidth=1)
ramka.grid(row=0,column=0)


label_login = tk.Label(ramka, text="Login: ").grid(row=0, column=0, sticky="nsew")

login_input = tk.Entry(ramka) # input field
login_input.grid(row=0, column=1, sticky="nsew")

tk.Label(ramka, text="Password: ").grid(row=1, column=0, sticky="nsew")
password_input = tk.Entry(ramka)
password_input.grid(row=1, column=1, sticky="nsew")

save_button = tk.Button(ramka, text="Login",
                    command=lambda: print(login_input.get()+" "+ password_input.get()))
            
save_button.grid(row=3, column=1, sticky="nsew")

app.run()