import mysql.connector
from PIL import Image
import re

# Establish database connection
def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harshit",
            database="healthsys"
        )
        print("Database connection established")
        return mydb
    except mysql.connector.Error as error:
        print("Error while connecting to database:", error)
        return None

# Insert user data into database
def insert_user_data(cursor, name, age, gender, address, mood):
    query = "INSERT INTO users (name, age, gender, address, mood) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, gender, address, mood)
    cursor.execute(query, values)
    cursor.commit()

# Get user input for name and validate
def get_user_name():
    while True:
        name = input("Enter name : ")
        if bool(re.match('^[a-zA-Z" "]*$', name)):
            print("Valid name")
            return name.title()
        else:
            print("Invalid name. Please enter only alphabetic characters and spaces.")

# Get user input for age and validate
def get_user_age():
    while True:
        try:
            age = int(input("Enter age : "))
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
            return gender
        else:
            print("Invalid gender. Please enter either 'male' or 'female'.")

# Get user input for address
def get_user_address():
    return input("Enter address: ")

# Get user input for mood and validate
def get_user_mood():
    valid_moods = [
        "heartbroken", "unhappy", "depressed", "miserable", "sorry", "bad", "melancholy", "upset", "worried",
        "sorrowful", "disappointed", "saddened", "mournful", "uneasy", "hopeless", "dejected", "heartsick",
        "troubled", "gloomy", "forlorn", "crestfallen", "doleful", "melancholic", "depressing", "glum", "downhearted",
        "disconsolate", "woebegone", "inconsolable", "
