from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root= Tk()
root.title("Alarm")
root.geometry("500x300")



mixer.init()

def th():
	t1 = threading.Thread(target=a, args=())
	t1.set()


def a():

	a = hr.get()
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

head =Label(root,text="ALARM CLOCK",font=('comic sans',20))
head.pack(fill=X)

panel = Frame(root)
panel.place(x=5,y=70)

clock = PhotoImage(file='al.png')

alp = Label(panel,image=clock)
alp.grid(rowspan=4,column=0)


atime = Label(panel,text="Alarm Time \n(Hr:Min:Sec)",font=('comic sans',18))
atime.grid(row=0,column=1,padx=10,pady=5)

hr = Entry(panel,font=('comic sans',20),width=5)
hr.grid(row=0,column=2,padx=10,pady=5)

amessage = Label(panel,text="Message",font=('comic sans',20))
amessage.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

amsg = Entry(panel,font=('comic sans',15),width=25)
amsg.grid(row=2,column=1,columnspan=2,padx=10,pady=5)


set = Button(panel,text="Set alarm",font=('comic sans',20),command=th)
set.grid(row=3,column=1,columnspan=2,padx=10,pady=5)





root.mainloop()