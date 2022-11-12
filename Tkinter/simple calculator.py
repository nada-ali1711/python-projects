from tkinter import *

app = Tk()

app.title("calculator")

app.minsize(500,500)

number1Label = Label(text="first numbr")

number1Label.pack()

number1Entry = Entry()

number1Entry.pack()



number2Label=Label(text="second number")

number2Label.pack()

number2Entry=Entry()

number2Entry.pack()



def addNum():

    num1=int(number1Entry.get())

    num2=int(number2Entry.get())

    res=num1+num2

    resultLabel = Label(text="The result is " + str(res))

    resultLabel.pack()







but = Button(text="ADD" , command=addNum)

but.pack()









app.mainloop()
