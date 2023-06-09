import mysql.connector
import PIL
from PIL import Image
import tkinter as tk
from tkinter import messagebox


class HealthSysApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Health System App")
        self.geometry("400x400")

        # Creating connection object
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harshit",
            database="healthsys"
        )

        # Checking connection establishment
        if self.mydb.is_connected():
            print("connection established")

        # Create a Label widget for the user name
        self.label_username = tk.Label(self, text="Enter your name:")
        self.label_username.pack()

        # Create an Entry widget for the user name
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        # Create a Button widget to submit the user name
        self.button_username = tk.Button(self, text="Submit", command=self.check_username)
        self.button_username.pack()

    def check_username(self):
        # Get the user name from the Entry widget
        username = self.entry_username.get()

        # Validate the user name
        if not username or not username.isalpha():
            messagebox.showerror("Error", "Please enter a valid name!")
            return

        # Greet the user and ask how they are feeling
        greeting = f"Hi {username.title()}, how are you feeling?"
        self.label_greeting = tk.Label(self, text=greeting)
        self.label_greeting.pack()

        # Create a Listbox widget for the mood options
        self.moods = ["happy", "sad", "angry", "excited", "stressed", "tired"]
        self.listbox_moods = tk.Listbox(self)
        for mood in self.moods:
            self.listbox_moods.insert(tk.END, mood)
        self.listbox_moods.pack()

        # Create a Button widget to submit the mood
        self.button_mood = tk.Button(self, text="Submit", command=self.check_mood)
        self.button_mood.pack()

    def check_mood(self):
        # Get the selected mood from the Listbox widget
        mood = self.listbox_moods.get(tk.ACTIVE)

        # Check if the mood is valid
        if mood not in self.moods:
            messagebox.showerror("Error", "Please select a valid mood!")
            return

        # Ask the user for their age and gender
        self.label_age = tk.Label(self, text="Enter your age:")
        self.label_age.pack()
        self.entry_age = tk.Entry(self)
        self.entry_age.pack()

        self.label_gender = tk.Label(self, text="Enter your gender:")
        self.label_gender.pack()
        self.entry_gender = tk.Entry(self)
        self.entry_gender.pack()

        self.button_info = tk.Button(self, text="Submit", command=self.check_info)
        self.button_info.pack()

        # Remove the previous widgets
        self.label_greeting.destroy()
        self.listbox_moods.destroy()
        self.button_mood.destroy()

    def check_info(self):
        # Get the age and gender from the Entry widgets
        age = self.entry_age.get()
        gender = self.entry_gender.get()

        # Validate the age and gender
        if not age.isnumeric() or not gender or not gender.isalpha():
            messagebox.showerror("Error", "Please enter valid information!")
            return

