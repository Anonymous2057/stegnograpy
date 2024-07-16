from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = tk.Tk()
root.title("Steganography - hide a secret text message in an image")
root.geometry("710x600+100+100")
root.resizable(False, False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=(("PNG file", "*.png"),
                                                                                                      ("JPG file", "*.jpg"), 
                                                                                                      ("All Files", "*.*")))
    if filename:
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=250, height=250)
        lbl.image = img

def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(filename, message)

def show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    if secret:
        secret.save("hidden.png")

# Logo
logo = PhotoImage(file=r"C:\Users\pmnm2\Desktop\python projects\encryptionlogo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)
Label(root, text="SM CREATIONS", bg="#2f4155", fg="white", font="arial 25 bold").place(x=200, y=20)

# First frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=150)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# Second frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=360, y=150)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

Scrollbar1 = Scrollbar(frame2)
Scrollbar1.place(x=320, y=0, height=300)

Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

# Third frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=15, y=460)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, image, photo file", bg="#2f4155", fg="yellow").place(x=20, y=5)

# Fourth frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=460)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=show).place(x=180, y=30)
Label(frame4, text="Picture, image, photo file", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
