from tkinter import *
from PIL import ImageTk,Image

root = Tk()
canvas=Canvas(root,width=300,height=300)
canvas.pack()
img = Image.open("C:/Users/int/Desktop/Penguins.jpg")
img = img.resize((200,200),Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
canvas.create_image(20,20,anchor=NW,image=img)

root.mainloop()
