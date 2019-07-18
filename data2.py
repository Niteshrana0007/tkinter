import tkinter
from functools import partial
from data1 import DataHandler


def get_data_for_category(name):
     return data_handler.get_data_for_category(name)

def open_category(name):
    
     # delete old labels
     for element in category_data_labels:
         element.configure(text="")
         del element

     list_data_for_category = get_data_for_category(name)
     for i in range(len(list_data_for_category)):
         element = list_data_for_category[i]
         label = tkinter.Label(data_frame,text = element)
         label.grid(column = 0,row  = i+1)
         category_data_labels.append(label)

def onFrameConfigure(event):
    canvas.config(scrollregion = canvas.bbox(tkinter.ALL))

window = tkinter.Tk()
window.title("Children Book")
window.geometry('300x500')
data_handler = DataHandler("data.json")
category_lists = data_handler.get_categories()
print(category_lists)
category_data_labels = []

'''canvas = tkinter.Canvas(window,bg='red')
frame = tkinter.Frame(canvas,bg='green')
vsb = tkinter.Scrollbar(canvas,command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)
vsb.pack(side=tkinter.RIGHT,fill=tkinter.Y)
canvas.pack(side=tkinter.BOTTOM,fill=tkinter.BOTH,expand=True)
canvas.create_window(window=frame,anchor=tkinter.NW)'''

buttons_container = tkinter.Frame(window,bg='red')
buttons_container.pack(side=tkinter.TOP, fill = tkinter.X)

for i in range(len(category_lists)):
    element = category_lists[i]
    command_func = partial(open_category,element)
    button  = tkinter.Button(buttons_container,text = element,command = command_func)
    button.grid(row=0,column=i)

content_frame = tkinter.Frame(window,bg='green')
content_frame.pack(side=tkinter.BOTTOM,expand=True,fill=tkinter.BOTH)

vsb = tkinter.Scrollbar(content_frame)
vsb.pack(side=tkinter.RIGHT,fill=tkinter.Y)

canvas = tkinter.Canvas(content_frame, yscrollcommand=vsb.set, bg='orange')
canvas.pack(side=tkinter.TOP,expand=True,fill=tkinter.BOTH)

data_frame = tkinter.Frame(canvas)
canvas.create_window((5,5),window=data_frame,anchor=tkinter.NW)

vsb.config(command = canvas.yview)

data_frame.bind('<Configure>',onFrameConfigure)

'''container = tkinter.Frame(window,bg='green')
container.pack(side=tkinter.TOP,expand=True,fill = tkinter.BOTH)

scrollbar1 = tkinter.Scrollbar(container)
scrollbar1.pack(side=tkinter.RIGHT,fill=tkinter.Y)

data_canvas = tkinter.Canvas(container,bg='red')
data_canvas.pack(side=tkinter.TOP)

canvas_frame = tkinter.Frame(data_canvas)
canvas_frame.pack(side = tkinter.TOP,expand=True,fill=tkinter.BOTH)



scrollbar1.config(command=data_canvas.yview)
data_canvas.config(yscrollcommand=scrollbar1.set)

canvas_frame.bind('<Configure>',onFrameConfigure)'''

window.mainloop()
