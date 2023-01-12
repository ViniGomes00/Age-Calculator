from tkinter import *
from datetime import datetime

root=Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator")

photo=PhotoImage(file="Age calculator.png")
myimage=Label(image=photo)
myimage.pack(padx=15,pady=15)

def calculateAge():
    today=datetime.today()
    birthDate=datetime(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age=today.year - birthDate.year -((today.month, today.day)<(birthDate.month, birthDate.day))
    Label(text=f"{nameValue.get()}, you are {age} years old", font=30).place(x=300,y=500)

Label(text="Name",font=23).place(x=200,y=200)
Label(text="Year",font=23).place(x=200,y=250)
Label(text="Month",font=23).place(x=200,y=300)
Label(text="Day",font=23).place(x=200,y=350)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(root, textvariable=nameValue, width=30, bd=3, font=20)
nameEntry.place(x=300, y=200)

yearEntry=Entry(root, textvariable=yearValue, width=30, bd=3, font=20)
yearEntry.place(x=300, y=250)

monthEntry=Entry(root, textvariable=monthValue, width=30, bd=3, font=20)
monthEntry.place(x=300, y=300)

dayEntry=Entry(root, textvariable=dayValue, width=30, bd=3, font=20)
dayEntry.place(x=300, y=350)

Button(text="Calculate Age", font=20, bg="black", fg="white", width=11, height=2, command=calculateAge).place(x=350, y=450)

root.mainloop()