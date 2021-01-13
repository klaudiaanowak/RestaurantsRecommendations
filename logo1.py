from tkinter import *
import sys
import os
import sqlite3



def koniec():
    sys.exit()
def register_user():

    conn = sqlite3.connect('Recommendations.db')
    c = conn.cursor()

    c.execute('INSERT INTO  users (login, haslo, email, tel) VALUES(?,?,?,?)',(login.get(), haslo.get(), email.get(), tel.get()))

    conn.commit() 
    conn.close()

    login_entry.delete(0, END)
    haslo_entry.delete(0, END)
    email_entry.delete(0, END)
    tel_entry.delete(0, END)

    screen7 = Toplevel(screen)
    screen7.title('Rejestracja')
    screen7.geometry('200x200')
    Label(screen7, text = 'Zostałeś zarejestrowany!', fg='green', font=('Calibri, 11')).pack()
    Label(screen7, text = '').pack()
    Button(screen7, text = 'Dalej', width = 10, height = 1, command = udanelogowanie).pack()


def rejestracja():
    screen1 = Toplevel(screen)
    screen1.title('Rejestracja')
    screen1.geometry('400x400')

    global login
    global haslo
    global email
    global tel
    global login_entry
    global haslo_entry
    global email_entry
    global tel_entry

    email = StringVar()
    login = StringVar()
    haslo = StringVar()
    tel = StringVar()


    Label(screen1, text = 'Uzupełnij dane ponizej').pack()
    Label(screen1, text = '').pack()
    Label(screen1, text = 'E-mail: ').pack()
    email_entry = Entry(screen1, textvariable = email)
    email_entry.pack()
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
    screen3 = Toplevel(screen)
    screen3.title('Logowanie')
    screen3.geometry('400x400')

    Label(screen3, text = 'Jesteś zalogowany!', fg='green', font=('Calibri, 11')).pack()
    Label(screen3, text = '').pack()
    Button(screen3, text = 'Sprawdź rekomendacje restauracji', height = '2', width = '30').pack()
    Label(screen3, text = '').pack()
    Button(screen3, text = 'Dodaj opinie o restauracji', height = '2', width = '30', command = opinia).pack()
    Label(screen3, text = '').pack()
    Button(screen3, text = 'Wyjście', height = '2', width = '30', command = koniec).pack()

def opinia():
    screen4 = Toplevel(screen)
    screen4.title('Rekomendacje restauracji')
    screen4.geometry('400x400')

    global ocena
    global komentarz
    global restauracja
    global ocena_entry
    global komentarz_entry
    global restauracja_entry

    ocena = StringVar()
    komentarz = StringVar()
    restauracja = StringVar()

    Label(screen4, text = 'Dodaj opienie o restauracji', height = '2', width = '30').pack()
    Label(screen4, text = '').pack()
    Label(screen4, text = 'Nazwa restauracji: ').pack()
    restauracja_entry = Entry(screen4, textvariable = restauracja)
    restauracja_entry.pack()
    Label(screen4, text = 'Ocena (1-5): ').pack()
    ocena_entry = Entry(screen4, textvariable = ocena)
    ocena_entry.pack()
    Label(screen4, text = 'Komentarz: ').pack()
    komentarz_entry = Entry(screen4, textvariable = komentarz)
    komentarz_entry.pack()
    Label(screen4, text = '').pack()
    Button(screen4, text = 'Dodaj', height = '2', width = '30', command = dodanoopinie).pack()
    Button(screen4, text = 'Wyjście', height = '2', width = '30', command = koniec).pack()

def dodanoopinie():
    
    conn = sqlite3.connect('Recommendations.db')
    c = conn.cursor()

    c.execute('INSERT INTO  reviews (login, nazwarestauracji, ocena, komentarz) VALUES(?,?,?,?)',(login.get(), restauracja.get(), ocena.get(), komentarz.get()))

    conn.commit() 
    conn.close()

    ocena_entry.delete(0, END)
    komentarz_entry.delete(0, END)
    restauracja_entry.delete(0, END)

    screen8 = Toplevel(screen)
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
    screen2 = Toplevel(screen)
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
    Button(screen2, text = 'Zaloguj się', width = 10, height = 1, command = udanelogowanie).pack()
    Button(screen2, text = 'Wyjście', height = '1', width = '10', command = koniec).pack()

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