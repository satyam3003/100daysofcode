from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=300,height=400)

# Label or text..............

my_label = Label(text=' I am a label', font=('Arial',24,'bold'))
my_label.grid(column=0, row=0)


# Button......

def button_clicked():
    my_label['text'] = 'I got clicked'


button = Button(text='Click me', command = button_clicked)
button.grid(column=1,row=1)

# Entry / input ...........


def entry_input():
    my_label['text'] = input.get()


input = Entry()
input.grid(column = 2,row=0)

button_2 = Button(text='Click',command = entry_input,width=10)
button_2.grid(column=3,row=2)

window.mainloop()
