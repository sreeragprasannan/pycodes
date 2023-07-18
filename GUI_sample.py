from tkinter import *

window = Tk()
window.geometry("500x500")



def hello():
    print("button clicked")


button = Button(window, text="ok", command=hello)
button2 = Button(window, text="click", command=hello)
button.grid(row=0, column=0)
button2.grid(row=0, column=1)

window.mainloop()
