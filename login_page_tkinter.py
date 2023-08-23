import tkinter
from tkinter import ttk

def submit():
    first_name = text_fnm.get()
    last_name = text_lnm.get()
    gender = gender_var.get()
    interest = [Web_var.get(), App_var.get(), Game_var.get(), Hybrid_var.get()]
    selected_city = city_combobox.get()

    print("First name:", first_name)
    print("Last name:", last_name)
    print("Gender:", gender)
    print("Interest:", interest)
    print("Selected city:", selected_city)

screen = tkinter.Tk()

screen.title("Login page")
screen.geometry('400x500')
screen.config(bg='Light grey')

lable_fnm = tkinter.Label(text='First name:', bg='Light grey', font='Calibri 15 bold', fg='Black',)
lable_fnm.grid(row=0, column=0, sticky='w')

label_lnm = tkinter.Label(text='Last name:', bg='Light grey', font='Calibri 15 bold', fg='Black')
label_lnm.grid(row=1, column=0, sticky='w')

text_fnm = tkinter.Entry()
text_fnm.grid(row=0, column=1, sticky='w')

text_lnm = tkinter.Entry()
text_lnm.grid(row=1, column=1, sticky='w')

gender_var = tkinter.StringVar()  # Initialize the gender_var

tkinter.Radiobutton(text='Male', value='Male', bg='Light grey', font='Calibri 15 bold', fg='Black', variable=gender_var).grid(row=2, column=0, sticky='w')
tkinter.Radiobutton(text='Female', value='Female', bg='Light grey', font='Calibri 15 bold', fg='Black', variable=gender_var).grid(row=2, column=1, sticky='w')

Web_var = tkinter.IntVar()
App_var = tkinter.IntVar()
Game_var = tkinter.IntVar()
Hybrid_var = tkinter.IntVar()

tkinter.Checkbutton(text='Web development', bg='Light grey', font='Calibri 15 bold', fg='Black', variable=Web_var).grid(row=3, column=0, sticky='w')
tkinter.Checkbutton(text='App development', bg='Light grey', font='Calibri 15 bold', fg='Black', variable=App_var).grid(row=4, column=0, sticky='w')
tkinter.Checkbutton(text='Game development', bg='Light grey', font='Calibri 15 bold', fg='Black', variable=Game_var).grid(row=5, column=0, sticky='w')
tkinter.Checkbutton(text='Hybrid development', bg='Light grey', font='Calibri 15 bold', fg='Black', variable=Hybrid_var).grid(row=6, column=0, sticky='w')

city = ['Ahmedabad', 'Rajkot', 'Baroda', 'Jamnagar', 'Junagadh']
city_combobox = ttk.Combobox(values=city)
city_combobox.grid(row=7, column=0, sticky='w')

submit_button = tkinter.Button(text='Submit', font='Calibri 15 bold', command=submit)
submit_button.place(x=160, y=300)

tkinter.mainloop()
