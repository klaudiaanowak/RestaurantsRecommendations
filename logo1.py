from tkinter import *
import sys
import sqlite3
from tkinter import messagebox as ms
import random



def koniec():
    sys.exit()
def register_user():

    conn = sqlite3.connect('RecommendationsDB.db')
    c = conn.cursor()

    c.execute('INSERT INTO  users (user_id, name, review_count, stars, haslo, email, telefon) VALUES(?,?,?,?,?,?,?)',(login.get(), imie.get(), '0', '0', haslo.get(), email.get(), tel.get()))

    conn.commit() 
    conn.close()

    login_entry.delete(0, END)
    haslo_entry.delete(0, END)
    email_entry.delete(0, END)
    tel_entry.delete(0, END)
    imie_entry.delete(0, END)

    screen1.destroy()
    global screen7
    screen7 = Tk()
    screen7.title('Rejestracja')
    screen7.geometry('200x200')
    Label(screen7, text = 'Zostałeś zarejestrowany!', fg='green', font=('Calibri, 11')).pack()
    Label(screen7, text = '').pack()
    Button(screen7, text = 'Dalej', width = 10, height = 1, command = logowanie).pack()


def rejestracja():
    screen.destroy()
    global screen1
    screen1 = Tk()
    screen1.title('Rejestracja')
    screen1.geometry('400x400')

    global login
    global haslo
    global email
    global tel
    global imie
    global login_entry
    global haslo_entry
    global email_entry
    global tel_entry
    global imie_entry

    email = StringVar()
    login = StringVar()
    haslo = StringVar()
    tel = StringVar()
    imie = StringVar()


    Label(screen1, text = 'Uzupełnij dane ponizej').pack()
    Label(screen1, text = '').pack()
    Label(screen1, text = 'E-mail: ').pack()
    email_entry = Entry(screen1, textvariable = email)
    email_entry.pack()
    Label(screen1, text = 'Imię: ').pack()
    imie_entry = Entry(screen1, textvariable = imie)
    imie_entry.pack()
    Label(screen1, text = 'Login: ').pack()
    login_entry = Entry(screen1, textvariable = login)
    login_entry.pack()
    Label(screen1, text = 'Hasło: ').pack()
    haslo_entry = Entry(screen1, textvariable = haslo)
    haslo_entry.pack()
    Label(screen1, text = 'Telefon: ').pack()
    tel_entry = Entry(screen1, textvariable = tel)
    tel_entry.pack()
    Label(screen1, text = '').pack()
    Button(screen1, text = 'Zarejestruj się', width = 10, height = 1, command = register_user).pack()
    Button(screen1, text = 'Wyjście', height = '1', width = '10', command = koniec).pack()

def udanelogowanie():
    screen7.destroy()
    global screen3
    screen3 = Tk()
    screen3.title('Logowanie')
    screen3.geometry('400x400')

    Label(screen3, text = 'Jesteś zalogowany!', fg='green', font=('Calibri, 11')).pack()
    Label(screen3, text = '').pack()
    Button(screen3, text = 'Sprawdź rekomendacje restauracji', height = '2', width = '30').pack()
    Label(screen3, text = '').pack()
    Button(screen3, text = 'Dodaj opinie o restauracji', height = '2', width = '30', command = wybor).pack()
    Label(screen3, text = '').pack()
    Button(screen3, text = 'Wyjście', height = '2', width = '30', command = koniec).pack()

def wybierz():
    global my_listbox
    clicked_items = my_listbox.curselecion()
    for item in clicked_items:
        Label(screen9, textvariable = my_listbox.get(item))


def wybor():
    screen11.destroy()
    global screen9
    screen9 = Tk()
    screen9.title('Wybór restauracji')
    screen9.geometry('400x400')

    Label(screen9, text = 'Wybierz restauracje, którą chcesz ocenić', font=('Calibri, 11')).pack()
    Label(screen9, text = '').pack()

    my_listbox = Listbox(screen9)
    my_listbox.pack(pady=15)
    

    my_listbox.insert(1, 'Steakhouse')
    my_listbox.insert(2, 'Coffee & Tea')
    my_listbox.insert(3, 'Bars')
    my_listbox.insert(4, 'Mexican')
    my_listbox.insert(5, 'Specialty Food')
    my_listbox.insert(6, 'Thai')
    my_listbox.insert(7, 'Buffets')
    my_listbox.insert(8, 'Burgers')
    my_listbox.insert(9, 'Canadian (New)')
    my_listbox.insert(10, 'Sandwiches')
    my_listbox.insert(11, 'Chinese')
    my_listbox.insert(12, 'Japanese')
    my_listbox.insert(13, 'Fast Food')

    def select():
        my_label.config(text=my_listbox.get(ANCHOR))
        global value
        value=my_listbox.get(ANCHOR)
        print(value)
        
    
    global my_label
    my_label = Label(screen9, text="", fg="green")
    my_label.pack(pady=5)

    my_button2 = Button(screen9, text="Select", command = select and opinia,height = '2', width = '30')
    my_button2.pack(pady=10)

    Button(screen9, text = 'Wyjście', height = '2', width = '30', command = koniec).pack()
    

