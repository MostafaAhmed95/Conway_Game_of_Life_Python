from tkinter import *
top = Tk()
top.geometry('300x300')
c = Canvas(top,height=300, width=300)
for i in range (0,300,20):
    l=c.create_line(i,0,i,300,width=3)
    l=c.create_line(0,i,300,i,width=3)
c.pack()
top.mainloop()
