# Message boxes:
from tkinter import *
from tkinter import messagebox  # import messagebox library


# There is a few different message dialog boxes that can be used
def infomessagebox():
   messagebox.showinfo(title="This is an info message box", message="This is an info message")


def warningmessagebox():
   while True:  # message will continue to appear when user tries to exit
       messagebox.showwarning(title="WARNING!", message="This is an endless warning message")


def showerror():
   messagebox.showerror(title="Error!", message="Something went wrong")


def askokcancel():
   # returns either true or false depending on what is clicked
   if (messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the thing?")):
       print("you did the thing")
   else:
       print("you canceled the thing")


def askretrycancel():
   # returns either true or false depending on what is clicked
   if (messagebox.askretrycancel(title="ask retry cancel", message="Do you want to retry the thing?")):
       print("you retried the thing")
   else:
       print("you canceled the thing")


def askyesno():
   # returns either true or false depending on what is clicked
   if (messagebox.askyesno(title="ask yes or no", message="Do you want to click yes or no?")):
       print("you clicked yes")
   else:
       print("you clicked no")


def askquestion():
   # The variable answer will be yes or no
   answer = messagebox.askquestion(title="ask question", message="Do you like to code?")
   if (answer =="yes"):
       print("you like to code")
   else:
       print("you don't like to code")


def askyesnocancel():
   # The variable answer will True,False or None depending on what is clicked
   answer = messagebox.askyesnocancel(title="ask yes no cancel", message="Do you like to code?",icon="error")
   if (answer == True):
       print("you like to code")
   elif (answer == False):
       print("you don't like to code")
   else:
       print("you have dodged the question")


   #The option icon=the icon of a message box can be changed to-"info","warning","error"etc...


window = Tk()
window.title("window for message boxes buttons")
window.resizable(False, False)


infobutton = Button(window, command=infomessagebox, text="click me for info message")
infobutton.pack()


warningbutton = Button(window, command=warningmessagebox, text="click me for an endless warning message")
warningbutton.pack()


errorbutton = Button(window, command=showerror, text="click me for an error message")
errorbutton.pack()


askokcancelbutton = Button(window, command=askokcancel, text="click me for an askokcancel message box")
askokcancelbutton.pack()


askretrycancelbutton = Button(window, command=askretrycancel, text="click me for an ask retry cancel message box")
askretrycancelbutton.pack()


askyesnobutton = Button(window, command=askyesno, text="click me for an ask yes no message box")
askyesnobutton.pack()


askquestionbutton = Button(window, command=askquestion, text="click me for an ask question message box")
askquestionbutton.pack()


askyesnocancelbutton = Button(window, command=askyesnocancel, text="click me for an ask yes no cancel message box")
askyesnocancelbutton.pack()


window.mainloop()