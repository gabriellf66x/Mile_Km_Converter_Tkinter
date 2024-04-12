from tkinter import *


def button_clicked():
    new_text = input.get()
    if new_text.isalpha() or new_text.isalnum():
        km.config(text='Entry not valid!')
    if new_text.isdigit():
        kilo = int(new_text) * 1.609
        km.config(text=str(kilo))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=25, pady=10)

my_label0 = Label(text="Miles", font=("Arial", 12, "bold"))
my_label01 = Label(text="is equal to", font=("Arial", 12, "bold"))
my_label02 = Label(text="Km", font=("Arial", 12, "bold"))
km = Label(text="0", font=("Arial", 12, "bold"))
my_label0.grid(column=2, row=1)
my_label01.grid(column=0, row=2)
my_label02.grid(column=2, row=2)
km.grid(column=1, row=2)
my_label0.config(padx=10, pady=5)

button = Button(text="Convert", command=button_clicked)
button.grid(column=1, row=4)

input = Entry(width=10)
print(input.get())
input.grid(column=1, row=1)

window.mainloop()
