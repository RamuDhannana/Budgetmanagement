import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import date
import mainpage as m

def plan_to_save(user,role):
    usr=user
    rl=role
    root= Tk()
    root.title("Budget Management")
    width = 500 
    height = 500 
    screen_width = root.winfo_screenwidth()  
    screen_height = root.winfo_screenheight() 
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    la1=Label(root,text="Plan for Save Money",fg="red",font=('Times', 24)).place(x = 140,y = 30)
    lb1= Label(root, text="Enter No Of Days:",font=('Times', 16),fg="Blue")  
    lb1.place(x=170, y=120)  
    en1= Entry(root,width=16, font=('Arial 19'))  
    en1.place(x=150, y=150)
    lb2= Label(root, text="Enter Amount To Save:",font=('Times', 16),fg="Blue")  
    lb2.place(x=170, y=220)  
    en2= Entry(root,width=16, font=('Arial 19'))  
    en2.place(x=150, y=250)
    def plan_money():
        days=int(en1.get())
        money=int(en2.get())
        root.destroy()
        mydb2 = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Ramu2002",
              database="mydb"
                )
        mycursor2 = mydb2.cursor()
        today = date.today()
        month=today.month
        y=today.year
        day=today.day
        if day>5:
            day=day-days
        else:
            month=month-1
            day=30-(day-days)
        dat=date(y,month,day)
        sql = "SELECT category,sum(amount) FROM expens WHERE userid = %s and priority >3 and dates between %s and %s and category<>'Health Insurance' group by category  order by priority desc" 
        adr = (usr,dat,today )
        mycursor2.execute(sql, adr)
        myresult = mycursor2.fetchall()
        cat=[]
        am=[]
        for item in myresult:
            cat.append(item[0])
            am.append(int(item[1]))
        real_amt=[]
        i=0
        for cash in am:
            if i < (len(am)//2):
                real_amt.append(0.3*cash)
            else:
                real_amt.append(0.2*cash)
            i+=1
        i=0
        s=0
        count=0
        while i<len(real_amt):
            if s<money:
                s=s+real_amt[i]
                count+=1
            i+=1
        
        if  s> money:
            rem=s-money
            m1=rem//2
            real_amt[count-1]=real_amt[count-1]-m1
            real_amt[count-2]=real_amt[count-2]-m1
        base = Tk()   
        base.geometry("550x550")
        width = 550 # Width 
        height = 550 # Height
        screen_width = base.winfo_screenwidth()  
        screen_height = base.winfo_screenheight() 
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        base.geometry('%dx%d+%d+%d' % (width, height, x, y))
        base.title('Save Plan')    
        lbl_0 = Label(base, text="Plan for Save Money within %d Days"%days,font=("bold",20),fg="blue")   
        lbl_0.place(x=70,y=60)
        lbl_1 =Label(base, text= "(Try To Reduce This Expenses in Particular Category to Save Money)",font=("bold",12))  
        lbl_1.place(x=40,y=110)
        lbl_2 = Label(base, text="--------------------------------------------------------------------",font=("bold",20),fg="blue")   
        lbl_2.place(x=0,y=140)
        yc=200
        s=0
        for i in range(count):
            if real_amt[i]>0:
                lbl_4 =Label(base, text= "%d. %s "%(i,cat[i]),font=("bold",12))  
                lbl_4.place(x=150,y=yc)
                lbl_5 =Label(base, text=": %.1f"%real_amt[i] ,font=("bold",12))  
                lbl_5.place(x=350,y=yc)
                s=s+real_amt[i]
                yc=yc+30
        lbl_6=Label(base, text=" Total Amount u Able To Save:" ,font=("bold",12))  
        lbl_6.place(x=120,y=yc+50)
        lbl_5 =Label(base, text="%.2f"%s ,font=("bold",12))  
        lbl_5.place(x=350,y=yc+50)
        def goback():
            base.destroy()
            m.autherization(usr,rl)
        b2=Button(base,text="Go Back!!",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=goback).place(x = 200,y = 420)
        base.mainloop()   


        
    b1=Button(root,text="Show Plan",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=plan_money).place(x = 190,y = 350)
    root.mainloop()
    
