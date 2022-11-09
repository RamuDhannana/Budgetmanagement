import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
import mainpage as m

def check():
    win.destroy()
    root= Tk()
    root.title("Budget Management")
    width = 500 
    height = 500 
    screen_width = root.winfo_screenwidth()  
    screen_height = root.winfo_screenheight() 
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    la1=Label(root,text="LOGIN",fg="red",font=('Times', 24)).place(x = 190,y = 30)
    lb1= Label(root, text="Enter User Name",font=('Times', 16),fg="Blue")  
    lb1.place(x=170, y=120)  
    en1= Entry(root,width=16, font=('Arial 19'))  
    en1.place(x=150, y=150)
    lb2= Label(root, text="Enter Password",font=('Times', 16),fg="Blue")  
    lb2.place(x=170, y=220)  
    en2= Entry(root,width=16, font=('Arial 19'),show="*")  
    en2.place(x=150, y=250)
    def validation():
        username=en1.get()
        password=en2.get()
        mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Ramu2002",
              database="mydb"
            )
        mycursor = mydb.cursor()
        sql = "SELECT name,password,role FROM users WHERE name = %s"
        adr = (username, )
        mycursor.execute(sql, adr)
        myresult = mycursor.fetchall()
        if len(myresult)>=1:
            if password==myresult[0][1]:
                root.destroy()
                m.autherization(username,myresult[0][2])
            else:
                print("password inCorrect")
        else:
            print("Invalid User!!!")
        
        
    b1=Button(root,text="Login",bg="#DEDEDE",fg="red", width=15,activebackground="#7C7CFC",command=validation).place(x = 190,y = 300)
    lb3= Label(root, text="Don't Have Account click New--> ",font=('Times', 13),fg="blue")  
    lb3.place(x=70, y=400)
    b2=Button(root,text="Create New",bg="#DEDEDE",fg="red", width=15,activebackground="#7C7CFC",command=register).place(x = 350,y = 400)
    root.mainloop()

def register():
    base = Tk()   
    base.geometry("550x550")
    width = 550 # Width 
    height = 550 # Height
    screen_width = base.winfo_screenwidth()  
    screen_height = base.winfo_screenheight() 
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    base.geometry('%dx%d+%d+%d' % (width, height, x, y))
    base.title('Registration form')    
    lbl_0 = Label(base, text="Registration form", width=20,font=("bold",20))   
    lbl_0.place(x=90,y=60)    
    lbl_1 =Label(base, text= "Enter UserName", width=20,font=("bold",10))  
    lbl_1.place(x=80,y=130)  
    enter_1 = Entry(base)  
    enter_1.place(x=240,y=130)  
    lbl_3 = Label(base, text="Enter Email", width=20,font=("bold",10))  
    lbl_3.place(x=68,y=180)    
    enter_3 = Entry(base)  
    enter_3.place(x=240,y=180)      
    menu= StringVar()
    menu.set("select Role")
    lbl_3 = Label(base, text="select Role:", width=20,font=("bold",11))  
    lbl_3.place(x=70,y=230) 
    drop=OptionMenu(base, menu,"Student","employee")
    drop.place(x = 250,y = 230)   
    lbl_5=Label(base, text ="Enter Password", width=20,font=("bold",11))  
    lbl_5.place(x=70,y=280)
    enter_4 = Entry(base)  
    enter_4.place(x=240,y=280)
    lbl_5=Label(base, text ="Re-Enter Password", width=20,font=("bold",11))  
    lbl_5.place(x=70,y=320)
    enter_5 = Entry(base)  
    enter_5.place(x=240,y=320)
    def insrt():
        user=enter_1.get()
        email=enter_3.get()
        gender=menu.get()
        print(gender)
        password=enter_4.get()
        mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Ramu2002",
              database="mydb"
            )
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (name,email,password,role) VALUES (%s, %s,%s,%s)"
        val = (user,email,password,gender)
        mycursor.execute(sql, val)
        mydb.commit()
        base.destroy()
        check()

        
    Button(base, text='Submit' , width=20, bg="black",fg='white',command=insrt).place(x=180,y=380)    
    base.mainloop()  

   
win = Tk()
win.title("Budget Management")
width = 700 # Width 
height = 500 # Height
screen_width = win.winfo_screenwidth()  
screen_height = win.winfo_screenheight() 

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
win.geometry('%dx%d+%d+%d' % (width, height, x, y))
frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("img.jpg"))
label = Label(frame, image = img)
label.pack()
la1=Label(win,text="BUDGET MANAGEMENT",bg="yellow",fg="blue",font=('Times', 24)).place(x = 150,y = 30)
b1=Button(win,text="Login Here",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=check).place(x = 190,y = 450)
b2=Button(win,text="Register",bg="#DEDEDE",fg="red", width=20,activebackground="#7C7CFC",command=register).place(x = 380,y = 450)
win.mainloop()

