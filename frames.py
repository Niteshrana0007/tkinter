import tkinter

window = tkinter.Tk()
window.title("NEWS")
window.geometry("300x500")

categories_frame = tkinter.Frame(window,bg="red",bd = 4)
categories_frame.pack(side = tkinter.TOP,fill = tkinter.X)

label = tkinter.Label(categories_frame,text="hello")
label.pack()

pagination_frame = tkinter.Frame(window,bg="green",bd=4)
pagination_frame.pack(side = tkinter.BOTTOM,fill = tkinter.X)

label2 = tkinter.Label(pagination_frame,text = "hi")
label2.pack()

articles_frame = tkinter.Frame(window,bg="yellow")
articles_frame.pack(side = tkinter.RIGHT,fill = tkinter.Y)

scrollbar = tkinter.Scrollbar(articles_frame)
scrollbar.pack(side = tkinter.RIGHT,expand = True, fill = tkinter.BOTH)

mylist = tkinter.Listbox(articles_frame,yscrollcommand = scrollbar.set)
for line in range(100):
    mylist.insert(tkinter.END,"This is line number" + str(line))

mylist.pack(side = tkinter.LEFT,expand = True,fill = tkinter.BOTH)
scrollbar.config(command = mylist.yview)

window.mainloop()