def opinia():
    screen9.destroy()
    global screen4
    screen4 = Tk()
    screen4.title('Rekomendacje restauracji')
    screen4.geometry('400x400')


    global ocena
    global ocena_entry
    global restauracja_entry

    ocena = StringVar()
    restauracja = StringVar()

    Label(screen4, text = 'Dodaj ocenę wybranej restauracji', height = '2', width = '30').pack()
    Label(screen4, text = '').pack()
    Label(screen4, text = 'Ocena (1-5): ').pack()
    ocena_entry = Entry(screen4, textvariable = ocena)
    ocena_entry.pack()
    Label(screen4, text = '').pack()
    Button(screen4, text = 'Dodaj', height = '2', width = '30', command = dodanoopinie).pack()
    Button(screen4, text = 'Wyjście', height = '2', width = '30', command = koniec).pack()



def dodanoopinie():
    
    conn = sqlite3.connect('RecommendationsDB.db')
    c = conn.cursor()
    
    review = join(random.sample('abcdefghijklmnoperstuwyzq1234567890!@#$%^&*()_-',25))
    business = ("SELECT * FROM users WHERE categories = ?")
    c.execute(business,[(value.get())])
    c.execute("""INSERT INTO  reviews (review_id, user_id, business_id, stars, date) VALUES(?,?,?,?,?),(review.get(), login.get(), business.get(), ocena.get(), '0')""")

    


    conn.commit() 
    conn.close()

    ocena_entry.delete(0, END)
    komentarz_entry.delete(0, END)
    restauracja_entry.delete(0, END)
    
    screen4.destroy()
    global screen8
    screen8 = Tk()
    screen8.title('Rekomendacje restauracji')
    screen8.geometry('400x400')

    Label(screen8, text = 'Twoja opinia została dodana!',fg = 'green', height = '2', width = '30').pack()
    Label(screen8, text = '').pack()
    Button(screen8, text = 'Sprawdź rekomendacje restauracji', height = '2', width = '30').pack()
    Label(screen8, text = '').pack()
    Button(screen8, text = 'Dodaj opinie o restauracji', height = '2', width = '30', command = opinia).pack()
    Label(screen8, text = '').pack()
    Button(screen8, text = 'Wyjście', height = '2', width = '30', command = koniec).pack()



def logowanie():
    global screen2
    screen2 = Tk()
    screen2.title('Logowanie')
    screen2.geometry('400x400')

    global login
    global haslo

    login = StringVar()
    haslo = StringVar()


    Label(screen2, text = 'Uzupełnij dane ponizej').pack()
    Label(screen2, text = '').pack()
    
    global login_verify
    global haslo_verify

    login_verify = StringVar()
    haslo_verify = StringVar()

    global login_entry1
    global haslo_entry1

    Label(screen2, text = 'Login: ').pack()
    login_entry1 = Entry(screen2, textvariable = login_verify)
    login_entry1.pack()
    Label(screen2, text = '').pack()
    Label(screen2, text = 'Hasło: ').pack()
    haslo_entry1 = Entry(screen2, textvariable = haslo_verify)
    haslo_entry1.pack()
    Label(screen2, text = '').pack()
    Button(screen2, text = 'Zaloguj się', width = 10, height = 1, command = weryfikacja).pack()
    Button(screen2, text = 'Wyjście', height = '1', width = '10', command = koniec).pack()

def weryfikacja():
    with sqlite3.connect('RecommendationsDB.db') as db:
        c = db.cursor()
    find_user = ('SELECT * FROM users WHERE user_id = ? and haslo = ?')
    c.execute(find_user,[(login_verify.get()),(haslo_verify.get())])
    result = c.fetchall()

    screen2.destroy()
    global screen11
    screen11 = Tk()
    screen11.title('Logowanie')
    screen11.geometry('400x400')

    if result:
        
        Label(screen11, text = 'Jesteś zalogowany!', fg='green', font=('Calibri, 11')).pack()
        Label(screen11, text = '').pack()
        Button(screen11, text = 'Sprawdź rekomendacje restauracji', height = '2', width = '30').pack()
        Label(screen11, text = '').pack()
        Button(screen11, text = 'Dodaj opinie o restauracji', height = '2', width = '30', command = wybor).pack()
        Label(screen11, text = '').pack()
        Button(screen11, text = 'Wyjście', height = '2', width = '30', command = koniec).pack()
    else:
        
        Label(screen11, text = 'Nie udało się zalogować!', fg='red', font=('Calibri, 11')).pack()
        Label(screen11, text = '').pack()
        Button(screen11, text = 'Spróbuj zalogować się ponownie', height = '2', width = '30', command = logowanie).pack()
        Label(screen11, text = '').pack()
        Button(screen11, text = 'Zarejestruj się', height = '2', width = '30', command = rejestracja).pack()
        Label(screen11, text = '').pack()
        Button(screen11, text = 'Wyjście', height = '2', width = '30', command = koniec).pack()

    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('400x400')
    screen.title('Rekomendacje restauracji')
    Label(text = 'Rekomendacje restauracji', bg = 'light blue', width = '300', height ='3', font = ('Calibri', 20)).pack()
    Label(text = '').pack()
    Button(text = 'Zaloguj się', height = '2', width = '30', command = logowanie).pack()
    Label(text = '').pack()
    Button(text = 'Zarejestruj się', height = '2', width = '30', command = rejestracja).pack()
    Label(text = '').pack()
    Button(text = 'Wyjście', height = '2', width = '30', command = koniec).pack()
    
    
    screen.mainloop()


main_screen()