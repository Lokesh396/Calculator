from tkinter import *
import tkinter.font as font


window=Tk()

window.title("Calculator")

window.configure(bg="#f5c1f3")

myfont=font.Font(family="Helvetica",weight='bold')

p1=PhotoImage(file="calc.png")
window.iconphoto(False,p1)

def clear():
    e1.delete('0',END)
def execute():
    try:
        data=eval(e1_value.get())
        e1.delete('0',END)
        e1.insert(END,data)
    except:
        SyntaxError
        e1.delete('0',END)
        e1.insert(END,"Please check the Expression")
e1_value=StringVar()
e1=Entry(window,width=35,borderwidth=5,textvariable=e1_value)
e1.grid(row=0,column=0,columnspan=4,padx=5,pady=5,ipady=15)

b1=Button(window,padx=34,pady=19,text="7",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"7"))
b1.grid(row=1,column=0)

b2=Button(window,padx=34,pady=19,text="8",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"8"))
b2.grid(row=1,column=1)

b3=Button(window,padx=34,pady=19,text="9",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"9"))
b3.grid(row=1,column=2)

b4=Button(window,padx=24,pady=16,text="AC",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command=clear)
b4.grid(row=1,column=3)
b4['font']=myfont

b20=Button(window,padx=33,pady=17,text="(",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command= lambda :e1.insert(END,"("))
b20.grid(row=2,column=3)
b20['font']=myfont

b5=Button(window,padx=34,pady=19,text="4",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"4"))
b5.grid(row=2,column=0)

b6=Button(window,padx=34,pady=19,text="5",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"5"))
b6.grid(row=2,column=1)

b7=Button(window,padx=34,pady=19,text="6",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"6"))
b7.grid(row=2,column=2)

b8=Button(window,padx=34,pady=19,text="1",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"1"))
b8.grid(row=3,column=0)

b9=Button(window,padx=34,pady=19,text="2",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"2"))
b9.grid(row=3,column=1)

b10=Button(window,padx=34,pady=19,text="3",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert(END,"3"))
b10.grid(row=3,column=2)

b11=Button(window,padx=33,pady=17,text=")",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command= lambda :e1.insert(END,")"))
b11.grid(row=3,column=3)
b11['font']=myfont
b12=Button(window,padx=34,pady=19,text="0",bg="#eff7ed",activebackground="#eaf279",activeforeground='#7d7d77',command= lambda :e1.insert("0"))
b12.grid(row=4,column=0)

b13=Button(window,padx=33,pady=17,text="+",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command= lambda :e1.insert(END,"+"))
b13.grid(row=4,column=1)
b13['font']=myfont

b14=Button(window,padx=35,pady=17,text="-",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command= lambda :e1.insert(END,"-"))
b14.grid(row=4,column=2)
b14['font']=myfont

b15=Button(window,padx=33,pady=17,text=".",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command= lambda :e1.insert(END,"."))
b15.grid(row=4,column=3)
b15['font']=myfont

b16=Button(window,padx=30,pady=19,text="%",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command= lambda :e1.insert(END,"%"))
b16.grid(row=5,column=0)
b16['font']=myfont

b17=Button(window,padx=34,pady=19,text="*",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command= lambda :e1.insert(END,"*"))
b17.grid(row=5,column= 1)
b17['font']=myfont

b18=Button(window,padx=34,pady=19,text="/",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command= lambda :e1.insert(END,"/"))
b18.grid(row=5,column=2)
b18['font']=myfont

b19=Button(window,padx=30,pady=18,text="=",bg="#eff7ed",fg="#eb902f",activebackground="#eb902f",activeforeground="#b7e8e3",command=execute)
b19.grid(row=5,column=3)
b19['font']=myfont

window.mainloop()
