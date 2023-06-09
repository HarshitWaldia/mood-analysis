import mysql.connector
#for connecting to database "healthsys"

import numpy
#for working with numbers and data
from numpy import *

import matplotlib
#for ploting graphs and other mathematical representation
from matplotlib import *

import module_Mood as moodlib
#for analyzing mood (NOT INBUILT) MADE BE HARSHIT WALDIA ---------RESEARCHED----------
from module_Mood import *

import PIL
#for working with images and image functioning 
from PIL import Image,ImageTk

import re
#for working with string manipulation
from re import *

import tkinter as tk
#for frontend development
from tkinter import *


# Establish database connection
def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harshit",
            database="healthsys"
        )
        print("Database Connection Established")
        return mydb
    except mysql.connector.Error as error:                           #if any error encounters
        print("Error while connecting to database:", error)
        return None

# Insert user data into database
def insert_user_data(cursor, name, age, gender, address, mood):
    query = "INSERT INTO users (name, age, gender, address, mood) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, gender, address, mood)
    cursor.execute(query, values)
    
    #if you skip this nothing would be saved
    cursor.commit()


# Get user input for name and validate
def get_user_name(name):
    while True:
        #name = input("Enter name : ")
        #USING REGERENCE RELATION FOR VALIDATION
        if bool(re.match('^[a-zA-Z" "]*$', name)):
            #TO BE REMOVED IN THE FUTURE
            print("Valid name")
            return name.title()
        else:
            print("Invalid name. Please enter only alphabetic characters and spaces.")


# Get user input for age and validate
def get_user_age(age):
    while True:
        try:
            #age = int(input("Enter age : "))
            if age > 1 and age < 100:
                print("Valid age")
                return age
            else:
                print("Age should be > 1 and < 100")
        except ValueError:
            print("Invalid input. Please enter a numeric value for age.")

# Get user input for gender and validate
def get_user_gender():
    while True:
        gender = input("Enter your gender : ").lower()
        if gender in ['male', 'female']:
            print("Valid gender")
            return gender.title()
        else:
            print("Invalid gender. Please enter either 'male' or 'female'.")

# Get user input for address
def get_user_address():
    return input("Enter address: ").title()

# Get user input for mood and validate
def get_user_mood():
    while True:
        mood = input("Enter your mood : ").lower()
        if mood in moodlib.mood_dict:
            print("Valid Mood")
            return mood.title()
        else:
            print("Never Heard Of It . Sorry !")



"""#TESTING SPACE 1.0
connect_to_database()
name=get_user_name()
gender=get_user_gender()
age=get_user_age()
address=get_user_address()
mood=get_user_mood()

print(name)
print(gender)
print(age)
print(address) 
print(mood)"""

def submit_data():
    name = name_entry.get()
    age = age_entry.get()

    if get_user_name(name) and get_user_age(age):
        # Add code to insert data into database here
        print("Data saved successfully!")
    else:
        error_label.config(text="Invalid input. Please try again.")


#Start of Front End Creation 

win=tk.Tk()
win.title("Health Analysis And Stress Relief System")
win.geometry("400x300")

#Name lable and entry fields 

name_lable=tk.Label(win,text="Name : ")
name_lable.pack()
name_entry=tk.Entry(win)
name_entry.pack()

# Age label and entry field
age_label = tk.Label(win, text="Age:")
age_label.pack()
age_entry = tk.Entry(win)
age_entry.pack()

# Submit button
submit_button = tk.Button(win, text="Submit", command=submit_data)
submit_button.pack()

# Error label (hidden by default)
error_label = tk.Label(win, text="", fg="red")
error_label.pack()
error_label.pack_forget()

win.mainloop()


