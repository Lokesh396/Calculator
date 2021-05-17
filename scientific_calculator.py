from tkinter import *
import time
import tkinter.font as font
from math import *
window=Tk()
answ=0
window.title("Scientific Calculator")
window.configure(background="#000000")
window.configure(cursor="mouse")
def allclear():
    e1.delete('0',END)
def delete_one():
    value=e1_value.get()
    e1.delete('0',END)
    e1.insert(END,value[0:-1])
def evaluate():
    try:
        x=eval(e1_value.get())
        e1.delete('0',END)
        e1.insert(END,x)
    except:
        TypeError
        SyntaxError
        ValueError
def degree():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        e1.insert(END,degrees(x))
    except:
        ValueError
        SyntaxError
def radian():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        e1.insert(END,radians(x))
    except:
        ValueError
        SyntaxError   
def fact():
    try:
        x=factorial(int(e1_value.get()))
        answ=x
        e1.delete('0',END)
        e1.insert(END,x)

    except:
        ValueError
        SyntaxError
        e1.delete('0',END)
        e1.insert(END,"please enter a correct value")
def absolute():
    try:
        x=abs(float(e1_value.get()))
        answ=x
        e1.delete('0',END)
        e1.insert(END,x)
    except:
        ValueError
        e1.delete('0',END)
def square_root():
    try:
        x=sqrt(float(e1_value.get()))
        answ=x
        e1.delete('0',END)
        e1.insert(END,x)
    except:
        ValueError
        e1.delete('0',END)
def cube():
    try:
        x=pow(float(e1_value.get()),3)
        answ=x
        e1.delete('0',END)
        e1.insert(END,x)
    except:
        ValueError
        e1.delete('0',END)  
def expo():
    try:
        x=exp(float(e1_value.get()))
        answ=x
        e1.delete('0',END)
        e1.insert(END,x)
    except:
        ValueError
        e1.delete('0',END)
def square():
    try:
        x=pow(float(e1_value.get()),2)
        answ=x
        e1.delete('0',END)
        e1.insert(END,x)
    except:
        ValueError
        e1.delete('0',END) 

def xpowery():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        e1.insert(END,x)
        e1.insert(END,"**") 
    except:
        ValueError
        e1.delete('0',END)  
def sininverse():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        x=asin(x)
        e1.insert(END,degrees(x))
    except:
        SyntaxError
        e1.delete('0',END)
        e1.insert(END,"Synatx Error")
def cosinverse():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        x=acos(x)
        e1.insert(END,degrees(x))
    except:
        SyntaxError
        e1.delete('0',END)
        e1.insert(END,"Synatx Error")
def taninverse():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        x=atan(x)
        e1.insert(END,degrees(x))
    except:
        SyntaxError
        e1.delete('0',END)
        e1.insert(END,"Synatx Error")

def sinca():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        x=sin(radians(x))
        e1.insert(END,x)
    except:
        SyntaxError
        e1.delete('0',END)
        e1.insert(END,"Synatx Error")
def cosca():
    try:
        x=int(e1_value.get())
        e1.delete('0',END)
        x=cos(radians(x))
        e1.insert(END,x)
    except:
        SyntaxError
        e1.delete('0',END)
        e1.insert(END,"Synatx Error")
def tanca():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        if(x==45.0):
            e1.insert(END,"1")
        elif(x== 0.0 or x== 90.0):
            e1.insert("Infinity")
        else:
            x=tan(radians(x))
            e1.insert(END,x)
        
    except:
        SyntaxError
        e1.delete('0',END)
        e1.insert(END,"Synatx Error")
def logc():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        e1.insert(END,log10(x))
    except:
        ValueError
        SyntaxError
        TypeError
def logn():
    try:
        x=float(e1_value.get())
        e1.delete('0',END)
        e1.insert(END,log(x))
    except:
        ValueError
        SyntaxError
        TypeError
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value,borderwidth=6,width=40,bg="#000000",fg="#eeeeee")#cursor="pirate")
e1.grid(row=0,column=0,columnspan=5,padx=5,pady=5,ipady=15)

