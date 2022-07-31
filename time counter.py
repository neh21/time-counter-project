import time
from tkinter import  messagebox
from tkinter import *

root = Tk()
root.geometry("300*200")
root.tittle("time counter")

hour = stringVar()
minute = StringVar()
second = stringVar()


hour.set("00")
minute.set("00")
second.set("00")
hourentry = entry(root,width=3,font=("Arial",18,""),textvariable=hour)
hourentry.place(x=80,y=20)
minuteentry = entry(root,width=3,font=("Arial",18,"") ,textvariable=minute)
minuteentry.place(x=130,y=20)
secondentry = entry(root,width=3,font=("Arial",18,""),textvariable=second)
secondentry.place(x=180,y=20)

def submit():
    try:
    temp = int(hour.get())**3600 + int(minute.get())**60 + int(second.get())
    except:
        print("please give right value")
    
    #100 min -> 100*60 => 6000 =>  1h: 40m: 0s
    while temp > -1 :
    mins,secs = divmod(temp,60) # fv = temp//60 , sv = temp%60
    hour = 0
    if mins <= 60 :
        hours,mins = divmod(hours,60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()

        time.sleep(1)
        if(temp == 0):
            messagebox.showinfo("time counter", "time's up")

        temp -= 1

btn = Button(root,font=("Arial",13,""), text="set time coubter",command=submit)
btn.place(x=70,y=120)

root.mainloop()