from tkinter import *

#Function for click bind event
def click(event):
    global sc_value
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screen.get())
        except Exception as e:
            print(e)
            value = "Error"
        sc_value.set(value)
        screen.update()

    elif text == "C":
        sc_value.set("")
        screen.update()
    else:
        sc_value.set(sc_value.get()+text)
        screen.update()

root = Tk()
# 
root.geometry("400x550")
root.maxsize(400,550)
root.minsize(400,550)
root.title("Calculator by Muhammad Jalal")
root.wm_iconbitmap("Calculator_icon.ico")
root.config(bg="grey10")
# 
# Creating entry or screen to write in calc
sc_value = StringVar()
sc_value.set("")
screen = Entry(root,relief=SUNKEN,textvariable=sc_value,font="Arial 25 bold",bg="grey",highlightbackground="grey20")
screen.pack(fill=X,padx=10,pady=10,ipady=5)
# 
b_list = ["9","8","7","6","5","4","3","2","1","0","=","+","-","*","/","C",".","00"]
inc = 0
for i in range(0,6):
    f = Frame(root,bg="grey10",padx=12,border=2)
    for j in range(0,3):
        if(inc<10):
            b = Button(f,text=b_list[inc],font="Arial 18 bold",padx=40,pady=7,relief=GROOVE,bg="grey",activebackground="grey40")
            b.pack(padx=6,pady=6,side=LEFT)
            b.bind('<Button-1>',click)
        if(inc==10):
            b1 = Button(f,text=".",font="Arial 19 bold",padx=42,pady=7,relief=GROOVE,bg="grey",activebackground="grey40")
            b1.pack(padx=7,pady=6,side=LEFT)
            b1.bind("<Button-1>",click)
        if(inc==11):
            b1 = Button(f,text="=",font="Arial 18 bold",padx=40,pady=7,relief=GROOVE,bg="grey",activebackground="grey40")
            b1.pack(padx=6,pady=6,side=LEFT)
            b1.bind("<Button-1>",click)
        if(inc==12):
            b1 = Button(f,text="+",font="Arial 18 bold",padx=40,pady=0,relief=GROOVE,bg="grey",activebackground="grey40")
            b1.pack(padx=6,pady=6,side=LEFT,ipady=10)
            b1.bind("<Button-1>",click)
        if(inc==13):
            b1 = Button(f,text="-",font="Arial 20 bold",padx=40,pady=7,relief=GROOVE,bg="grey",activebackground="grey40")
            b1.pack(padx=6,pady=6,side=LEFT)
            b1.bind("<Button-1>",click)
        if(inc==14):
            b1 = Button(f,text="*",font="Arial 20 bold",padx=40,pady=7,relief=GROOVE,bg="grey",activebackground="grey40")
            b1.pack(padx=6,pady=6,side=LEFT)
            b1.bind("<Button-1>",click)
        if(inc==15):
            b1 = Button(f,text="/",font="Arial 23 bold",padx=40,pady=7,relief=GROOVE,bg="grey",activebackground="grey40")
            b1.pack(padx=6,pady=6,side=LEFT)
            b1.bind("<Button-1>",click)
        if(inc==16):
            b1 = Button(f,text="C",font="Arial 16 bold",padx=40,pady=7,relief=GROOVE,bg="grey",activebackground="grey40")
            b1.pack(padx=6,pady=6,side=LEFT)
            b1.bind("<Button-1>",click)
        if(inc==17):
            b1 = Button(f,text="00",font="Arial 18 bold",padx=40,pady=7,relief=GROOVE,bg="grey",activebackground="grey40")
            b1.pack(padx=6,pady=6,side=LEFT)
            b1.bind("<Button-1>",click)
        inc+=1
    f.pack(fill=X)
# 
root.mainloop()