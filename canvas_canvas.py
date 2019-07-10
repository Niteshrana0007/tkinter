import tkinter

def populate(frame):
    '''put in some fake data'''
    for row in range(5):
        tkinter.Label(frame,text=str(row),width=3,borderwidth="1",
                      relief = "solid").grid(row=row,column=0)
        t = "this is second column " + str(row)
        tkinter.Label(frame,text=t).grid(row=row,column=1)

def onFrameConfigure(event):
    '''reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion = canvas.bbox(tkinter.ALL))

def populate_frame():
    populate(frame)

root = tkinter.Tk()
button = tkinter.Button(root,text = "Button1",command = populate_frame)
button.pack(side = tkinter.TOP)
canvas = tkinter.Canvas(root,bg = "red")
frame = tkinter.Frame(canvas,bg = "green")
vsb = tkinter.Scrollbar(root,command = canvas.yview)
canvas.configure(yscrollcommand = vsb.set)

vsb.pack(side = tkinter.RIGHT,fill = tkinter.Y)
canvas.pack(side=tkinter.LEFT,fill=tkinter.BOTH,expand=True)
canvas.create_window((4,4),window=frame,anchor=tkinter.NW)

frame.bind('<Configure>',onFrameConfigure)
root.mainloop()
