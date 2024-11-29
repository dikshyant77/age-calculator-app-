from tkinter import *
from datetime import date


root = Tk()
root.title("Age Calculator App")
root.geometry('400x400')

frame = Frame(master = root, height = 200, width = 360, bg = "#7fffd4")

Label1 = Label(frame, text = "Name", bg = "#0047AB", fg = "white", width = 12)
Label2 = Label(frame, text = "Day", bg = "#0047AB", fg = "white", width = 12)
Label3 = Label(frame, text = "Month", bg = "#0047AB", fg = "white", width = 12)
Label4 = Label(frame, text = "Year", bg = "#0047AB", fg = "white", width = 12)

name_entry= Entry(frame)
day_entry= Entry(frame)
month_entry= Entry(frame)
year_entry= Entry(frame)

def do_age():
  name = name_entry.get()
  greet = "Hey "+name+"!"

  year_input = year_entry.get()
  
  this_year = date.today()
  age = this_year.year - int(year_input)

  message = "Your age is "+str(age)

  text_box.insert(END, greet)
  text_box.insert(END, message)

text_box = Text(bg = "#4169E1", fg = 'white')

button = Button(text = "Calculate Age",command = do_age, bg = '#89CFF0')

frame.place(x = 20, y = 10)
Label1.place(x = 20, y = 10)
name_entry.place(x = 150, y = 10)
Label2.place(x = 20, y = 60)
day_entry.place(x = 150, y = 60)
Label3.place(x = 20, y = 110 )
month_entry.place(x= 150, y = 110)
Label4.place(x = 20, y = 160)
year_entry.place(x = 150, y = 160)
button.place(x = 130, y = 210)

text_box.place(y = 250)
root.mainloop()
