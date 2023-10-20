from tkinter import *
from tkinter import ttk
import pymysql
class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System",bd=10,relief=GROOVE,font=("times-new roman", 40, "bold"), bg="lightgreen", fg="red")
        title.pack(side=TOP, fill=X)

        #---All Variable----

        self.Roll_No_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.DOB_var=StringVar()
        

        #---Manage Frame----

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_Frame,text="Manage Student",bg="crimson",fg="white",font=("time new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_Roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_Roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var,font=("time new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.Email_var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",12,"bold"),state='readonly')
        combo_Gender['values']=("Male","Female","Other")
        combo_Gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_Contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.Contact_var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_DOB = Entry(Manage_Frame, textvariable=self.DOB_var, font=("time new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Address=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=30 ,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #----Button Fram----

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=10,y=530,width=430)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)

        

        #---Detail Frame----
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=850,height=600)

        lbl_search=Label(Detail_Frame,text="Search",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",12,"bold"),state='readonly')
        combo_search['values']=("Roll","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20)


        txt_search=Entry(Detail_Frame,width=20,font=("time new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        #-----Table Frame-----------

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=830,height=510)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_Frame,columns=("Roll No.","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No.",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("Roll No.",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    def add_students(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s,%s)", (
                                                                                self.Roll_No_var.get(),
                                                                                self.Name_var.get(),
                                                                                self.Email_var.get(),
                                                                                self.Gender_var.get(),
                                                                                self.Contact_var.get(),
                                                                                self.DOB_var.get(),
                                                                                self.txt_Address.get('1.0', 'end-1c')
                                                                                ))
        con.commit()
        self.fetch_data()
        con.close()

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()



root = Tk()
obj = student(root)
root.mainloop()

