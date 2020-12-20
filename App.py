import tkinter as tk

class App(tk.Tk):
    # App dziedziczy z tkinter.Tk
    def __init__(self, title="Aplikacja"):
        super().__init__() # konstruktor Tk
        self.title(title)  # ustaw tytuł
        self.center()


    def run(self):
        self.mainloop()
    
    def center(self):
        self.update()
        # szerokość / wysokość okna
        wx = self.winfo_width()*2
        wy = self.winfo_height()*2
        # szerokość wysokość ekranu
        sx = self.winfo_screenwidth()
        sy = self.winfo_screenheight()
        # środek ekranu przesunięty o 
        x = (sx - wx) // 2 # połowę szerokośi
        y = (sy - wy) // 2 # połowę wysokości

        self.geometry("{}x{}+{}+{}".format(wx, wy, x, y))


class Ramka(tk.Frame):
    # dodajemy argument kluczowy side
    def __init__(self, parent, color="white", side=tk.TOP):
        tk.Frame.__init__(self, parent, background=color)   
        self.pack(fill=tk.BOTH, expand=True, side=side)

    def change_color(self, color="white"):
        # Frame.config umożliwia zmianę parametrów
        self.config(bg=color) # bg = background