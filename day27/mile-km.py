from tkinter import *

window = Tk()
window.title("Mile to Kilometer conv")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

base_text = Label(text='is equal to: ', font=('Arial', 12))
base_text.grid(column=0, row=1)
base_text.config(padx=20, pady=5)

output = Label(text='0', font=('Arial', 12))
output.grid(column=1, row=1)
output.config(padx=20, pady=5)


def entry_input():
    conv = input.get()
    op = round(float(conv) * 1.6, 2)
    output['text'] = op


input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)

button = Button(text='calculate', command=entry_input, width=10)
button.grid(column=1, row=2)

mile = Label(text='miles', font=('Arial', 12))
mile.grid(column=2, row=0)
mile.config(padx=20, pady=5)

km = Label(text='km', font=('Arial', 12))
km.grid(column=2, row=1)
km.config(padx=20, pady=5)

window.mainloop()
