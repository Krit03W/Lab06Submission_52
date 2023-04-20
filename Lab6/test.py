from tkinter import *  
from PIL import ImageTk, Image

root = Tk()  
canvas = Canvas(root, width=200, height=200)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("1182001.png"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop()