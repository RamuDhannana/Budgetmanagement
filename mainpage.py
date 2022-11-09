import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import date
import budgetplan as pl

def autherization(usr,role):
    user=usr
    rl=role
    win = Tk()
    today = date.today()
    d1 = today.strftime("%y-%m-%d")
    win.title("Budget Management")
    width = 900 # Width 
    height = 600 # Height
    screen_width = win.winfo_screenwidth()  
    screen_height = win.winfo_screenheight() 
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    la1=Label(win,text="Today Expenses",bg="yellow",fg="blue",font=('Times', 24)).place(x = 320,y = 10)
    frameChartsLT = Frame(win,width=200)
    frameChartsLT.place(x = 130,y = 70)
    mydb1 = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Ramu2002",
              database="mydb"
            )
    mycursor1 = mydb1.cursor()
    sql = "SELECT category,sum(amount) FROM expens WHERE userid ='%s' and dates ='%s' group by category"%(user,d1)
    mycursor1.execute(sql)
    myresult = mycursor1.fetchall()
    cat=[]
    am=[]
    for item in myresult:
        cat.append(item[0])
        am.append(int(item[1]))

    fig = Figure() # create a figure object
    ax = fig.add_subplot(111) # add an Axes to the figure

    ax.pie(am, radius=1, labels=cat,autopct='%0.2f%%', shadow=True,)

    chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
    chart1.get_tk_widget().pack()
    def add_exp():
        win.destroy()
        win1= Tk()
        win1.geometry("500x500")
        width = 500 # Width 
        height = 350 # Height
        screen_width = win1.winfo_screenwidth()  
        screen_height = win1.winfo_screenheight() 
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        win1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        la1=Label(win1,text="ADD EXPENDITURE",bg="yellow",fg="blue",font=('Times', 24)).place(x = 120,y = 10)
        menu= StringVar()
        menu.set("Select Expenditure")
        lbl_3 = Label(win1, text="Select Expenditure:", width=20,font=("bold",14))  
        lbl_3.place(x=40,y=120) 
        drop=OptionMenu(win1, menu,"Education purpose","Housing or Rent", "Travel Expenses","Groceries","Bills","CellPhone","Pet Food and Care","Clothing","Health Insurance","Entertainment","FastFOOd","Medical","others")
        drop.place(x = 250,y = 120)
        lbl_5=Label(win1, text ="Enter Amount:", width=20,font=("bold",14))  
        lbl_5.place(x=70,y=180)
        enter_4 = Entry(win1,width=20)  
        enter_4.place(x=270,y=180)
        def addexp():
            if rl== 'Student':
                pr={"Education purpose":1,"Housing or Rent":3,"Travel Expenses":4,"Groceries":2,"Bills":5,"CellPhone":9,"Pet Food and Care":10,"Clothing":6,"Health Insurance":7,"Entertainment":12,"FastFOOd":13,"Medical":0,"others":15}
            else:
                pr={"Education purpose":4,"Housing or Rent":1,"Travel Expenses":3,"Groceries":2,"Bills":2,"CellPhone":9,"Pet Food and Care":10,"Clothing":6,"Health Insurance":7,"Entertainment":12,"FastFOOd":13,"others":15,"Medical":0}
            today = date.today()
            d1 = today.strftime("%y-%m-%d")
            categ=menu.get()
            amt=enter_4.get()
            mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Ramu2002",
              database="mydb"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO expens (userid,dates,category,amount,priority) VALUES (%s, %s,%s,%s,%s)"
            val=(user,d1,categ,amt,pr[categ])
            mycursor.execute(sql,val)
            mydb.commit()
            win1.destroy()
            autherization(user,rl)
        b2=Button(win1,text="ADD",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=addexp).place(x = 200,y = 240)
        win1.mainloop()

        
    def show():
        win.destroy()
        win2 = Tk()
        win2.title("Budget Management")
        width = 850 # Width 
        height = 600 # Height
        screen_width = win2.winfo_screenwidth()  
        screen_height = win2.winfo_screenheight() 
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        win2.geometry('%dx%d+%d+%d' % (width, height, x, y))
        frame = Frame(win2, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        la1=Label(win2,text="THIS Month EXPENSES",bg="yellow",fg="blue",font=('Times', 24)).place(x = 250,y = 10)
        frameChartsLT = Frame(win2,width=200)
        frameChartsLT.place(x = 130,y = 70)
        mydb2 = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Ramu2002",
              database="mydb"
                )
        mycursor2 = mydb2.cursor()
        month=today.month
        y=today.year
        
        sql = "SELECT category,sum(amount) FROM expens WHERE userid ='%s' and  month(dates)=%d and year(dates)=%d group by category"%(user,month,y)
        mycursor2.execute(sql)
        myresult = mycursor2.fetchall()
        cat=[]
        am=[]
        for item in myresult:
            cat.append(item[0])
            am.append(int(item[1]))

        fig = Figure() # create a figure object
        ax = fig.add_subplot(111) # add an Axes to the figure

        ax.pie(am, radius=1, labels=cat,autopct='%0.2f%%', shadow=True,)

        chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
        chart1.get_tk_widget().pack()
        lbl_3 = Label(win2, text="TOTAL EXPENSES:%d"%sum(am), width=20,font=("bold",12),fg="blue")  
        lbl_3.place(x=330,y=490)
        def close():
            win2.destroy()
            print("Thank U")
        b1=Button(win2,text="GO BACK",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=close).place(x = 350,y = 510)
        win2.mainloop()
    def plan():
        win.destroy()
        pl.plan_to_save(usr,rl)
        
    b1=Button(win,text="Add Expenditure",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=add_exp).place(x = 150,y = 500)
    b2=Button(win,text="Plan To Save",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=plan).place(x = 580,y = 500)
    b3=Button(win,text="Show Month Expenses",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=show).place(x = 370,y = 500)
    win.mainloop()
