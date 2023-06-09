from tkinter import *
win=Tk()

name=Entry(win ,width=50)

name.pack()
name.insert(0,"Enter Your Name:")

#font="Comic Sans MS"

def myClick():
    lable_1=Label(win,text="hello"+name.get())
    lable_1.pack()

my_Button=Button(win,text="Enter",command=myClick)
my_Button.pack()

win.mainloop()
