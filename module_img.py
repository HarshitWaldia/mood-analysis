#importing the Image class from PIL package
from PIL import Image
#read the image, creating an object

def sad():
    
    im = Image.open(r"C:\Users\harsh\Mini Project\img6.jpg")
    

    #show picture
    im.show()


def jokes():
    im=Image.open(r"C:\Users\harsh\Mini Project\img5.jpg")

    im.show()


def happy():
    im=Image.open(r"C:\Users\harsh\Mini Project\img4.jpg")

    im.show()