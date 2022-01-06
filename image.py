from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.title("Barcelona ")
window.resizable(0, 0)
# window.iconbitmap('fcb.ico')                                         #adding icon in title
# create frame
frame=Frame(window, width=600, height=500, bg='white', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)
# create thumbanials of all images
img1 = Image.open("IMG_2152.png")
img1.thumbnail((550, 450))
img2 = Image.open("IMG_0522.png")
img2.thumbnail((550, 450))
img3 = Image.open("IMG_2980.png")
img3.thumbnail((550, 450))
img4 = Image.open("IMG_5161.png")
img4.thumbnail((550, 450))

# open images to use with labels
image1 = ImageTk.PhotoImage(img1)
image2 = ImageTk.PhotoImage(img2)
image3 = ImageTk.PhotoImage(img3)
image4 = ImageTk.PhotoImage(img4)
# create list of images
images = [image1, image2,image3, image4]
# configure the image to the Label in frame
i = 0
image_label = Label(frame, image=images[i])
image_label.pack()
# create functions to display previous and next images
def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
        previous()
def next():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
    except:
        i = -1
        next()
# create buttons
btn1 = Button(window, text="<<",width=8, bd=5,bg='white', fg='green', font=('cambria 15 bold'), relief=RAISED, command=previous)
btn1.pack(side=LEFT, padx=60, pady=5)
btn3 = Button(window, text="Exit", width=8,bd=5, bg='white', fg='green', font=('cambria 15 bold'), relief=RAISED, command=window.destroy)
btn3.pack(side=LEFT, padx=60, pady=5)
btn2 = Button(window, text=">>", width=8, bd=5,bg='white', fg='green', font=('cambria 15 bold'), relief=RAISED, command=next)
btn2.pack(side=LEFT, padx=60, pady=5)
window.mainloop()