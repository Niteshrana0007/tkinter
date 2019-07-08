import tkinter
from functools import partial
from data2 import DataHandler


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
         label = tkinter.Label(window,text = element)
         label.grid(column = 0,row  = i+1)
         category_data_labels.append(label)

window = tkinter.Tk()
window.title("Children Book")
window.geometry('300x500')
data_handler = DataHandler("data.json")
category_lists = data_handler.get_categories()
print(category_lists)
category_data_labels = []

for i in range(len(category_lists)):
    element = category_lists[i]
    command_func = partial(open_category,element)
    button  = tkinter.Button(window,text = element,command = command_func)
    button.grid(row=0,column=i)

window.mainloop()
