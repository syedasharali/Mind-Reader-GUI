from tkinter import *
from PIL import Image,ImageTk,ImageGrab
import numpy as np
import random

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
        
        
"""This file has been removed to prevent unauthorized duplication. If you need to reach me, please send an email to syedasharali092@gmail.com."""
