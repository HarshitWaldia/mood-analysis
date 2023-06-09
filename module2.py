from tkinter import *
from PIL import Image,ImageTk

window=Tk()

window.title("MoodLog")

""" actual window size while opening """
window.geometry("733x434")

""" min size for opening window """
window.minsize(733,434)

#Tittle
window.title("Stress Management")


#photo =PhotoImage(file="Hogwarts2.jpg") 
""" only for .png extension of images .So this image is not supported  """

#image=Image.open("C:\\Users\\harsh\\Mini Project\\Hogwarts2.jpg")
#photo=ImageTk.PhotoImage(image)
#lable1= Label(image=photo)
#lable1.pack()

def play_game():
    import webbrowser
    webbrowser.open('http://poki.com',new=2)

    # webbrowser.open_new_tab('http://poki.com')
    

Button_1=Button(window,text="GAME",command=play_game,bg="black",fg="white")
Button_1.pack()

window.mainloop()