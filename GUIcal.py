from tkinter import *

window = Tk()
frame1 = Frame(window,width=200,height=300)

frame1.pack()


label1 = Label(frame1,text= "enter_first_number")
label1.pack()

label2 = Label(frame1,text= "enter_second_number")
label2.pack()

def btnClick():
    labelnum1 = configure =
btnnum1 = Button(frame1,command = btnClick)
btnnum1.grid(row=0,column=1)

