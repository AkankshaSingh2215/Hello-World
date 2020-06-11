import sys
from tkinter import *
import time

def times():
	current_time=time.strftime("%H:%M:%S")
	clock.config(text=current_time)
	clock.after(200,times)

root=Tk()
root.geometry("500x400")
clock=Label(root,font=("times",50,"bold"),bg="pink")
clock.grid(row=2,column=2,pady=25,padx=100)	
times()

digi=Label(root,text="Digital Clock", font ="times 24 bold",bg="red")
digi.grid(row=0,column=2)

notation=Label(root, text="hours minutes seconds",font="times 30 bold",bg="yellow")
notation.grid(row=3,column=2)	

root.mainloop()


