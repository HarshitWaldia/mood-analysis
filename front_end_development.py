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