l1=Label(window,text="Scientific Calculator",width=19,bg="#000000",fg="#eb902f")
l1.grid(row=0,column=5,columnspan=3,padx=5,pady=5,ipady=15)
#1
b1=Button(window,text="(",padx=35.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda : e1.insert(END,"("))
b1.grid(row=1,column=0)
b2=Button(window,text=")",padx=35,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda : e1.insert(END,")"))
b2.grid(row=1,column=1)
b3=Button(window,text="exp",padx=27,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=expo)
b3.grid(row=1,column=2)
b4=Button(window,text="π",padx=33.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=lambda:e1.insert(END,"3.14"))
b4.grid(row=1,column=3)
b5=Button(window,text="AC",padx=28,pady=15,bg="#eb902f",fg="#eeeeee",activebackground="#eeeeee",activeforeground='#eb902f',command=allclear)
b5.grid(row=1,column=4)
b6=Button(window,text="del",padx=27,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=delete_one)
b6.grid(row=1,column=5)
b7=Button(window,text="√",padx=33.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=square_root)
b7.grid(row=1,column=6)
b8=Button(window,text="/",padx=32.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda : e1.insert(END,"/"))
b8.grid(row=1,column=7)

#2

b11=Button(window,text="Deg",padx=25,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=degree)
b11.grid(row=2,column=0)
b12=Button(window,text="Rad",padx=25,pady=15,bg="#000000",fg="#e8dd46",activebackground="#eeeeee",activeforeground='#000000',command=radian)
b12.grid(row=2,column=1)
b13=Button(window,text="x^3",padx=25.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=cube)
b13.grid(row=2,column=2)
b14=Button(window,text="abs",padx=26,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=absolute)
b14.grid(row=2,column=3)
b15=Button(window,text="7",padx=33,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"7"))
b15.grid(row=2,column=4)
b16=Button(window,text="8",padx=33,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"8"))
b16.grid(row=2,column=5)
b17=Button(window,text="9",padx=33.5,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"9"))
b17.grid(row=2,column=6)
b18=Button(window,text="*",padx=31,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda : e1.insert(END,"*"))
b18.grid(row=2,column=7)

#3

b21=Button(window,text="sin",padx=28,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=sinca)
b21.grid(row=3,column=0)
b22=Button(window,text="cos",padx=26.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=cosca)
b22.grid(row=3,column=1)
b23=Button(window,text="tan",padx=28,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=tanca)
b23.grid(row=3,column=2)
b24=Button(window,text="log",padx=28,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=logc)
b24.grid(row=3,column=3)
b25=Button(window,text="4",padx=33,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"4"))
b25.grid(row=3,column=4)
b26=Button(window,text="5",padx=33,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"5"))
b26.grid(row=3,column=5)
b27=Button(window,text="6",padx=34,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"6"))
b27.grid(row=3,column=6)
b28=Button(window,text="-",padx=32,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda : e1.insert(END,"-"))
b28.grid(row=3,column=7)

#4

b31=Button(window,text="sin-1",padx=21.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=sininverse)
b31.grid(row=4,column=0)
b32=Button(window,text="cos-1",padx=21.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=cosinverse)
b32.grid(row=4,column=1)
b33=Button(window,text="tan-1",padx=21.5,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=taninverse)
b33.grid(row=4,column=2)
b34=Button(window,text="ln",padx=32,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=logn)
b34.grid(row=4,column=3)
b35=Button(window,text="1",padx=33,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"1"))
b35.grid(row=4,column=4)
b36=Button(window,text="2",padx=33,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"2"))
b36.grid(row=4,column=5)
b37=Button(window,text="3",padx=33.5,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"3"))
b37.grid(row=4,column=6)
b38=Button(window,text="+",padx=29,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda : e1.insert(END,"+"))
b38.grid(row=4,column=7)

#5

b41=Button(window,text="n!",padx=30,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=fact)
b41.grid(row=5,column=0)
b42=Button(window,text="x^2",padx=25,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=square)
b42.grid(row=5,column=1)
b43=Button(window,text="x^y",padx=25,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command=xpowery)
b43.grid(row=5,column=2)
b44=Button(window,text="ans",padx=27,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",state=DISABLED,activeforeground='#7d7d77')
b44.grid(row=5,column=3)
b45=Button(window,text="0",padx=32,pady=15,bg="#3b3433",fg="#eeeeee",command= lambda : e1.insert(END,"0"))
b45.grid(row=5,column=4)
b46=Button(window,text=".",padx=36,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda : e1.insert(END,"."))
b46.grid(row=5,column=5)
b46=Button(window,text="%",padx=31,pady=15,bg="#000000",fg="#eb902f",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda : e1.insert(END,"%"))
b46.grid(row=5,column=6)
b48=Button(window,text="=",padx=29,pady=15,bg="#eb902f",fg="#eeeeee",activebackground="#eeeeee",activeforeground='#eb902f',command=evaluate)
b48.grid(row=5,column=7)
window.mainloop()