from tkinter import *
root=Tk()
def f1():
    print('This is New project')
def f2():
    print('This is New')
def f3():
    print('This is Open')
def f4():
    print('This is Save')
def f5():
    print('This is Settings')
def f6():
    print('This is Print')


mymenu=Menu(root)
root.config(menu=mymenu)
sm1=Menu(mymenu)
mymenu.add_cascade(label='file')
sm1.add_command(label='New project',command=f1)
sm1.add_command(label='New',command=f2)
sm1.add_separator()
sm1.add_command(label='Open',command=f3)
sm1.add_command(label='Save',command=f4)
sm1.add_separator()

sm1.add_command(label='Settings',command=f5)
sm1.add_command(label='Print',command=f6)

sm2=Menu(mymenu)
mymenu.add_cascade(label='Edit')
sm2.add_command(label='New project',command=f1)
sm2.add_command(label='New',command=f2)
sm2.add_separator()
sm2.add_command(label='Open',command=f3)
sm2.add_command(label='Save',command=f4)
sm2.add_separator()

sm2.add_command(label='Settings',command=f5)
sm2.add_command(label='Print',command=f6)
root.mainloop()
