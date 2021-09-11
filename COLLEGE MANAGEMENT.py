def addteacher():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d:%m:%Y")
        try:
            strr='insert into teacherdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res=messagebox.askyesnocancel('Notifications','Id {},Name {} Added successfully.. and want to clean the form'.format(id,name),parent=addroot)
            if (res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror('Notifications','Id Already Exist try another Id...',parent=addroot)
        strr='select * from teacherdata1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        teachertable.delete(*teachertable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            teachertable.insert('',END,values=vv)





    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Teacher Management System')
    addroot.config(bg='light grey')
    addroot.iconbitmap('manage.ico')
    addroot.resizable(False,False)
    #--------------------------------------add teacher labels---------------------------------#
    idlabel=Label(addroot,text='Enter Id:',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text='Enter Name:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    ##-------------------------------Add Teacher Entry--------------------------------##
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()

    identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
    #-----------------------------------------addbutton---------------------------#
    submitbtn=Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='grey',command=submitadd)
    submitbtn.place(x=150,y=420)
    addroot.mainloop()

def searchteacher():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate=time.strftime("%d:%m:%Y")
        if (id!=''):
            strr='select * from teacherdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas=mycursor.fetchall()
            teachertable.delete(*teachertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                teachertable.insert('', END, values=vv)


        elif (name!=''):
            strr='select * from teacherdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas=mycursor.fetchall()
            teachertable.delete(*teachertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                teachertable.insert('', END, values=vv)

        elif (mobile!=''):
            strr='select * from teacherdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas=mycursor.fetchall()
            teachertable.delete(*teachertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                teachertable.insert('', END, values=vv)

        elif (email!=''):
            strr='select * from teacherdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas=mycursor.fetchall()
            teachertable.delete(*teachertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                teachertable.insert('', END, values=vv)

        elif (address!=''):
            strr='select * from teacherdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas=mycursor.fetchall()
            teachertable.delete(*teachertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                teachertable.insert('', END, values=vv)

        elif (gender!=''):
            strr='select * from teacherdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas=mycursor.fetchall()
            teachertable.delete(*teachertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                teachertable.insert('', END, values=vv)

        elif (dob!=''):
            strr='select * from teacherdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas=mycursor.fetchall()
            teachertable.delete(*teachertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                teachertable.insert('', END, values=vv)

        elif (addeddate!=''):
            strr='select * from teacherdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas=mycursor.fetchall()
            teachertable.delete(*teachertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                teachertable.insert('', END, values=vv)

    searchroot=Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Teacher Management System')
    searchroot.config(bg='white')
    searchroot.iconbitmap('manage.ico')
    searchroot.resizable(False,False)
    #--------------------------------------add teacher labels---------------------------------#
    idlabel=Label(searchroot,text='Enter Id:',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot, text='Enter Name:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter D.O.B:',  font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)


    ##-------------------------------Add Teacher Entry--------------------------------##
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()


    identry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)


    #-----------------------------------------addbutton---------------------------#
    submitbtn=Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='grey',command=search)
    submitbtn.place(x=150,y=480)
    searchroot.mainloop()

def deleteteacher():
   cc=teachertable.focus()
   content=teachertable.item(cc)
   pp=content['values'][0]
   strr='delete from teacherdata1 where id=%s'
   mycursor.execute(strr,(pp))
   con.commit()
   messagebox.showinfo('Notifications','Id {} deleted successfully...'.format(pp))
   strr='select * from teacherdata1'
   mycursor.execute(strr)
   datas = mycursor.fetchall()
   teachertable.delete(*teachertable.get_children())
   for i in datas:
       vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
       teachertable.insert('', END, values=vv)




def updateteacher():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date=dateval.get()
        time=timeval.get()

        strr='update teacherdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications','Id {} Modified successfully...'.format(id),parent=updateroot)
        strr = 'select * from teacherdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        teachertable.delete(*teachertable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            teachertable.insert('', END, values=vv)

    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Teacher Management System')
    updateroot.config(bg='white')
    updateroot.iconbitmap('manage.ico')
    updateroot.resizable(False,False)
    #--------------------------------------add teacher labels---------------------------------#
    idlabel=Label(updateroot,text='Enter Id:',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot, text='Enter Name:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile:',  font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email:', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address:',  font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender:',  font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B:',  font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date:',  font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time:',  font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)

    ##-------------------------------Add Teacher Entry--------------------------------##
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()

    identry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)
    #-----------------------------------------addbutton---------------------------#
    submitbtn=Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='grey',command=update)
    submitbtn.place(x=150,y=540)
    cc=teachertable.focus()
    content=teachertable.item(cc)
    pp=content['values']
    if(len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()


def showteacher():
    strr = 'select * from teacherdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    teachertable.delete(*teachertable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        teachertable.insert('', END, values=vv)


def exportteacher():
    ff=filedialog.asksaveasfilename()
    gg=teachertable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=teachertable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','Teacher data is saved{}...'.format(paths))

def exitteacher():
    res=messagebox.askyesnocancel('Notifications','Do you want to exit?')
    if (res==True):
        root.destroy()



##########################################CONNECTION OF THE DATABASE###########################################
def Connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()


        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr='create database teachermanagementsystem1'
            mycursor.execute(strr)
            strr='use teachermanagementsystem1'
            mycursor.execute(strr)
            strr='create table teacherdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr='alter table teacherdata1 modify column id int not null'
            mycursor.execute(strr)
            strr='alter table teacherdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'database created and now you are connected...',parent=dbroot)
        except:
            strr='use teachermanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database....',parent=dbroot)
        dbroot.destroy()




    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('manage.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='white')
    #------------------------------Connectdb Labels------------------------------------------------#
    hostlabel=Label(dbroot,text="Enter Host:",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter User:",  font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password:",  font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    passwordlabel.place(x=10, y=130)
    #-------------------------------------------Connectdb Entry-------------------------------------#
    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()

    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    ################################################Connectdb Button##################################
    submitbutton=Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='grey',bd=5,width=20,activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()
###################################
def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%Y")
    clock.config(text='Date:'+date_string+"\n"+"Time:"+time_string)
    clock.after(200,tick)

#######################################INTRO SLIDER##################################
import random
colors=['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)




def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count=0
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
        count +=1
    SliderLabel.after(200,IntroLabelTick)





#######################################################################################################
from tkinter import*
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
import pandas
root=Tk()
root.title('Teacher Profile')
root.config(bg='light grey')
root.geometry('1174x700+200+50')
root.iconbitmap('manage.ico')
root.resizable(False,False)
###########################################Frames#########################################
##--------------------------------------------------------------Data Entry Frame---------------------------------------------##

DataEntryFrame=Frame(root,bg='grey',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

frontlabel=Label(DataEntryFrame,text='--------------Welcome-------------',width=30,font=('arial',22,'italic bold'),bg='light grey')
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(DataEntryFrame,text='1. Add Teacher',width=25,font=('times',15,'bold'),bd=6,bg='Sky blue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addteacher)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. Search Teacher ',width=25,font=('times',15,'bold'),bd=6,bg='Sky blue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchteacher)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. Delete Teacher',width=25,font=('times',15,'bold'),bd=6,bg='Sky blue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deleteteacher)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. Update Teacher',width=25,font=('times',15,'bold'),bd=6,bg='Sky blue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updateteacher)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEntryFrame,text='5. Show All',width=25,font=('times',15,'bold'),bd=6,bg='Sky blue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showteacher)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. Export Data',width=25,font=('times',15,'bold'),bd=6,bg='Sky blue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportteacher)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. Exit',width=25,font=('times',15,'bold'),bd=6,bg='Sky blue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitteacher)
exitbtn.pack(side=TOP,expand=True)

##-----------------------------------------------------------------------Show Data Frames------------------------##
ShowDataFrame=Frame(root,bg="light grey",relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

##=================================SHOW DATA FRAME====================================##
style=ttk.Style()
style.configure('Treeview.Heading',font=('times',15,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyan')
scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
teachertable=Treeview(ShowDataFrame,column=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=teachertable.xview)
scroll_y.config(command=teachertable.yview)
teachertable.heading('Id',text='Id')
teachertable.heading('Name',text='Name')
teachertable.heading('Mobile No',text='Mobile No')
teachertable.heading('Email',text='Email')
teachertable.heading('Address',text='Address')
teachertable.heading('Gender',text='Gender')
teachertable.heading('D.O.B',text='D.O.B')
teachertable.heading('Added Date',text='Added Date')
teachertable.heading('Added Time',text='Added Time')
teachertable['show']='headings'
teachertable.column('Id',width=100)
teachertable.column('Name',width=200)
teachertable.column('Mobile No',width=200)
teachertable.column('Email',width=300)
teachertable.column('Address',width=200)
teachertable.column('Gender',width=100)
teachertable.column('D.O.B',width=150)
teachertable.column('Added Date',width=150)
teachertable.column('Added Time',width=150)
teachertable.pack(fill=BOTH,expand=1)
###########################################SLIDER#########################################
ss='Welcome to the Teacher Profile'
count=0
text=''
###########################################
SliderLabel=Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
#################################################CLOCK#####################################
clock=Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()
#########################################################CONNNECT DATA BASE BUTTON####################
connectbutton=Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='light grey',activebackground='blue',activeforeground='white',command=Connectdb)

connectbutton.place(x=930,y=0)
root.mainloop()