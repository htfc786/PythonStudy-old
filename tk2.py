from tkinter import*
win = Tk()
win.title("实验程序")
win.geometry("500x500+200+50")
def p():
    print(1)
Label(win,text="欢迎来到实验程序").pack()
Button(win,text = "1",width = 1,height = 1,command = p).pack()
f = Frame(win)
f.pack()
f1 = Frame(f)
s = Scrollbar(win,orient=VERTICAL)
s.pack(fill=Y, side=RIGHT)
t = Text(win,yscrollcommand=s.set)
t.pack()
s.config(command=t.yview)
f1.pack(side = LEFT)
win.mainloop()