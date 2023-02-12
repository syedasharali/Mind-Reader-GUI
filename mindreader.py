from tkinter import *
from PIL import Image,ImageTk,ImageGrab
import numpy as np
import random
from math import ceil
import time as t

count=0
yes_list=[]
no_list=[]

ar=np.array([
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63],
    [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59, 62, 63],
    [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 63],
    [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62,63],
    [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
    [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]])

def calculate():
    global ar_temp,lr,set_temp
    
    set_temp=set(ar[yes_list[0]-1])
    for i in range(1,len(yes_list)):
        set_temp = set(set_temp & set(ar[yes_list[i]-1]))
    for i in range(len(no_list)):
        set_temp = set(set_temp - set(ar[no_list[i]-1]))
    lr=Label(root,text=f'YOUR NUMBER IS \n{list(set_temp)[0]}',font=('Lucida Console',55,'bold'),justify='center',bg='white',fg=random.choice(('black','blue','red','green')),wraplength=x-x/4,anchor='center')
    lr.place(x=x/2-x/4 ,y=y/2-y/10)
    root.bind('<Button-1>',redo)
        

def yes():
    global count,yes_list
    f1.destroy
    b1.config(state=DISABLED)
    root.after(300, enable_button)
    root.update()
    count+=1
    if count>=6:
        lp1.destroy()
        l1.destroy()
        b1.destroy()
        b2.destroy()
        yes_list.append(count)
        calculate()
    else:
        for i in range(1,6):
            if count==i:
                yes_list.append(i)
        lp1['image']=image_list[count]
    
        
def no():
    global count,no_list
    b2.config(state=DISABLED)
    root.after(300, enable_button)
    root.update()
    count+=1
    if count>=6:
        lp1.destroy()
        l1.destroy()
        b1.destroy()
        b2.destroy()
        no_list.append(count)
        if 0<=len(no_list)>=6:
            Label(root,text="You Haven't Choose Any NUMBER!!",font=('Lucida Console',40,'bold'),justify='center',bg='white',wraplength=x-x/4,anchor='center').place(x=x/8,y=y/2-y/10)
            root.bind('<Button-1>',redo)
        else:
            calculate()
    else:
        for i in range(1,6):
            if count==i:
                no_list.append(i)
        lp1['image']=image_list[count]
        
def enable_button():
    try:
        b1.configure(state="normal")
        b2.configure(state="normal")
    except:
        pass

def redo(evt):
    global yes_list,no_list,count
    f1.destroy()
    lr.destroy()
    yes_list=[]
    no_list=[]
    count=0
    root.unbind('<Button-1>')
    do()

def do():
    global lp1,b1,b2,ld,l1,f1
    try:
        l.destroy()
        b.destroy()
    except:
        pass
    f1=Frame(root,bg='white')
    f1.pack(expand=TRUE)
    lp1=Label(f1,image=image_list[0])
    lp1.grid(row=0,column=0,columnspan=13)
    b1=Button(f1,text='Yes',font=('Comic Sans MS', 40),bg='white',fg='blue',command=yes)
    b1.grid(row=1,column=2,padx=15,pady=5,sticky=NSEW)
    b2=Button(f1,text='No',font=('Comic Sans MS', 40),bg='white',fg='red',command=no)
    b2.grid(row=1,column=3,padx=15,pady=5,sticky=NSEW,ipady=0)
    ld=Label(f1,text='                               ',bg='white')
    ld.grid(row=1,column=0,pady=15,sticky=NSEW)
    l1=Label(f1,text='Can you see your number?',font=('Georgia', 40, 'bold'),bg='white')
    l1.grid(row=1,column=1,pady=15,sticky=NSEW)
    root.mainloop()

root=Tk()
root.configure(background='white')
root.iconbitmap('data/magic.ico')
root.title('Magic')
x=root.winfo_screenwidth()
y=root.winfo_screenheight()
root.geometry(f'{x-100}x{y-100}')
root.minsize(400,400)
l=Label(root,text='Think of a NUMBER between 1 and 63',font=('Lucida Console',55,'bold'),justify='center',bg='white',wraplength=x-x/4,anchor='center')
l.place(x=x/2-x/4 ,y=y/2-y/10)
b=Button(root,text='Ready!',font=('Comic Sans MS', 40),bg='white',command=do)
b.place(x=x/2-100 ,y=y/2+100)
a1 = np.load("data/a1.npy")
a2 = np.load("data/a2.npy")
a3 = np.load("data/a3.npy")
a4 = np.load("data/a4.npy")
a5 = np.load("data/a5.npy")
a6 = np.load("data/a6.npy")
im1=Image.fromarray(np.uint8(a1))
im2=Image.fromarray(np.uint8(a2))
im3=Image.fromarray(np.uint8(a3))
im4=Image.fromarray(np.uint8(a4))
im5=Image.fromarray(np.uint8(a5))
im6=Image.fromarray(np.uint8(a6))
im1=im1.resize((x-100,y-220))
im2=im2.resize((x-100,y-220))
im3=im3.resize((x-100,y-220))
im4=im4.resize((x-100,y-220))
im5=im5.resize((x-100,y-220))
im6=im6.resize((x-100,y-220))
img1=ImageTk.PhotoImage(im1)
img2=ImageTk.PhotoImage(im2)
img3=ImageTk.PhotoImage(im3)
img4=ImageTk.PhotoImage(im4)
img5=ImageTk.PhotoImage(im5)
img6=ImageTk.PhotoImage(im6)
image_list=[img1,img2,img3,img4,img5,img6]


root.mainloop()