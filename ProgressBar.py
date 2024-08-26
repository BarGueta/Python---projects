# Progress bar:
from tkinter import *
from tkinter.ttk import *
import time
from tkinter import messagebox


def start():
   GB = 100
   download = 0  # The current task
   speed = 1
   bar['value'] = 0  # Restarts the value of the progress bar when clicking the button
   while (download < GB):
       time.sleep(0.05)
       bar['value'] += (speed / GB) * 100  # The value of the progress bar will increment by 1 percent in every iteration
       download += speed
       percent.set(str(int((download / GB) * 100)) + "%")
       text.set(str(download) + "/" + str(GB) + " GB completed")
       window.update_idletasks()  # After each iteration of the while loop it is going to update the window
   messagebox.showinfo(title="Info", message="Download is completed!")


window = Tk()
window.resizable(False, False)

percent = StringVar()  # to update the variable percent with a new text
text = StringVar()  # to update the variable text with a new text


bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)


# Orientation can be vertical too…


percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()


# textvariable - to update the label with some text after each iteration of the while loop


button = Button(window, text="download", command=start).pack()


window.mainloop()
