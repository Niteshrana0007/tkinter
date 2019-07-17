import tkinter
from functools import partial
from project_1 import DataHandler


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
         label = tkinter.Label(canvas_frame,text = element)
         label.grid(column = 0,row  = i+1)
         category_data_labels.append(label)

window = tkinter.Tk()
window.title("Children Book")
window.geometry('300x500')
data_handler = DataHandler("project.json")
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

buttons_container = tkinter.Frame(window)
buttons_container.pack(side=tkinter.TOP, fill = tkinter.X)

for i in range(len(category_lists)):
    element = category_lists[i]
    command_func = partial(open_category,element)
    button  = tkinter.Button(buttons_container,text = element,command = command_func)
    button.grid(row=0,column=i)

container = tkinter.Frame(window,bg='green')
container.pack(side=tkinter.TOP,expand=True,fill = tkinter.BOTH)

scrollbar1 = tkinter.Scrollbar(container)
scrollbar1.pack(side=tkinter.RIGHT,fill=tkinter.Y)

data_canvas = tkinter.Canvas(container,bg='red')
data_canvas.pack(side=tkinter.TOP)

canvas_frame = tkinter.Frame(data_canvas)
canvas_frame.pack(side = tkinter.TOP,expand=True,fill=tkinter.BOTH)


window.mainloop()
