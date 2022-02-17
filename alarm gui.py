from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root= Tk()
root.title("SIMMI'S Alarm")
root.geometry("650x400")
root.iconbitmap('Logo.ico')



mixer.init()

def th():
	t1 = threading.Thread(target=a, args=())
	t1.start()


def a():

	a = f"{hr.get()}:{min.get()}:{sec.get()}"
	if a == "":
		msg = messagebox.showerror('Invalid data','Please enter valid time')
	else:
		Alarmtime= a
		CurrentTime = time.strftime("%H:%M:%S")

		while Alarmtime != CurrentTime:
			CurrentTime = time.strftime("%H:%M:%S")
			
		if Alarmtime == CurrentTime:
			mixer.music.load('tone.mp3')
			mixer.music.play()
			msg = messagebox.showinfo('It is time',f'{amsg.get()}')
			if msg == 'ok':
				mixer.music.stop()



header =Frame(root)
header.place(x=5,y=5)

head =Label(root,text="ALARM CLOCK",font=('poppings',22))
head.pack(fill=X)

panel = Frame(root)
panel.place(x=5,y=70)

imageClock = PhotoImage(file='AlarmClock.png')

img = Label(panel,image=imageClock)
img.grid(rowspan=5,column=0,columnspan=1)


alarmtime = Label(panel,text="Alarm Time \n(24 hour format)",font=('comic sans',17))
alarmtime.grid(row=1,column=2,padx=5,pady=5)

timeFormat = Label(panel,text = "Hour        Min        Sec   ",font=60)
timeFormat.grid(row=0,column=3,columnspan=4,padx=5,pady=5)
# The Variables we require to set the alarm(initialization):
hr = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hr= Entry(panel,textvariable = hr,font=('comic sans',20),bg = "pink",width = 4)
hr.grid(row=1,column=3,padx=5,pady=5)
min= Entry(panel,textvariable = min,font=('comic sans',20),bg = "pink",width = 4)
min.grid(row=1,column=4,padx=5,pady=5)
sec = Entry(panel,textvariable = sec,font=('comic sans',20),bg = "pink",width = 4)
sec.grid(row=1,column=5,padx=5,pady=5)

amessage = Label(panel,text="Message",font=('comic sans',16))
amessage.grid(row=2,column=2,columnspan=2,padx=5,pady=5)

amsg = Entry(panel,font=('comic sans',15),width=25)
amsg.grid(row=3,column=2,columnspan=3,padx=5,pady=5)


set = Button(panel,text="Set alarm",fg="red",font=('comic sans',20),command=th)
set.grid(row=4,column=2,columnspan=3,padx=5,pady=5)





root.mainloop()