import re
import tkinter as tk
from PIL import Image, ImageTk ,ImageDraw,ImageFont,ImageOps # Import Pillow for image processing
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename,askdirectory
import random
from io import BytesIO
import sqlite3
import os
import smtplib
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
import mygmail
from tkinter.ttk import Combobox, Treeview
from tkcalendar import Calendar
from tkinter import messagebox

from tkinter.scrolledtext import ScrolledText

# from pages import AddTeacherAccountPage,WelcomePage,TeacherLoginPage
# Initialize the main window
root = tk.Tk()
root.geometry("600x700")
root.title("STUDENT MANAGEMENT SYSTEM")

bg_color = '#273b7a'  # Background color for the frame
btn_color = '#1c2952'  # Button color
hover_color = '#3a4d8f'  # Button hover color
font_color = 'white'

# Load and resize icons
def load_icon(path, size):
    img = Image.open(path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)
# Icon paths and sizes
loginStudIcon = load_icon('images/student_login.png', (100, 100))
loginTeacherIcon = load_icon('images/teacher_login.png', (100, 100))
loginAdminIcon = load_icon('images/admin_login.png', (100, 100))
unlocked_icon =  tk.PhotoImage(file='images/unlocked.png')
locked_icon =  tk.PhotoImage(file='images/locked.png')
AddStudPicIcon = tk.PhotoImage(file='images/add_image.png')

# Function for hover effects
def on_enter(event):
    event.widget['bg'] = hover_color

def on_leave(event):
    event.widget['bg'] = btn_color

def messageBox(message):

     MessageBoxFm = tk.Frame(root, highlightbackground=bg_color,highlightthickness=3)

     closeBtn = tk.Button(MessageBoxFm,text='❌',bd=0, font=('Bold',13),fg=bg_color,command=lambda: MessageBoxFm.destroy())
     closeBtn.place(x=280,y=5)
     messageLb = tk.Label(MessageBoxFm,text=message,font=('Bold',15))
     messageLb.pack(pady=50)
     MessageBoxFm.place(x=100,y=120,width=320,height=200)

def initDatabase():
    if os.path.exists('StudentsAccounts.db'):
        connection = sqlite3.connect('StudentsAccounts.db')

        cursor = connection.cursor()

        cursor.execute("""SELECT * FROM Student_data
""")
        connection.commit()
        # print(cursor.fetchall())
        connection.close()
    else:
        connection = sqlite3.connect('StudentsAccounts.db')

        cursor = connection.cursor()

        cursor.execute("""
CREATE TABLE Student_data(
            id_number text,
            password text,
            name text,
            age text,
            gender text,
            phone_number text,
            class text,
            email text,
            image blod           

            )
""")
        cursor.execute("""
CREATE TABLE Teacher_data(
            id_number text,
            password text,
            name text,
            age text,
            gender text,
            phone_number text,
            subject text,
            email text,
            image blod           
            )
""")

        connection.commit()
        connection.close()

def checkStudentIdAlreadyExists(id_number):
    connection = sqlite3.connect('StudentsAccounts.db')

    cursor = connection.cursor()
    
    cursor.execute(f"""SELECT id_number FROM Student_data WHERE id_number == '{id_number}'
""")
    connection.commit()
    # print(cursor.fetchall())
    response = cursor.fetchall()
    connection.close()
    return response

def checkTeacherIdAlreadyExists(id_number):
    connection = sqlite3.connect('StudentsAccounts.db')

    cursor = connection.cursor()
    
    cursor.execute(f"""SELECT id_number FROM Teacher_data WHERE id_number == '{id_number}'
""")
    connection.commit()
    # print(cursor.fetchall())
    response = cursor.fetchall()
    connection.close()
    return response

# def checkValidPassword(id_number,password):
#     connection = sqlite3.connect('StudentsAccounts.db')

#     cursor = connection.cursor()
    
#     cursor.execute(f"""SELECT id_number,password FROM Student_data WHERE id_number == '{id_number}' AND password =='{password}'
# """)
#     connection.commit()
#     # print(cursor.fetchall())
#     response = cursor.fetchall()
#     connection.close()
#     return response

def checkValidPassword(user_type, id_number, password):
    # Ensure valid input for user type
    if user_type not in ["student", "teacher"]:
        raise ValueError("Invalid user type. Use 'student' or 'teacher'.")

    # Determine the appropriate table name
    table_name = "Student_data" if user_type == "student" else "Teacher_data"

    # Connect to the database
    connection = sqlite3.connect('StudentsAccounts.db')
    cursor = connection.cursor()

    # Use parameterized queries to prevent SQL injection
    query = f"SELECT id_number, password FROM {table_name} WHERE id_number = ? AND password = ?"
    cursor.execute(query, (id_number, password))

    response = cursor.fetchall()
    connection.close()
    return response



import sqlite3
def add_data(id_number,password,name,age,gender,phone_number,student_class,email,pic_data):
    connection = sqlite3.connect('StudentsAccounts.db')

    cursor = connection.cursor()

    cursor.execute(f"""
INSERT INTO Student_data VALUES('{id_number}','{password}','{name}','{age}','{gender}','{phone_number}','{student_class}','{email}', ?)

    """,[pic_data])
    connection.commit()
    connection.close()

def addTeacherdata(id_number,password,name,age,gender,phone_number,subject,email,pic_data):
    connection = sqlite3.connect('StudentsAccounts.db')

    cursor = connection.cursor()

    cursor.execute(f"""
INSERT INTO Teacher_data VALUES('{id_number}','{password}','{name}','{age}','{gender}','{phone_number}','{subject}','{email}', ?)

    """,[pic_data])
    connection.commit()
    connection.close()

def ConfirmationBox(message):
    answer = tk.BooleanVar()
    answer.set(False)

    def action(ans):
        answer.set(ans)
        ConfirmationBoxFm.destroy()

    ConfirmationBoxFm = tk.Frame(root, highlightbackground=bg_color,highlightthickness=3)
    messageLb= tk.Label(ConfirmationBoxFm,text=message,font=('Bold',15))
    messageLb.pack(pady=20)

    CancelBtn = tk.Button(ConfirmationBoxFm,text='Cancel', font=('Bold',15),bd=0,bg=bg_color,fg='white',command=lambda: ConfirmationBoxFm.destroy())
    CancelBtn.place(x=50,y=160)

    YesBtn = tk.Button(ConfirmationBoxFm,text='Yes', font=('Bold',15),bd=0,bg=bg_color,fg='white',command=lambda:action(True))
    YesBtn.place(x=190,y=160,width=80)

    ConfirmationBoxFm.place(x=100,y=120,width=320, height=220)
    # print("code rhai uper")
    root.wait_window(ConfirmationBoxFm)
    return answer.get()
    print("code rhai niche")

def drawStudentcard(studentPicPath,studentData):
    label ="""
id_number:
name:
age:
gender:
phone_number:
class:
email:
"""

    studentCard = Image.open('images/student_card_frame.png')
    pic = Image.open(studentPicPath).resize((100,100))

    studentCard.paste(pic,(15,25))
    draw = ImageDraw.Draw(studentCard)
    headingfont = ImageFont.truetype('arial',18)
    lablefont = ImageFont.truetype('arial',15)

    draw.text(xy=(150,60),text='student card',fill=(0,0,0),font=headingfont)
    draw.multiline_text(xy=(15,120),text=label,fill=(0,0,0),font=lablefont,spacing=6)

    draw.multiline_text(xy=(120,120),text=studentData,fill=(0,0,0),font=lablefont,spacing=6)

    # studentCard.show()
    return studentCard

def studentCardPage(student_card_obj):

    def saveStudentCard():
        path = askdirectory()
        if path :
            print(path)
            student_card_obj.save(f'{path}/studentCard.png')

    studentCardImg = ImageTk.PhotoImage(student_card_obj)

    def closePage():
         StudentCardPageFm.destroy()
         root.update()
         StudentLoginPage()


    StudentCardPageFm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3, relief='sunken', bd=3)

    heading_lb = tk.Label(StudentCardPageFm, text='Student Card', bg=bg_color, fg='white', font=('Bold', 18), bd=3, relief='sunken')
    heading_lb.place(x=0, y=0, width=400)

    closeBtn = tk.Button(StudentCardPageFm, text="❌", bg=bg_color, fg='white', font=('Bold', 13), bd=0, command=closePage)
    closeBtn.place(x=360, y=0)


    # Correct initialization of studentCardLb
    studentCardLb = tk.Label(StudentCardPageFm,image=studentCardImg)  # Highlighted
    studentCardLb.image = studentCardImg
    studentCardLb.place(x=50, y=50)  # Highlighted

    saveStudentCardBtn = tk.Button(StudentCardPageFm, text='Save student card', bg=bg_color, fg='white', font=('Bold', 15), bd=1, relief='sunken',command=saveStudentCard)
    saveStudentCardBtn.place(x=80, y=375)
    
    PrintStudentCardBtn = tk.Button(StudentCardPageFm, text='🖨️', bg=bg_color, fg='white', font=('Bold', 15), bd=1, relief='sunken')
    PrintStudentCardBtn.place(x=270, y=370)
    
    StudentCardPageFm.place(x=50, y=30, height=450, width=400)



#WElcome page    
def WelcomePage():

    def forwardToStudentLoginPage():
        welcomePageFm.destroy()
        root.update()
        StudentLoginPage()

    def forwardToTeacherLoginPage():
        welcomePageFm.destroy()
        root.update()
        TeacherLoginPage()

    def forwardToAdminLoginPage():
        welcomePageFm.destroy()
        root.update()
        AdminLoginPage()

    # Create the main frame
    welcomePageFm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

    # Heading label
    headingLabl = tk.Label(
        welcomePageFm,
        text="Welcome to Student Registration \n& Management System",
        bg=bg_color,
        fg=font_color,
        font=('Arial', 18, 'bold'),
        justify='center',
        bd=3,
        relief='ridge'
        
    )
    headingLabl.place(x=0, y=0, width=500, height=70)

    # Create a reusable function to place buttons
    def create_login_button(frame, text, icon, x, y,commands):
        # Image button
        img_btn = tk.Button(frame, image=icon, highlightthickness=0,bd=0,command=commands)
        img_btn.place(x=x, y=y, width=100, height=100)

        # Text button
        text_btn = tk.Button(
            frame,
            text=text,
            bg=btn_color,
            fg=font_color,
            font=('Arial', 15, 'bold'),
            bd=3,
            relief='ridge',
            command= commands,
            activebackground=hover_color,
            activeforeground='white'
        )
        text_btn.place(x=x + 130, y=y + 25, width=200, height=50)
        
        # Add hover effects
        text_btn.bind("<Enter>", on_enter)
        text_btn.bind("<Leave>", on_leave)

    # Add login buttons
    create_login_button(welcomePageFm, "Login Student", loginStudIcon, 60, 100,forwardToStudentLoginPage)
    create_login_button(welcomePageFm, "Login Teacher", loginTeacherIcon, 60, 250,forwardToTeacherLoginPage)
    create_login_button(welcomePageFm, "Admin Login", loginAdminIcon, 60, 400,forwardToAdminLoginPage)

    # Configure and pack the frame
    welcomePageFm.pack(pady=30)
    welcomePageFm.pack_propagate(False)
    welcomePageFm.configure(width=500, height=620)


# def sendMailToStudent(email,message, subject):
    import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMailToStudent(email, message, subject, username=mygmail.emailAddress, password=mygmail.password):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = email
        msg.attach(MIMEText(message, 'html'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as smtp_connection:
            smtp_connection.starttls()
            smtp_connection.login(username, password)
            smtp_connection.sendmail(username, email, msg.as_string())
        
        print('Mail sent successfully.')
    except Exception as e:
        print(f'Error sending mail: {e}')

#     smtp_server = 'smtp.gmail.co

def forgetPasswordPage():

    def recoverPassword():
        if checkStudentIdAlreadyExists(id_number=studenIdEnt.get()):
            print('correct id')
            connection = sqlite3.connect('StudentsAccounts.db')

            cursor = connection.cursor()

            cursor.execute(f""" SELECT password FROM Student_data WHERE id_number == '{studenIdEnt.get()}' """)


            connection.commit()
            recoverPassword = cursor.fetchall()[0][0]
            print('recovered pass ',recoverPassword)
            
            cursor.execute(f""" SELECT email FROM Student_data WHERE id_number == '{studenIdEnt.get()}' """)

            connection.commit()
            studeEmail = cursor.fetchall()[0][0]
            print('email address :', studeEmail)

            connection.close()
            confirmation =ConfirmationBox(message=f"we will send \n your password via \n your email address: {studeEmail} \n Do you want to continue ? ")
            if confirmation:
                msg = f"<h1> Your password is :</h1> <h2>{recoverPassword} </h2>"
                sendMailToStudent(email=studeEmail,message=msg,subject='Password Recovery')
        else:
            print('incorrect id')
            messageBox(message='!invalid Id number ')

    forgetPasswordPageFm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=4)

    headingLb = tk.Label(forgetPasswordPageFm,text='⚠️ Forgetting Password',font=('bold',15),bg=bg_color,fg='white')
    headingLb.place(x=0,y=0, width=350)
    closeBtn = tk.Button(forgetPasswordPageFm, text='❌',font=('Bold',15),bg=bg_color,bd=0,fg='white',command=lambda: forgetPasswordPageFm.destroy())
    closeBtn.place(x=300,y=0)

    studenIdLb = tk.Label(forgetPasswordPageFm,text='Enter student Id number ',font=('Bold',13))
    studenIdLb.place(x=70,y=40)
    studenIdEnt = tk.Entry(forgetPasswordPageFm,font=('Bold',15), justify=tk.CENTER)
    studenIdEnt.place(x=70,y=70,width=180)

    InfoLb = tk.Label(forgetPasswordPageFm,text='via your email address \n we will send your password\n to you',font=('Bold',13))
    InfoLb.place(x=70,y=110)
    nextBtn = tk.Button(forgetPasswordPageFm, text='next',font=('Bold',15),bg=bg_color,bd=0,fg='white',command=recoverPassword)
    nextBtn.place(x=130,y=200,width=80)

    forgetPasswordPageFm.place(x=75,y=120,width=350,height=250)

def FetchstudentData(query):
    connection = sqlite3.connect('StudentsAccounts.db')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    response = cursor.fetchall()
    connection.close()
    return response

def StudentDashBoard(Student_id):

    getStudentDetails = FetchstudentData(f"SELECT name, age , gender,class, phone_number,email FROM Student_data WHERE id_number == '{Student_id}' ")

    getStudentPic = FetchstudentData(f"SELECT image FROM Student_data WHERE id_number == '{Student_id}' ")

    studentPic = BytesIO(getStudentPic[0][0])
    # print(studentPic)
    
    def Logout():
        confirm = ConfirmationBox(message='do you want to \n Logout your Account ?')
        if confirm:
            StudDashboardFm.destroy()
            WelcomePage()
            root.update()

    def switch(indicator,page):
        homeBtnIndicator.config(bg='#B39DDB')
        StudentCardBtnIndicator.config(bg='#B39DDB')
        AttendanceBtnIndicator.config(bg='#B39DDB')
        homeBtnIndicator.config(bg='#B39DDB')
        VivaBtnIndicator.config(bg='#B39DDB')
        EditBtnIndicator.config(bg='#B39DDB')
        securityBtnIndicator.config(bg='#B39DDB')

        indicator.config(bg=bg_color)

        for child in PagesFm.winfo_children():
            child.destroy()
            root.update()
        page()

    StudDashboardFm =tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    
    OptionsFm = tk.Frame(StudDashboardFm ,highlightbackground=bg_color
    ,highlightthickness=2, bg='#B39DDB')

    homeBtn = tk.Button(OptionsFm,text='Home',font=('Bold',15),fg=bg_color, bg="#B39DDB", bd=0,justify=tk.LEFT, command= lambda: switch(indicator=homeBtnIndicator,page=HomePage))
    homeBtn.place(x=10,y=50)

    homeBtnIndicator = tk.Label(OptionsFm,bg=bg_color)
    homeBtnIndicator.place(x=5,y=48, width=3, height= 40)
    StudentCardBtn = tk.Button(OptionsFm,text='Student\nCard',font=('Bold',15),fg=bg_color, bg="#B39DDB", bd=0, justify=tk.LEFT,command= lambda: switch(indicator=StudentCardBtnIndicator, page=DashboardStudentCardPage))
    StudentCardBtn.place(x=10,y=100)
    StudentCardBtnIndicator = tk.Label(OptionsFm,bg="#B39DDB")
    StudentCardBtnIndicator.place(x=5,y=108, width=3, height= 40)

    AttendanceBtn = tk.Button(OptionsFm,text='Attendance',font=('Bold',15),fg=bg_color, bg="#B39DDB", bd=0, justify=tk.LEFT, command= lambda: switch(indicator=AttendanceBtnIndicator, page=AttendancePage))
    AttendanceBtn.place(x=10,y=170)
    AttendanceBtnIndicator = tk.Label(OptionsFm,bg="#B39DDB")
    AttendanceBtnIndicator.place(x=5,y=170, width=3, height= 40)

    VivaBtn = tk.Button(OptionsFm,text='Viva',font=('Bold',15),fg=bg_color, bg="#B39DDB", bd=0,  justify=tk.LEFT,command= lambda: switch(indicator=VivaBtnIndicator,page=VivaPage))
    VivaBtn.place(x=10,y=220)
    VivaBtnIndicator = tk.Label(OptionsFm,bg="#B39DDB")
    VivaBtnIndicator.place(x=5,y=220, width=3, height= 40)  
  
    EditBtn = tk.Button(OptionsFm,text='Edit data',font=('Bold',15),fg=bg_color, bg="#B39DDB", bd=0, justify=tk.LEFT,command= lambda: switch(indicator=EditBtnIndicator,page=EditPage))
    EditBtn.place(x=10,y=270)
    EditBtnIndicator = tk.Label(OptionsFm,bg="#B39DDB")
    EditBtnIndicator.place(x=5,y=270, width=3, height= 40)  
    
  
    securityBtn = tk.Button(OptionsFm,text='security',font=('Bold',15),fg=bg_color, bg="#B39DDB", bd=0, justify=tk.LEFT,command= lambda: switch(indicator=securityBtnIndicator,page=SecurityPage))
    securityBtn.place(x=10,y=320)
    securityBtnIndicator = tk.Label(OptionsFm,bg="#B39DDB")
    securityBtnIndicator.place(x=5,y=320, width=3, height= 40)  
    

    LogoutBtn = tk.Button(OptionsFm,text='Log out',font=('Bold',15),fg=bg_color, bg="#B39DDB", bd=0, justify=tk.LEFT,command= Logout)
    LogoutBtn.place(x=10,y=370)
    
    # homeBtn.place(x=10,y=50)

    OptionsFm.place(x=0,y=0,width=125 ,height=575)

    def HomePage():
        StudentPicImageObj = Image.open(studentPic)
        size = 100
        mask = Image.new(mode='L', size=(size,size))
        DrawCircle = ImageDraw.Draw(im=mask)
        DrawCircle.ellipse(xy=(0,0,size,size), fill=255,outline=True)
        output = ImageOps.fit(image=StudentPicImageObj,size=mask.size,centering=(1,1))
        output.putalpha(mask)

        studentPicture = ImageTk.PhotoImage(output)

        homePageFm = tk.Frame(PagesFm)

        studentPicLb = tk.Label(homePageFm,image=studentPicture)
        studentPicLb.image = studentPicture
        studentPicLb.place(x=10,y=10)

        hiLb = tk.Label(homePageFm, text= f"hi { getStudentDetails[0][0]}",font=('Bold',15))
        hiLb.place(x=130,y=50)
        studentDetails = f"""
Student Id : {Student_id}\n
Name: {getStudentDetails[0][0]}\n
Age: {getStudentDetails[0][1]}\n
Gender : {getStudentDetails[0][2]}\n
Class: {getStudentDetails[0][3]}\n 
contact : {getStudentDetails[0][4]}\n 
Email: {getStudentDetails[0][5]}\n  """
        StudentDetalisLb = tk.Label(homePageFm,text= studentDetails, font=('Bold',13), justify=tk.LEFT)

        StudentDetalisLb.place(x=20,y=130)

        homePageFm.pack(fill=tk.BOTH, expand=True)

    def DashboardStudentCardPage():
        studentDetails = f"""
{Student_id}
{getStudentDetails[0][0]}
{getStudentDetails[0][1]}
{getStudentDetails[0][2]}
{getStudentDetails[0][4]}
{getStudentDetails[0][3]}
{getStudentDetails[0][5]}"""
        
        studentCardImageObj = drawStudentcard(studentPicPath=studentPic,studentData=studentDetails)

        def saveStudentCard():
            path = askdirectory()
            if path :
                # print(path)
                studentCardImageObj.save(f'{path}/studentCard.png')

        studentCardImg = ImageTk.PhotoImage(studentCardImageObj)
        # studentCardImageObj.show()
        studentcardImage = ImageTk.PhotoImage(studentCardImageObj)
        StudentCardPageFm = tk.Frame(PagesFm)
        cardLb = tk.Label(StudentCardPageFm,image=studentcardImage)
        cardLb.image = studentcardImage
        cardLb.place(x=20,y=50)
        saveStudenCardBtn = tk.Button(StudentCardPageFm,text='Save student card', font=('Bold',15), bd=1, fg='white', bg=bg_color,command=saveStudentCard)
        saveStudenCardBtn.place(x=40, y= 400)


        StudentCardPageFm.pack(fill=tk.BOTH, expand=True)   

    def SecurityPage():
        def showHindePassword():
                if currentPasswordEnt['show']=='*':
                    currentPasswordEnt.config(show='')
                    showHindeBtn.config(image=unlocked_icon)
                else:
                    currentPasswordEnt.config(show='*')
                    showHindeBtn.config(image=locked_icon)
        def setPassword():
            if newPasswordEnt.get() != '':
                confirm = ConfirmationBox(message='Do you want to \n change your password ?')
                if confirm:
                    connection = sqlite3.connect('StudentsAccounts.db')

                    cursor = connection.cursor()

                    cursor.execute(f"""UPDATE Student_data SET password ='{newPasswordEnt.get()}'WHERE id_number == '{Student_id}' """)

                    connection.commit()
                    connection.close()
                    messageBox(message="Password change successfully")

                    currentPasswordEnt.config(state=tk.NORMAL)
                    currentPasswordEnt.delete(0,tk.END)
                    currentPasswordEnt.insert(0,newPasswordEnt.get())
                    currentPasswordEnt.config(state='readonly')
                    newPasswordEnt.delete(0,tk.END)

            else:
                messageBox(message="Enter New Password ")            

        securityPageFm = tk.Frame(PagesFm)

        currentPasswordLb = tk.Label(securityPageFm,text= 'Your current password is ',font=('Bold',12))
        currentPasswordLb.place(x=80,y=30)

        currentPasswordEnt = tk.Entry(securityPageFm, font=("Bold",15),justify=tk.CENTER, show='*')
        currentPasswordEnt.place(x=50,y=80)

        studentCurrentPassword = FetchstudentData(f"SELECT password FROM Student_data WHERE id_number == {Student_id}")
        # print(studentCurrentPassword)
        currentPasswordEnt.insert(tk.END,studentCurrentPassword[0][0])
        currentPasswordEnt.config(state='readonly')

        showHindeBtn = tk.Button(securityPageFm,image=locked_icon,bd=0,command=showHindePassword)
        showHindeBtn.place(x=280,y=70)

        changePasswordLb = tk.Label(securityPageFm,text='Change pasword',font=('Bold',15), bg='red', fg='white')

        changePasswordLb.place(x=30,y=210,width=290)

        newPasswordlb = tk.Label(securityPageFm, text='Set new password',font=('Bold',12))
        newPasswordlb.place(x=100,y=280)

        newPasswordEnt = tk.Entry(securityPageFm, font=('bold',15), justify=tk.CENTER)
        newPasswordEnt.place(x=60,y=330)

        changePasswordBtn = tk.Button(securityPageFm, text="Set password",font=('Bold',12), bg=bg_color, fg='white',command=setPassword)
        changePasswordBtn.place(x=110,y=380)


        securityPageFm.pack(fill=tk.BOTH, expand=True)

    def VivaPage():
        import pyttsx3
        import tkinter as tk
        from tkinter import scrolledtext, messagebox, ttk
        import sqlite3

        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)

        # Global student_id
        # student_id = 101  # Replace this with your global variable logic

        # Initialize database connection
        conn = sqlite3.connect("StudentsAccounts.db")
        cursor = conn.cursor()

        # Create table for storing results
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS viva_results (
            student_id INTEGER,
            subject_name TEXT,
            total_marks INTEGER,
            obtained_marks INTEGER
        )
        """)
        conn.commit()

        def speak(text):
            try:
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print(f"Error in TTS: {e}")

        # Questions and answers
        questions = {
            "python": {
                "What is the keyword to define a function?": ["def", "func", "define", "lambda"],
                "What is the output of print(2 + 2)?": ["4", "22", "8", "None"],
                "What is the type of [1, 2, 3]?": ["list", "tuple", "set", "dictionary"],
                "What is the keyword to define a class?": ["class", "def", "object", "init"],
                "What method is used to add an item to a list?": ["append", "insert", "push", "add"]
            },
            "c": {
                "What is the format specifier for an integer?": ["%d", "%f", "%c", "%s"],
                "What is the keyword to include header files?": ["include", "import", "header", "load"],
                "What is the result of 5 modulo 2?": ["1", "2", "0", "5"],
                "What is the return type of the main function?": ["int", "void", "char", "float"],
                "Which operator is used to access a pointer's value?": ["*", "&", "%", "@"]
            },
            "dsa": {
                "What data structure uses FIFO?": ["Queue", "Stack", "Heap", "Tree"],
                "What data structure uses LIFO?": ["Stack", "Queue", "Graph", "List"],
                "What is the time complexity of binary search?": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
                "What is a dynamic programming technique?": ["Memoization", "Sorting", "Searching", "Hashing"],
                "What data structure is used for depth-first search?": ["Stack", "Queue", "Graph", "Array"]
            }
        }

        SubjectList = ["PYTHON", "C", "DSA"]
        VivaPageFm = tk.Frame(PagesFm)

        def start_voice_viva():
            subject = SelectClassBtn.get().lower()
            if subject not in questions:
                messagebox.showerror("Invalid Subject", "Please choose a valid subject.")
                return

            # Clear the VivaPage frame
            for widget in VivaPageFm.winfo_children():
                widget.destroy()

            question_list = list(questions[subject].items())
            question_index = [0]
            total_marks = len(question_list)
            obtained_marks = [0]

            def ask_question():
                if question_index[0] < total_marks:
                    question, options = question_list[question_index[0]]
                    speak(question)
                    question_label.config(text=question)
                    for i, option in enumerate(options):
                        answer_checkboxes[i].config(text=option, state=tk.NORMAL)
                    for i in range(len(options), 4):
                        answer_checkboxes[i].config(text="", state=tk.DISABLED)
                else:
                    speak("The viva is over. Thank you!")
                    done = messagebox.showinfo("Viva Complete", "You have completed the viva!")
                    if done:
                        # Save results to database
                        cursor.execute("""
                        INSERT INTO viva_results (student_id, subject_name, total_marks, obtained_marks)
                        VALUES (?, ?, ?, ?)
                        """, (Student_id, subject, total_marks, obtained_marks[0]))
                        conn.commit()

                        VivaPageFm.destroy()
                        VivaPage()
                        root.update()

            def process_answer():
                if question_index[0] >= total_marks:
                    return

                correct_answer = question_list[question_index[0]][1][0]

                # Get the selected answer
                selected_answer = None
                for i, var in enumerate(answer_vars):
                    if var.get() == "1":
                        selected_answer = answer_checkboxes[i].cget("text")
                        break

                # Update obtained marks
                if selected_answer == correct_answer:
                    obtained_marks[0] += 1
                    log.insert(tk.END, "Correct!\n")
                else:
                        log.insert(tk.END, f"Wrong. Correct Answer: {correct_answer}\n")


                # Reset checkboxes
                for var in answer_vars:
                    var.set("0")

                question_index[0] += 1
                ask_question()

            # Viva UI
            question_label = tk.Label(VivaPageFm, text="Question will appear here.", wraplength=400, font=("Arial", 14))
            question_label.pack(pady=10)

            answer_vars = [tk.StringVar(value="0") for _ in range(4)]
            answer_checkboxes = []

            answer_frame = tk.Frame(VivaPageFm)
            answer_frame.pack(pady=10)

            for i in range(4):
                cb = tk.Checkbutton(answer_frame, text="", variable=answer_vars[i], font=("Arial", 12), anchor='w', onvalue="1", offvalue="0")
                cb.pack(fill='x', padx=10, pady=2)
                answer_checkboxes.append(cb)

            next_button = tk.Button(
                VivaPageFm,
                text="Next",
                command=process_answer,
                font=("Arial", 12),
            )
            next_button.pack(pady=10)

            log = scrolledtext.ScrolledText(VivaPageFm, wrap=tk.WORD, font=("Arial", 10), width=50, height=10)
            log.pack(pady=10)
            

            ask_question()

        # Main Viva UI
        VivaPageLb = tk.Label(VivaPageFm, text="Student Viva", font=('Bold', 15))
        VivaPageLb.place(x=10, y=20)

        selectSbuLb = tk.Label(VivaPageFm, text='Select Student Subject', font=('Bold', 12))
        selectSbuLb.place(x=50, y=45)

        SelectClassBtn = ttk.Combobox(VivaPageFm, font=('Bold', 15), state='readonly', values=SubjectList)
        SelectClassBtn.place(x=10, y=75, width=180, height=30)

        start_button = tk.Button(VivaPageFm, text="Start Viva", command=start_voice_viva, font=("Arial", 12))
        start_button.place(x=50, y=120)

        VivaPageFm.pack(fill=tk.BOTH, expand=True)


    def EditPage():
        EditPageFm = tk.Frame(PagesFm)
        picPath = tk.StringVar()
        picPath.set('')
        def openPic():
            path = askopenfilename()
            if path:
                img = ImageTk.PhotoImage(Image.open(path).resize((100,100)))
                picPath.set(path)

                AddPicBtn.config(image=img)
                AddPicBtn.image = img
                
        def CheckInvalidEmail(email):
          
            pattern = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"
 
            match = re.match(pattern=pattern, string=email)

            return match            
        def removeHightlightWaring(entry):
            if entry['highlightbackground'] != 'gray':
                if entry.get() !='':
                    entry.config(highlightcolor=bg_color,highlightbackground='gray',) 

        def checkInputs():
            nonlocal getStudentDetails, getStudentPic, studentPic
            if StudNameEnt.get()=='':
              StudNameEnt.config(highlightcolor='red', highlightbackground='red')
              StudNameEnt.focus()
              messageBox(message='student full Name is required')  
             
            elif StudAgeEnt.get()=='':   
                StudAgeEnt.config(highlightcolor='red', highlightbackground='red')
                StudAgeEnt.focus()
                messageBox(message='student age is required') 

            elif StudContEnt.get()=='':   
                StudContEnt.config(highlightcolor='red', highlightbackground='red')
                StudContEnt.focus()
                messageBox(message='student contact number is required') 

            elif StudEmailEnt.get()=='':   
                StudEmailEnt.config(highlightcolor='red', highlightbackground='red')
                StudEmailEnt.focus()
                messageBox(message='student Email is required') 

            elif not CheckInvalidEmail(email=StudEmailEnt.get().lower()):
                StudEmailEnt.config(highlightcolor='red', highlightbackground='red')
                StudEmailEnt.focus()
                messageBox(message='Please enter a valid\nEmail address') 
            else:
                if picPath.get()!= '':
                    newStudentPicture = Image.open(picPath.get()).resize((100,100))
                    newStudentPicture.save('tempPic.png')

                    with open('tempPic.png', 'rb') as readNewPic:
                        newPictureBinary = readNewPic.read()
                        readNewPic.close()

                    connection = sqlite3.connect('StudentsAccounts.db') 
                    cursor = connection.cursor()

                    cursor.execute(f"UPDATE Student_data SET image =? WHERE id_number == '{Student_id}'",[newPictureBinary]) 

                    connection.commit()
                    connection.close()

                    messageBox(message='Data Updated successfully ') 
                name = StudNameEnt.get()    
                age = StudAgeEnt.get()   
                contact_number = StudContEnt.get()   
                email_address = StudEmailEnt.get()   
                connection = sqlite3.connect('StudentsAccounts.db') 
                cursor = connection.cursor()

                cursor.execute(f"UPDATE Student_data SET name ='{name}', age = '{age}', phone_number= '{contact_number}', email = '{email_address}' WHERE id_number == '{Student_id}'") 
                connection.commit()
                connection.close()
                messageBox(message='Data Updated successfully') 
                getStudentDetails = FetchstudentData(f"SELECT name, age , gender,class, phone_number,email FROM Student_data WHERE id_number == '{Student_id}' ")

                getStudentPic = FetchstudentData(f"SELECT image FROM Student_data WHERE id_number == '{Student_id}' ")

                studentPic = BytesIO(getStudentPic[0][0]) 
                   

        StudentCurrentPic = ImageTk.PhotoImage(Image.open(studentPic))              

        AddPicSecFm = tk.Frame(EditPageFm,highlightbackground=bg_color,highlightthickness=2)
 
        AddPicBtn = tk.Button(AddPicSecFm,image=StudentCurrentPic,bd=0,command=openPic)
        AddPicBtn.image =StudentCurrentPic
        AddPicBtn.pack()
        AddPicSecFm.place(x=5,y=5,width=105,height=105)

        StudNameLb = tk.Label(EditPageFm,text='Enter Student name.',font=('Bold',12))

        StudNameLb.place(x=5,y=130)


        StudNameEnt = tk.Entry(EditPageFm,font=('Bold',15),highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
        StudNameEnt.place(x=5,y=160,width=180)
        StudNameEnt.bind('<KeyRelease>',
        lambda e: removeHightlightWaring(entry=StudNameEnt))

        StudNameEnt.insert(tk.END, getStudentDetails[0][0])
        StudAgeLb= tk.Label(EditPageFm,text='Enter Student Age.', font=('Bold',12))
        StudAgeLb.place(x=5,y=210)

        StudAgeEnt = tk.Entry(EditPageFm, font=('Bold',15), highlightbackground='gray',highlightcolor=bg_color,highlightthickness=2)
        StudAgeEnt.place(x=5,y=235, width=180)
        StudAgeEnt.bind('<KeyRelease>',
        lambda e: removeHightlightWaring(entry=StudAgeEnt))
        StudAgeEnt.insert(tk.END, getStudentDetails[0][1])
        StudContLb= tk.Label(EditPageFm,text='Enter new Contact number ', font=('Bold',12))
        StudContLb.place(x=5,y=285)

        StudContEnt = tk.Entry(EditPageFm, font=('Bold',15), highlightbackground='gray',highlightcolor=bg_color,highlightthickness=2)
        StudContEnt.place(x=5,y=310, width=180)
        StudContEnt.bind('<KeyRelease>',
        lambda e: removeHightlightWaring(entry=StudContEnt))   
        StudContEnt.insert(tk.END, getStudentDetails[0][4])
        StudEmailLb= tk.Label(EditPageFm,text='Enter new email address ', font=('Bold',12))
        StudEmailLb.place(x=5,y=360)

        StudEmailEnt = tk.Entry(EditPageFm, font=('Bold',15), highlightbackground='gray',highlightcolor=bg_color,highlightthickness=2)
        StudEmailEnt.place(x=5,y=385, width=180)
        StudEmailEnt.bind('<KeyRelease>',
        lambda e: removeHightlightWaring(entry=StudEmailEnt))
        StudEmailEnt.insert(tk.END, getStudentDetails[0][-1])
        UpdateDataBtn = tk.Button(EditPageFm, text="Update", font=('Bold',15),fg='white', bg=bg_color, bd=0, command=checkInputs)

        UpdateDataBtn.place(x=220, y=470, width=80)

      

        EditPageFm.pack(fill=tk.BOTH, expand=True)    

    def deleteAccountPage():

        def confirmDeleteAccount():
            confirm = ConfirmationBox(message='⚠️ DO you want to delete \n this account ?')

            if confirm:
                connection = sqlite3.connect('StudentsAccounts.db')
                cursor = connection.cursor()

                cursor.execute(f"""DELETE FROM Student_data WHERE id_number == {Student_id} """)
                connection.commit()
                connection.close()
                
                StudDashboardFm.destroy()
                WelcomePage()
                root.update()
                messageBox(message='Account successfully deleted')

        deleteAccountPageFm = tk.Frame(PagesFm)
        deleteAccountLb = tk.Label(deleteAccountPageFm, text='⚠️Delete account', bg='red', fg= 'white', font=('Bold',15))
        deleteAccountLb.place(x=30, y=100, width=290)
        deleteAccountBtn= tk.Button(deleteAccountPageFm, text='Delete Account', bg='red',fg='white', font=('Bold', 13),command=confirmDeleteAccount)

        deleteAccountBtn.place(x=110,y=200)
        deleteAccountPageFm.pack(fill=tk.BOTH, expand=True)

    

    def AttendancePage():
        AttendancePageFm = tk.Frame(PagesFm)

        AttendancePageLb = tk.Label(AttendancePageFm,text="Attendance ", font=('Bold',15))
        AttendancePageLb.place(x=100,y=200)

        AttendancePageFm.pack(fill=tk.BOTH, expand=True)    

    PagesFm = tk.Frame(StudDashboardFm,bg='red')
    PagesFm.place(x=122,y=5,width=345,height=550)
    HomePage()

    StudDashboardFm.pack(pady=5)
    StudDashboardFm.pack_propagate(False)
    StudDashboardFm.configure(width=480,height=580)

#Student log in page hai 
def StudentLoginPage():
    def forwardToWelcomePage():
        StudentLoginPageFm.destroy()
        root.update()
        WelcomePage()

    def showHindePassword():
        if passwordEnt['show']=='*':
            passwordEnt.config(show='')
            showHindeBtn.config(image=unlocked_icon)
        else:
            passwordEnt.config(show='*')
            showHindeBtn.config(image=locked_icon)
   
    def removeHightlightWaring(entry):
        if entry['highlightbackground'] != 'gray':
            if entry.get() !='':
                entry.config(highlightcolor=bg_color,highlightbackground='gray',)

    def login_account():
        verifyIdNumber = checkStudentIdAlreadyExists(id_number=idNumberEnt.get())

        if verifyIdNumber:
            print('Id is correct')
            verifyPassword = checkValidPassword(user_type="student",id_number=idNumberEnt.get(),password=passwordEnt.get())

            if verifyPassword:
                # print('password is correct')
                id_number=idNumberEnt.get()
                StudentLoginPageFm.destroy()
                StudentDashBoard(Student_id=id_number)
                root.update()
            else:
                print('Oop password is incorrect') 
                passwordEnt.config(highlightcolor='red',highlightbackground='red')

                messageBox(message='invalid passwoed')

        else:
            idNumberEnt.config(highlightcolor='red',highlightbackground='red')
            messageBox(message='Please enter valid stuent id')


    StudentLoginPageFm = tk.Frame(root,highlightbackground=bg_color,highlightthickness=4)


    HeadinLb = tk.Label(StudentLoginPageFm,text='Student login Page', bg=bg_color,fg='white', font=('bold',18))

    HeadinLb.place(x=0,y=0,width=400)

    BackBtn = tk.Button(StudentLoginPageFm,text="❌", font=('bold',20),fg=bg_color,bd=0,command=forwardToWelcomePage)
    BackBtn.place(x=5,y=40)

    StudIcoLb = tk.Label(StudentLoginPageFm,image=loginStudIcon)
    StudIcoLb.place(x=150,y=40)

    IdNumberLb = tk.Label(StudentLoginPageFm,text='Enter Student ID number.',font=('Bold',15),fg=bg_color)
    IdNumberLb.place(x=80,y=140)

    idNumberEnt = tk.Entry(StudentLoginPageFm,font=('Bold',15), justify=tk.CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=4)
    idNumberEnt.place(x=80, y=190)
    idNumberEnt.bind('<KeyRelease>', lambda e: removeHightlightWaring(entry=idNumberEnt))

    passwordLb = tk.Label(StudentLoginPageFm,text='Enter Student Password.',font=('Bold',15),fg=bg_color)
    passwordLb.place(x=80,y=240)

    passwordEnt = tk.Entry(StudentLoginPageFm,font=('Bold',15), justify=tk.CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=4,show='*')
    passwordEnt.place(x=80, y=290)
    passwordEnt.bind('<KeyRelease>',lambda e: removeHightlightWaring(entry=passwordEnt))

    showHindeBtn = tk.Button(StudentLoginPageFm,image=locked_icon,bd=0,command=showHindePassword)
    showHindeBtn.place(x=310,y=280)

    loginBtn = tk.Button(StudentLoginPageFm,text='Login',font=('Bold', 15), bg=bg_color, fg='white',command=login_account)
    loginBtn.place(x = 95, y=340, width=200, height=40)

    forgetPasswordBtn = tk.Button(StudentLoginPageFm, text='⚠️ \n forget Password', fg=bg_color,bd=0,command=forgetPasswordPage)
    forgetPasswordBtn.place(x=150, y=390)

    StudentLoginPageFm.pack(pady=30)
    StudentLoginPageFm.pack_propagate(False)
    StudentLoginPageFm.configure(width=400, height=460)

#admin  login page
def AdminLoginPage():

    def forwardToWelcomePage():
        AdminLoginPageFm.destroy()
        root.update()
        WelcomePage()

    def showHindePassword():
        if passwordEnt['show']=='*':
            passwordEnt.config(show='')
            showHindeBtn.config(image=unlocked_icon)
        else:
            passwordEnt.config(show='*')
            showHindeBtn.config(image=locked_icon)
     
    AdminLoginPageFm = tk.Frame(root,highlightbackground=bg_color,highlightthickness=4)


    HeadinLb = tk.Label(AdminLoginPageFm,text='Admin login Page', bg=bg_color,fg='white', font=('bold',18))

    HeadinLb.place(x=0,y=0,width=400)

    BackBtn = tk.Button(AdminLoginPageFm,text="❌", font=('bold',20),fg=bg_color,bd=0,command=forwardToWelcomePage)
    BackBtn.place(x=5,y=40)

    AdminIcoLb = tk.Label(AdminLoginPageFm,image=loginAdminIcon)
    AdminIcoLb.place(x=150,y=40)

    usersLb = tk.Label(AdminLoginPageFm,text='Enter Admin User Name',font=('Bold',15),fg=bg_color)
    usersLb.place(x=80,y=140)

    adminEnt = tk.Entry(AdminLoginPageFm,font=('Bold',15), justify=tk.CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=4)
    adminEnt.place(x=80, y=190)

    passwordLb = tk.Label(AdminLoginPageFm,text='Enter Admin Password.',font=('Bold',15),fg=bg_color)
    passwordLb.place(x=80,y=240)

    passwordEnt = tk.Entry(AdminLoginPageFm,font=('Bold',15), justify=tk.CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=4,show='*')
    passwordEnt.place(x=80, y=290)

    showHindeBtn = tk.Button(AdminLoginPageFm,image=locked_icon,bd=0,command=showHindePassword)
    showHindeBtn.place(x=310,y=280)

    loginBtn = tk.Button(AdminLoginPageFm,text='Login',font=('Bold', 15), bg=bg_color, fg='white')
    loginBtn.place(x = 95, y=340, width=200, height=40)

    forgetPasswordBtn = tk.Button(AdminLoginPageFm, text='⚠️ \n forget Password', fg=bg_color,bd=0)
    forgetPasswordBtn.place(x=150, y=390)

    AdminLoginPageFm.pack(pady=30)
    AdminLoginPageFm.pack_propagate(False)
    AdminLoginPageFm.configure(width=400, height=460)

def TeacherLoginPage():
    def forwardToWelcomePage():
        TeacherLoginPageFm.destroy()
        root.update()
        WelcomePage()
    def showHindePassword():
        if passwordEnt['show']=='*':
            passwordEnt.config(show='')
            showHindeBtn.config(image=unlocked_icon)
        else:
            passwordEnt.config(show='*')
            showHindeBtn.config(image=locked_icon)

    def login_account():
        verifyIdNumber = checkTeacherIdAlreadyExists(id_number= TeacherEnt.get())

        if verifyIdNumber:
            print('Id is correct')
            verifyPassword = checkValidPassword(user_type="teacher",id_number= TeacherEnt.get(),password=passwordEnt.get())

            if verifyPassword:
                # print('password is correct')
                id_number= TeacherEnt.get()
                TeacherLoginPageFm.destroy()
                # TeacherDashBoard()
                root.update()
                TeacherDashboard(id_number)
            else:
                print('Oop password is incorrect') 
                passwordEnt.config(highlightcolor='red',highlightbackground='red')

                messageBox(message='invalid passwoed')

        else:
             TeacherEnt.config(highlightcolor='red',highlightbackground='red')
             messageBox(message='Please enter valid stuent id')
        

     
    TeacherLoginPageFm = tk.Frame(root,highlightbackground=bg_color,highlightthickness=4)


    HeadinLb = tk.Label(TeacherLoginPageFm,text='Teachers login Page', bg=bg_color,fg='white', font=('bold',18))

    HeadinLb.place(x=0,y=0,width=400)

    BackBtn = tk.Button(TeacherLoginPageFm,text="❌", font=('bold',20),fg=bg_color,bd=0,command=forwardToWelcomePage)
    BackBtn.place(x=5,y=40)

    AdminIcoLb = tk.Label(TeacherLoginPageFm,image=loginTeacherIcon)
    AdminIcoLb.place(x=150,y=40)

    TeacherusersLb = tk.Label(TeacherLoginPageFm,text='Enter Teacher User Name',font=('Bold',15),fg=bg_color)
    TeacherusersLb.place(x=80,y=140)

    TeacherEnt = tk.Entry(TeacherLoginPageFm,font=('Bold',15), justify=tk.CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=4)
    TeacherEnt.place(x=80, y=190)

    passwordLb = tk.Label(TeacherLoginPageFm,text='Enter teacher Password.',font=('Bold',15),fg=bg_color)
    passwordLb.place(x=80,y=240)

    passwordEnt = tk.Entry(TeacherLoginPageFm,font=('Bold',15), justify=tk.CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=4,show='*')
    passwordEnt.place(x=80, y=290)

    showHindeBtn = tk.Button(TeacherLoginPageFm,image=locked_icon,bd=0,command=showHindePassword)
    showHindeBtn.place(x=310,y=280)

    loginBtn = tk.Button(TeacherLoginPageFm,text='Login',font=('Bold', 15), bg=bg_color, fg='white',command=login_account)
    loginBtn.place(x = 95, y=340, width=200, height=40)

    forgetPasswordBtn = tk.Button(TeacherLoginPageFm, text='⚠️ \n forget Password', fg=bg_color,bd=0)
    forgetPasswordBtn.place(x=150, y=390)

    TeacherLoginPageFm.pack(pady=30)
    TeacherLoginPageFm.pack_propagate(False)
    TeacherLoginPageFm.configure(width=400, height=460)


classList = ['BCA-FY','BCA-SY','BCA-TY','IMCA-FY','IMCA-SY','IMCA-TY','MCA-FY','MCA-SY',]
def AddStudentAccountPage():

    picPath = tk.StringVar()
    picPath.set('')
    def openPic():
        path = askopenfilename()
        if path:
            print(path)
            img = ImageTk.PhotoImage(Image.open(path).resize((100,100)))
            picPath.set(path)

            AddPicBtn.config(image=img)
            AddPicBtn.image = img
    def forwardToWelcomePage():
        picPath = tk.StringVar()
        picPath.set('')


        ans = ConfirmationBox(message='Do you want to leave\n registration form ?')
        if ans:
            AddAccountPagefm.destroy()
            root.update()
            WelcomePage()
    def removeHightlightWaring(entry):
        if entry['highlightbackground'] != 'gray':
            if entry.get() !='':
                entry.config(highlightcolor=bg_color,highlightbackground='gray',)

    def CheckInvalidEmail(email):
        pattern = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"
 
        match = re.match(pattern=pattern, string=email)

        return match     

    def GenerateIdNumber():
        GeneratedId =''

        for r in range(6):
            GeneratedId += str(random.randint(0,9))

        # print(checkIdAlreadyExists(id_number=GeneratedId))    
        if not checkStudentIdAlreadyExists(id_number=GeneratedId):

            print('id number:',GeneratedId) 

            StudenId.config(state=tk.NORMAL)
            StudenId.delete(0,tk.END)
            StudenId.insert(tk.END,GeneratedId)
            StudenId.config(state='readonly')
        else:
            GenerateIdNumber()


    def checkInputVlidation():
        if StudNameEnt.get()=='':
            StudNameEnt.config(highlightcolor='red', highlightbackground='red')
            StudNameEnt.focus()
            messageBox(message='student full Name is required')  
             
        elif StudAgeEnt.get()=='':   
            StudAgeEnt.config(highlightcolor='red', highlightbackground='red')
            StudAgeEnt.focus()
            messageBox(message='student age is required') 

        elif StudContEnt.get()=='':   
            StudContEnt.config(highlightcolor='red', highlightbackground='red')
            StudContEnt.focus()
            messageBox(message='student contact number is required') 

        elif StudEmailEnt.get()=='':   
            StudEmailEnt.config(highlightcolor='red', highlightbackground='red')
            StudEmailEnt.focus()
            messageBox(message='student Email is required') 

        elif not CheckInvalidEmail(email=StudEmailEnt.get().lower()):
            StudEmailEnt.config(highlightcolor='red', highlightbackground='red')
            StudEmailEnt.focus()
            messageBox(message='Please enter a valid\nEmail address') 


        elif SelectClassBtn.get()=='':   
            SelectClassBtn.config(highlightcolor='red', highlightbackground='red')
            SelectClassBtn.focus()
            messageBox(message='student class is required') 

        elif AccountPasswordEnt.get()=='':   
            AccountPasswordEnt.config(highlightcolor='red', highlightbackground='red')
            AccountPasswordEnt.focus()
            messageBox(message='student password is required') 
        else:

            pic_data = b''

            if picPath.get() != '':

                resize_pic = Image.open(picPath.get()).resize((100,100))
                resize_pic.save('temp_pic.png')

                read_data = open('temp_pic.png','rb')
                pic_data= read_data.read()
                read_data.close()
            else:
                read_data = open('images/add_image.png','rb')
                pic_data= read_data.read()
                read_data.close()  
                picPath.set('images/add_image.png')

            add_data(id_number=StudenId.get(),password=AccountPasswordEnt.get(),name=StudNameEnt.get(),
            age=StudAgeEnt.get(),
            gender=StudGender.get(),
            phone_number=StudContEnt.get(),
            student_class=SelectClassBtn.get(),
            email=StudEmailEnt.get(),
            pic_data=pic_data
            )   
            data = f"""
{StudenId.get()}
{StudNameEnt.get()}
{StudAgeEnt.get()}
{StudGender.get()}
{StudContEnt.get()}
{SelectClassBtn.get()}
{StudEmailEnt.get()}
""" 
            messageBox('Account successfully Created')
            getStudentCard = drawStudentcard(studentPicPath=picPath.get(),studentData=data)
            studentCardPage(getStudentCard)
            AddAccountPagefm.destroy()
            root.update()


    StudGender = tk.StringVar()
    AddAccountPagefm = tk.Frame(root,highlightbackground=bg_color,highlightthickness=4)

    AddPicSecFm = tk.Frame(AddAccountPagefm,highlightbackground=bg_color,highlightthickness=2)
 
    AddPicBtn = tk.Button(AddPicSecFm,image=AddStudPicIcon,bd=0,command=openPic)
    AddPicBtn.pack()
    AddPicSecFm.place(x=5,y=5,width=105,height=105)
   
    StudNameLb = tk.Label(AddAccountPagefm,text='Enter Student name.',font=('Bold',12))

    StudNameLb.place(x=5,y=130)

    StudNameEnt = tk.Entry(AddAccountPagefm,font=('Bold',15),highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
    StudNameEnt.place(x=5,y=160,width=180)
    StudNameEnt.bind('<KeyRelease>',
    lambda e: removeHightlightWaring(entry=StudNameEnt))

    StudGenderLb = tk.Label(AddAccountPagefm,text='Select Student  Gender.',font=('Bold',12))
    StudGenderLb.place(x=5,y=210)
    MaleGenderBtn= tk.Radiobutton(AddAccountPagefm,text='Male',font=('bold',12), variable=StudGender, value='male')
    MaleGenderBtn.place(x=5,y=235)
    FemaleGenderBtn= tk.Radiobutton(AddAccountPagefm,text='Female',font=('bold',12),variable=StudGender, value='female')
    FemaleGenderBtn.place(x=75,y=235)
    StudGender.set('male')

    StudAgeLb= tk.Label(AddAccountPagefm,text='Enter Student Age.', font=('Bold',12))
    StudAgeLb.place(x=5,y=275)

    StudAgeEnt = tk.Entry(AddAccountPagefm, font=('Bold',15), highlightbackground='gray',highlightcolor=bg_color,highlightthickness=2)
    StudAgeEnt.place(x=5,y=305, width=180)
    StudAgeEnt.bind('<KeyRelease>',
    lambda e: removeHightlightWaring(entry=StudAgeEnt))

    StudContLb= tk.Label(AddAccountPagefm,text='Enter Contact number ', font=('Bold',12))
    StudContLb.place(x=5,y=360)

    StudContEnt = tk.Entry(AddAccountPagefm, font=('Bold',15), highlightbackground='gray',highlightcolor=bg_color,highlightthickness=2)
    StudContEnt.place(x=5,y=390, width=180)
    StudContEnt.bind('<KeyRelease>',
    lambda e: removeHightlightWaring(entry=StudContEnt))

    StudClassLb= tk.Label(AddAccountPagefm,text='Select Studen Class', font=('Bold',12))
    StudClassLb.place(x=5,y=445)

    SelectClassBtn = Combobox(AddAccountPagefm,font=('Bold',15),state='readonly',values=classList)
    SelectClassBtn.place(x=5,y=475,width=180,height=30)
    # SelectClassBtn.bind('<KeyRelease>',
    # lambda e: removeHightlightWaring(entry=SelectClassBtn))

    StudenIdLb = tk.Label(AddAccountPagefm,text='Student ID Number:',font=('Bold',12))
    StudenIdLb.place(x=240, y=35)

    StudenId = tk.Entry(AddAccountPagefm,font=('bold',18),bd=0)
    # StudenId.insert(tk.END,'1367')
    StudenId.config(state='readonly')
    GenerateIdNumber()
    StudenId.place(x=380,y=35,width=80)

    IdInfoLb = tk.Label(AddAccountPagefm,text='Automatically Genrated Id number !\n Remember Using this Id number \nStudent will login Account',justify=tk.LEFT) 
    IdInfoLb.place(x=240,y=65)

    
    StudEmailLb= tk.Label(AddAccountPagefm,text='Enter email address ', font=('Bold',12))
    StudEmailLb.place(x=240,y=130)

    StudEmailEnt = tk.Entry(AddAccountPagefm, font=('Bold',15), highlightbackground='gray',highlightcolor=bg_color,highlightthickness=2)
    StudEmailEnt.place(x=240,y=160, width=180)
    StudEmailEnt.bind('<KeyRelease>',
    lambda e: removeHightlightWaring(entry=StudEmailEnt))

    EmailInfoLb = tk.Label(AddAccountPagefm,text=
'''Via email student can recover account
in case forgetting password
Student will get future notification''',justify=tk.LEFT) 
    EmailInfoLb.place(x=240,y=200)

    AccountPasswordLb= tk.Label(AddAccountPagefm,text='Create Account Password.', font=('Bold',12))
    AccountPasswordLb.place(x=240,y=275)

    AccountPasswordEnt = tk.Entry(AddAccountPagefm, font=('Bold',15), highlightbackground='gray',highlightcolor=bg_color,highlightthickness=2)
    AccountPasswordEnt.place(x=240,y=307, width=180) 
    AccountPasswordEnt.bind('<KeyRelease>',
    lambda e: removeHightlightWaring(entry=AccountPasswordEnt))
    AccountPassInfoLb = tk.Label(AddAccountPagefm,text='''Via this password and student ID
student can login his account 
    ''',justify=tk.LEFT) 
    AccountPassInfoLb.place(x=240,y=345)

    homeBtn = tk.Button(AddAccountPagefm,text='Home',font=('Bold',15),bg='red',fg='white',bd=0,command=forwardToWelcomePage)
    homeBtn.place(x=240,y=420)
    SubmitBtn = tk.Button(AddAccountPagefm,text='Submit',font=('Bold',15),bg=bg_color,fg='white',bd=0,command=checkInputVlidation)
    SubmitBtn.place(x=360,y=420)
    AddAccountPagefm.pack(pady=5)
    AddAccountPagefm.pack_propagate(False)
    AddAccountPagefm.configure(width=480,height=580)

def AddTeacherAccountPage():
    picPath = tk.StringVar()
    picPath.set('')

    def openPic():
        path = askopenfilename()
        if path:
            img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
            picPath.set(path)
            AddPicBtn.config(image=img)
            AddPicBtn.image = img

    def forwardToWelcomePage():
        ans = ConfirmationBox(message='Do you want to leave the registration form?')
        if ans:
            AddAccountPagefm.destroy()
            root.update()
            WelcomePage()

    def removeHighlightWarning(entry):
        if entry['highlightbackground'] != 'gray':
            if entry.get() != '':
                entry.config(highlightcolor=bg_color, highlightbackground='gray')

    def checkInvalidEmail(email):
        pattern = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"
        return re.match(pattern, email)

    def generateIdNumber():
        generatedId = ''
        for _ in range(6):
            generatedId += str(random.randint(0, 9))
        if not checkTeacherIdAlreadyExists(id_number=generatedId):
            TeacherId.config(state=tk.NORMAL)
            TeacherId.delete(0, tk.END)
            TeacherId.insert(tk.END, generatedId)
            TeacherId.config(state='readonly')
        else:
            generateIdNumber()

    def checkInputValidation():
        if TeacherNameEnt.get() == '':
            TeacherNameEnt.config(highlightcolor='red', highlightbackground='red')
            TeacherNameEnt.focus()
            messageBox(message='Teacher full name is required')
        elif TeacherAgeEnt.get() == '':
            TeacherAgeEnt.config(highlightcolor='red', highlightbackground='red')
            TeacherAgeEnt.focus()
            messageBox(message='Teacher age is required')
        elif TeacherContEnt.get() == '':
            TeacherContEnt.config(highlightcolor='red', highlightbackground='red')
            TeacherContEnt.focus()
            messageBox(message='Teacher contact number is required')
        elif TeacherEmailEnt.get() == '':
            TeacherEmailEnt.config(highlightcolor='red', highlightbackground='red')
            TeacherEmailEnt.focus()
            messageBox(message='Teacher email is required')
        elif not checkInvalidEmail(TeacherEmailEnt.get().lower()):
            TeacherEmailEnt.config(highlightcolor='red', highlightbackground='red')
            TeacherEmailEnt.focus()
            messageBox(message='Please enter a valid email address')
        elif SelectSubjectBtn.get() == '':
            SelectSubjectBtn.config(highlightcolor='red', highlightbackground='red')
            SelectSubjectBtn.focus()
            messageBox(message='Teacher subject is required')
        elif AccountPasswordEnt.get() == '':
            AccountPasswordEnt.config(highlightcolor='red', highlightbackground='red')
            AccountPasswordEnt.focus()
            messageBox(message='Teacher password is required')
        else:
            pic_data = b''
            if picPath.get() != '':
                resize_pic = Image.open(picPath.get()).resize((100, 100))
                resize_pic.save('temp_pic.png')
                with open('temp_pic.png', 'rb') as read_data:
                    pic_data = read_data.read()
            else:
                with open('images/add_image.png', 'rb') as read_data:
                    pic_data = read_data.read()
                picPath.set('images/add_image.png')

            addTeacherdata(
                id_number=TeacherId.get(),
                password=AccountPasswordEnt.get(),
                name=TeacherNameEnt.get(),
                age=TeacherAgeEnt.get(),
                gender=TeacherGender.get(),
                phone_number=TeacherContEnt.get(),
                subject=SelectSubjectBtn.get(),
                email=TeacherEmailEnt.get(),
                pic_data=pic_data
            )

            data = f"""
{TeacherId.get()}
{TeacherNameEnt.get()}
{TeacherAgeEnt.get()}
{TeacherGender.get()}
{TeacherContEnt.get()}
{SelectSubjectBtn.get()}
{TeacherEmailEnt.get()}
"""
            messageBox('Account successfully created')
            getTeacherCard = drawStudentcard(studentPicPath=picPath.get(), studentData=data)
            studentCardPage(getTeacherCard)
            AddAccountPagefm.destroy()
            root.update()

    subjectList = ['Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'Biology', 'English']
    TeacherGender = tk.StringVar()
    AddAccountPagefm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=4)

    AddPicSecFm = tk.Frame(AddAccountPagefm, highlightbackground=bg_color, highlightthickness=2)
    AddPicBtn = tk.Button(AddPicSecFm, image=AddStudPicIcon, bd=0, command=openPic)
    AddPicBtn.pack()
    AddPicSecFm.place(x=5, y=5, width=105, height=105)

    TeacherNameLb = tk.Label(AddAccountPagefm, text='Enter Teacher name', font=('Bold', 12))
    TeacherNameLb.place(x=5, y=130)

    TeacherNameEnt = tk.Entry(AddAccountPagefm, font=('Bold', 15), highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    TeacherNameEnt.place(x=5, y=160, width=180)
    TeacherNameEnt.bind('<KeyRelease>', lambda e: removeHighlightWarning(entry=TeacherNameEnt))

    TeacherGenderLb = tk.Label(AddAccountPagefm, text='Select Teacher Gender', font=('Bold', 12))
    TeacherGenderLb.place(x=5, y=210)
    MaleGenderBtn = tk.Radiobutton(AddAccountPagefm, text='Male', font=('bold', 12), variable=TeacherGender, value='male')
    MaleGenderBtn.place(x=5, y=235)
    FemaleGenderBtn = tk.Radiobutton(AddAccountPagefm, text='Female', font=('bold', 12), variable=TeacherGender, value='female')
    FemaleGenderBtn.place(x=75, y=235)
    TeacherGender.set('male')

    TeacherAgeLb = tk.Label(AddAccountPagefm, text='Enter Teacher Age', font=('Bold', 12))
    TeacherAgeLb.place(x=5, y=275)

    TeacherAgeEnt = tk.Entry(AddAccountPagefm, font=('Bold', 15), highlightbackground='gray', highlightcolor=bg_color, highlightthickness=2)
    TeacherAgeEnt.place(x=5, y=305, width=180)
    TeacherAgeEnt.bind('<KeyRelease>', lambda e: removeHighlightWarning(entry=TeacherAgeEnt))

    TeacherContLb = tk.Label(AddAccountPagefm, text='Enter Contact number', font=('Bold', 12))
    TeacherContLb.place(x=5, y=360)

    TeacherContEnt = tk.Entry(AddAccountPagefm, font=('Bold', 15), highlightbackground='gray', highlightcolor=bg_color, highlightthickness=2)
    TeacherContEnt.place(x=5, y=390, width=180)
    TeacherContEnt.bind('<KeyRelease>', lambda e: removeHighlightWarning(entry=TeacherContEnt))

    TeacherSubjectLb = tk.Label(AddAccountPagefm, text='Select Teacher Subject', font=('Bold', 12))
    TeacherSubjectLb.place(x=5, y=445)

    SelectSubjectBtn = Combobox(AddAccountPagefm, font=('Bold', 15), state='readonly', values=subjectList)
    SelectSubjectBtn.place(x=5, y=475, width=180, height=30)

    TeacherIdLb = tk.Label(AddAccountPagefm, text='Teacher ID Number:', font=('Bold', 12))
    TeacherIdLb.place(x=240, y=35)

    TeacherId = tk.Entry(AddAccountPagefm, font=('bold', 18), bd=0)
    TeacherId.config(state='readonly')
    generateIdNumber()
    TeacherId.place(x=380, y=35, width=80)

    IdInfoLb = tk.Label(AddAccountPagefm, text='Automatically Generated ID number!\nRemember Using this ID number Teacher will login Account', justify=tk.LEFT)
    IdInfoLb.place(x=240, y=65)

    TeacherEmailLb = tk.Label(AddAccountPagefm, text='Enter email address', font=('Bold', 12))
    TeacherEmailLb.place(x=240, y=130)

    TeacherEmailEnt = tk.Entry(AddAccountPagefm, font=('Bold', 15), highlightbackground='gray', highlightcolor=bg_color, highlightthickness=2)
    TeacherEmailEnt.place(x=240, y=160, width=180)
    TeacherEmailEnt.bind('<KeyRelease>', lambda e: removeHighlightWarning(entry=TeacherEmailEnt))

    EmailInfoLb = tk.Label(AddAccountPagefm, text='''\nVia email teacher can recover account\n1 in case of forgetting password\nTeacher will get future notification''', justify=tk.LEFT)
    EmailInfoLb.place(x=240, y=200)

    AccountPasswordLb = tk.Label(AddAccountPagefm, text='Create Account Password', font=('Bold', 12))
    AccountPasswordLb.place(x=240, y=275)

    AccountPasswordEnt = tk.Entry(AddAccountPagefm, font=('Bold', 15), highlightbackground='gray', highlightcolor=bg_color, highlightthickness=2)
    AccountPasswordEnt.place(x=240, y=307, width=180)
    AccountPasswordEnt.bind('<KeyRelease>', lambda e: removeHighlightWarning(entry=AccountPasswordEnt))

    AccountPassInfoLb = tk.Label(AddAccountPagefm, text='''\nVia this password and teacher ID\nteacher can login to their account''', justify=tk.LEFT)
    AccountPassInfoLb.place(x=240, y=345)

    homeBtn = tk.Button(AddAccountPagefm, text='Home', font=('Bold', 15), bg='red', fg='white', bd=0, command=forwardToWelcomePage)
    homeBtn.place(x=240, y=420)
    SubmitBtn = tk.Button(AddAccountPagefm, text='Submit', font=('Bold', 15), bg=bg_color, fg='white', bd=0, command=checkInputValidation)
    SubmitBtn.place(x=360, y=420)

    AddAccountPagefm.pack(pady=5)
    AddAccountPagefm.pack_propagate(False)
    AddAccountPagefm.configure(width=480, height=580)

def TeacherDashboard(Teacher_id):

    getTeacherDetails = FetchstudentData(f"SELECT name, age , gender,subject, phone_number,email FROM Teacher_data WHERE id_number == '{Teacher_id}' ")

    getTeacherPic = FetchstudentData(f"SELECT image FROM Teacher_data WHERE id_number == '{Teacher_id}' ")

    teacherPic = BytesIO(getTeacherPic[0][0])
    
    # print(studentPic)

    def switch(indicator,page):

        homeBtnIndicator.config(bg='#B39DDB')
        viewDetailsBtnIndicator.config(bg='#B39DDB')
        homeBtnIndicator.config(bg='#B39DDB')
        findStudentBtnIndicator.config(bg='#B39DDB')
        announcementBtnIndicator.config(bg='#B39DDB')
        attendanceBtnIndicator.config(bg='#B39DDB')
        toDoListBtnIndicator.config(bg='#B39DDB')

        indicator.config(bg=bg_color)
        for child in PagesFm.winfo_children():
            child.destroy()
            root.update()
        page()    
    dashboadrFm = tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)


    optionsFm = tk.Frame(dashboadrFm, highlightbackground=bg_color,highlightthickness=2, bg='#B39DDB')
    optionsFm.place(x=0,y=0, width=125,height=575)

    homeBtn = tk.Button(optionsFm, text='HOME', font=('Bold',15), fg=bg_color, bg='#B39DDB',bd=0, command= lambda: switch(indicator=homeBtnIndicator,page=HomePage))
    homeBtn.place(x=10,y=50)

    homeBtnIndicator = tk.Label(optionsFm,text="",bg=bg_color)
    homeBtnIndicator.place(x=5, y=48, width=3, height=40)
    
    findStudentBtn = tk.Button(optionsFm, text='Find\nStudent', font=('Bold',15), fg=bg_color, bg='#B39DDB',bd=0, command= lambda: switch(indicator=findStudentBtnIndicator, page=findStudentPage))
    findStudentBtn.place(x=10,y=100)

    findStudentBtnIndicator = tk.Label(optionsFm,text="",bg='#B39DDB')
    findStudentBtnIndicator.place(x=5, y=108, width=3, height=40)

    announcementBtn = tk.Button(optionsFm, text='ANNOUNCE\nMENT🔔', font=('Bold',15), fg=bg_color, bg='#B39DDB',bd=0, command= lambda: switch(indicator=announcementBtnIndicator, page=announcementPage))
    announcementBtn.place(x=10,y=170)

    announcementBtnIndicator = tk.Label(optionsFm,text="",bg='#B39DDB')
    announcementBtnIndicator.place(x=5, y=175, width=3, height=40)

    attendanceBtn = tk.Button(optionsFm, text='ATTENCE\nDANCE✔️', font=('Bold',15), fg=bg_color, bg='#B39DDB',bd=0, command= lambda: switch(indicator=attendanceBtnIndicator,page=attendancePage))
    attendanceBtn.place(x=10,y=240)

    attendanceBtnIndicator = tk.Label(optionsFm,text="",bg='#B39DDB')
    attendanceBtnIndicator.place(x=5, y=245, width=3, height=40)

    toDoListBtn = tk.Button(optionsFm, text='toDoList⚒️', font=('Bold',15), fg=bg_color, bg='#B39DDB',bd=0, command= lambda: switch(indicator=toDoListBtnIndicator, page=toDoListPage))
    toDoListBtn.place(x=10,y=310)

    toDoListBtnIndicator = tk.Label(optionsFm,text="",bg='#B39DDB')
    toDoListBtnIndicator.place(x=5, y=315, width=3, height=40)

    viewDetailsBtn = tk.Button(optionsFm, text='view Details', font=('Bold',15), fg=bg_color, bg='#B39DDB',bd=0, command= lambda: switch(indicator=viewDetailsBtnIndicator,page=viewDetailsPage))
    viewDetailsBtn.place(x=10,y=380)

    viewDetailsBtnIndicator = tk.Label(optionsFm,text="",bg='#B39DDB')
    viewDetailsBtnIndicator.place(x=5, y=385, width=3, height=40)

    logOutBtn = tk.Button(optionsFm, text='log Out', font=('Bold',15), fg=bg_color, bg='#B39DDB',bd=0)
    logOutBtn.place(x=10,y=450)



    def HomePage():
        StudentPicImageObj = Image.open(teacherPic)
        size = 100
        mask = Image.new(mode='L', size=(size,size))
        DrawCircle = ImageDraw.Draw(im=mask)
        DrawCircle.ellipse(xy=(0,0,size,size), fill=255,outline=True)
        output = ImageOps.fit(image=StudentPicImageObj,size=mask.size,centering=(1,1))
        output.putalpha(mask)

        studentPicture = ImageTk.PhotoImage(output)

        homePageFm = tk.Frame(PagesFm)

        studentPicLb = tk.Label(homePageFm,image=studentPicture)
        studentPicLb.image = studentPicture
        studentPicLb.place(x=10,y=10)

        # hiLb = tk.Label(homePageFm, text= f"hi { getTeacherDetails[0][0]}",font=('Bold',15))
        hiLb = tk.Label(homePageFm, 
                text=f"hi {getTeacherDetails[0][0]}, {'sir' if getTeacherDetails[0][2] == 'male' else 'mam'}", 
                font=('Bold', 15))
        hiLb.place(x=130,y=50)
#         studentDetails = f"""
# Teacher Id : {Teacher_id}\n
# Name: {getTeacherDetails[0][0]}\n
# Age: {getTeacherDetails[0][1]}\n
# Gender : {getTeacherDetails[0][2]}\n
# main subject: {getTeacherDetails[0][3]}\n 
# contact : {getTeacherDetails[0][4]}\n 
# Email: {getTeacherDetails[0][5]}\n  """
#         StudentDetalisLb = tk.Label(homePageFm,text= studentDetails, font=('Bold',13), justify=tk.LEFT)
#         StudentDetalisLb.place(x=20,y=130)
        classListLb = tk.Label(homePageFm,text='Number of student by class.',font=('Bold',13),bg=bg_color,fg='white')
        classListLb.place(x=20,y=130)

        studentNumberLb = tk.Label(homePageFm, text='',font=('Bold',13), justify=tk.LEFT)
        studentNumberLb.place(x=20,y=170)
        for i in classList:
            result = FetchstudentData(query=f"SELECT COUNT(*) FROM Student_data WHERE class == '{i}' ")
            # print(i,result)
            studentNumberLb['text']+= f" {i} Class:   {result[0][0]} \n\n"

        homePageFm.pack(fill=tk.BOTH, expand=True)



    def findStudentPage():

        def findStudent():
            # foundData =''
            if findByOptionBtn.get() == 'id':
                foundData =FetchstudentData(query=f"SELECT id_number, name,class, gender FROM Student_data WHERE id_number == '{searchInput.get()}' ")
                print(foundData)
                
            elif findByOptionBtn.get() == 'name':
                foundData =FetchstudentData(query=f"SELECT id_number, name,class, gender FROM Student_data WHERE name LIKE '%{searchInput.get()}%' ")
                print(foundData)

            elif findByOptionBtn.get() == 'gender':
                foundData =FetchstudentData(query=f"SELECT id_number, name,class, gender FROM Student_data WHERE gender == '{searchInput.get()}' ")     
                print(foundData)

            elif findByOptionBtn.get() == 'class':
                foundData =FetchstudentData(query=f"SELECT id_number, name,class, gender FROM Student_data WHERE class == '{searchInput.get()}' ")     
                print(foundData)
                    
                if foundData:
                    for item in recordTable.get_children():
                        recordTable.delete(item)

                    for details in foundData:
                        recordTable.insert(parent='',index='end', values=details)
                else:
                    for item in recordTable.get_children():
                        recordTable.delete(item)

        def generateStudentCard():

            selection = recordTable.selection()
            selected_id = recordTable.item(item=selection, option='values')
            print(selected_id)


              

        searchFilters = ['id','name','class','gender']
        findStudentPageFm = tk.Frame(PagesFm)

        findStudentRecordLb = tk.Label(findStudentPageFm,text='Find student Record', font=('Bold',13), fg='white', bg=bg_color)
        findStudentRecordLb.place(x=20, y=10, width=300)

        findByLb = tk.Label(findStudentPageFm, text='Find by', font=('Bold',12))
        findByLb.place(x=15, y=50)

        findByOptionBtn=Combobox(findStudentPageFm,font=('Bold',12), state='readonly', values=searchFilters)
        findByOptionBtn.place(x=80,y=50,width=80)
        findByOptionBtn.set('id')

        searchInput = tk.Entry(findStudentPageFm,font=('Bold',12))
        searchInput.place(x=20, y=90)
        searchInput.bind('<KeyRelease>', lambda e: findStudent())

        recordTableLb =tk.Label(findStudentPageFm,font=('Bold',12),text='Record table',bg=bg_color,fg='white')
        recordTableLb.place(x=20,y=160, width=300)

        recordTable = Treeview(findStudentPageFm)
        recordTable.place(x=0,y=200,width=350)

        recordTable['columns']= ('id', 'name', 'class', 'gender')

        recordTable.column('#0', stretch=tk.NO,width=0)

        recordTable.heading('id',text='Id Number', anchor=tk.W)
        recordTable.column('id',width=50,anchor=tk.W)

        recordTable.heading('name',text='Name', anchor=tk.W)
        recordTable.column('name',width=90,anchor=tk.W)

        recordTable.heading('class',text='Class', anchor=tk.W)
        recordTable.column('class',width=40,anchor=tk.W)

        recordTable.heading('gender',text='Gender', anchor=tk.W)
        recordTable.column('gender',width=40,anchor=tk.W)  

        generateStudentCardBtn = tk.Button(findStudentPageFm, text='Genrate student card', font=('Bold',13), bg=bg_color,fg='white')
        generateStudentCardBtn.place(x=160, y= 450)

        clearBtn = tk.Button(findStudentPageFm, text='Clear', font=('Bold',13), bg=bg_color,fg='white')
        clearBtn.place(x=10, y= 450)


        findStudentPageFm.pack(fill=tk.BOTH, expand=True)


    def attendancePage():
        def mark_attendance(selected_date):
            conn = sqlite3.connect("attendance.db")
            cursor = conn.cursor()

            for roll_no, var in attendance_vars.items():
                status = 'Present' if var.get() else 'Pass'
                cursor.execute("INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)", (roll_no, selected_date, status))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Attendance marked successfully for {selected_date}!")

        def view_30_days_attendance(roll_no):
            conn = sqlite3.connect("attendance.db")
            cursor = conn.cursor()

            end_date = datetime.now().date()
            start_date = (end_date - timedelta(days=30)).strftime("%Y-%m-%d")
            end_date = end_date.strftime("%Y-%m-%d")

            cursor.execute("""
                SELECT date, status FROM attendance
                WHERE roll_no = ? AND date BETWEEN ? AND ?
                ORDER BY date
            """, (roll_no, start_date, end_date))
            records = cursor.fetchall()

            conn.close()

            for row in tree.get_children():
                tree.delete(row)

            for date, status in records:
                tree.insert("", "end", values=(roll_no, date, status))

        attendanceFm = tk.Frame(PagesFm)

        tk.Label(attendanceFm, text="Attendance System", font=("Helvetica", 16, "bold"), pady=10).pack()

        date_frame = ttk.LabelFrame(attendanceFm, text="Date Selection", padding=10)
        date_frame.pack(pady=10, fill="x")

        tk.Label(date_frame, text="Select Date:", font=("Helvetica", 12)).pack(side="left", padx=5)
        date_picker = DateEntry(date_frame, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern='yyyy-MM-dd')
        date_picker.pack(side="left", padx=5)

        attendance_vars = {}

        def create_attendance_widgets():
            canvas = tk.Canvas(attendanceFm)
            scrollbar = ttk.Scrollbar(attendanceFm, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            for roll_no in range(1301, 1373):
                var = tk.BooleanVar(value=True)
                attendance_vars[roll_no] = var
                tk.Checkbutton(
                    scrollable_frame,
                    text=f"Roll No: {roll_no}",
                    variable=var,
                    anchor="center",
                    width=20
                ).pack(anchor="w")

        create_attendance_widgets()

        tk.Button(attendanceFm, text="Save Attendance", command=lambda: mark_attendance(date_picker.get()), bg="green", fg="white", font=("Helvetica", 12)).pack(pady=10)

        view_frame = ttk.LabelFrame(attendanceFm, text="View Attendance", padding=10)
        view_frame.pack(pady=10, fill="both", expand=True)

        tk.Label(view_frame, text="Enter Roll No to View Last 30 Days Attendance:", font=("Helvetica", 12)).pack(pady=5)
        roll_no_entry = tk.Entry(view_frame, font=("Helvetica", 12))
        roll_no_entry.pack(pady=5)

        tk.Button(view_frame, text="View 30 Days Attendance", command=lambda: view_30_days_attendance(roll_no_entry.get()), bg="orange", fg="white", font=("Helvetica", 12)).pack(pady=5)

        tree_frame = ttk.LabelFrame(attendanceFm, text="Attendance Records", padding=10)
        tree_frame.pack(pady=10, fill="both", expand=True)

        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side="right", fill="y")

        tree = ttk.Treeview(tree_frame, columns=("Roll No", "Date", "Status"), show="headings", yscrollcommand=tree_scroll.set)
        tree.heading("Roll No", text="Roll No")
        tree.heading("Date", text="Date")
        tree.heading("Status", text="Status")
        tree.pack(fill="both", expand=True)

        tree_scroll.config(command=tree.yview)
        attendanceFm.pack(fill=tk.BOTH, expand=True)



    def announcementPage():

        selecetedClass = []
        def add_class(name):
            if selecetedClass.count(name):
                selecetedClass.remove(name)
            else:    
                selecetedClass.append(name)
                print(selecetedClass)

        def collectEmails():
            for _class in selecetedClass:
                email = FetchstudentData("SELECT email  FROM Student_data WHERE class== '{_class}' ")    
                print(email)    

        announcementPageFm = tk.Frame(PagesFm)

        subjectLb = tk.Label(announcementPageFm, text='enter announcement subject.',font=('Bold',12))
        subjectLb.place(x=10,y=10)

        announcementsubject = tk.Entry(announcementPageFm,font=('Bold',12))
        announcementsubject.place(x=10,y=40, width=210, height=25)

        announcementMessage = ScrolledText(announcementPageFm,font=('Bold',12))
        announcementMessage.place(x=10,y=100, width=300, height=200)

        classesListLb = tk.Label(announcementPageFm, text='Select class to announce',font=('Bold',12))
        classesListLb.place(x=10,y=320)

        yPosition =350
        for grade in classList:
            classCheckBtn = tk.Checkbutton(announcementPageFm, text=f'Class {grade}',command=lambda grade=grade: add_class(name=grade))
            classCheckBtn.place(x=10 , y=yPosition)
            yPosition+=25

            sendAnnouncementBtn = tk.Button(announcementPageFm,text='Send announcement', font=('Bold',12), bg=bg_color, fg='white',command=collectEmails)

            sendAnnouncementBtn.place(x=180,y=520)

        announcementPageFm.pack(fill=tk.BOTH, expand=True)

    def attendancepage():
        pass
 
    # def toDoListPage():
    #     tasks = []

    #     def add_task():
    #         task = taskInput.get()
    #         if task.strip():
    #             tasks.append(task)
    #             update_task_list()
    #             taskInput.delete(0, tk.END)

    #     def delete_task():
    #         selected_task_indices = taskList.curselection()
    #         for index in reversed(selected_task_indices):
    #             del tasks[index]
    #         update_task_list()

    #     def update_task_list():
    #         taskList.delete(0, tk.END)
    #         for i, task in enumerate(tasks, 1):
    #             taskList.insert(tk.END, f"{i}. {task}")

    #     toDoListFm = tk.Frame(PagesFm)

    #     taskInput = tk.Entry(toDoListFm, font=('Bold', 12))
    #     taskInput.place(x=20, y=20, width=200)

    #     addTaskBtn = tk.Button(toDoListFm, text='Add Task', font=('Bold', 12), bg=bg_color, fg='white',
    #                             command=add_task)
    #     addTaskBtn.place(x=230, y=18)

    #     deleteTaskBtn = tk.Button(toDoListFm, text='Delete Selected', font=('Bold', 12), bg='red', fg='white',
    #                                command=delete_task)
    #     deleteTaskBtn.place(x=20, y=50)

    #     taskList = tk.Listbox(toDoListFm, font=('Bold', 12), selectmode=tk.MULTIPLE)
    #     taskList.place(x=20, y=90, width=300, height=300)

    #     toDoListFm.pack(fill=tk.BOTH, expand=True)

    def toDoListPage():

        # Initialize database
        conn = sqlite3.connect("StudentsAccounts.db")
        cursor = conn.cursor()

        # Create a table for tasks if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            task TEXT NOT NULL
        )
        """)
        conn.commit()

        def add_task():
            selected_date = calendar.get_date()
            task = taskInput.get().strip()

            if not task:
                messagebox.showwarning("Input Error", "Task cannot be empty!")
                return

            cursor.execute("INSERT INTO tasks (date, task) VALUES (?, ?)", (selected_date, task))
            conn.commit()
            taskInput.delete(0, tk.END)
            update_task_list(selected_date)

        def delete_task():
            selected_date = calendar.get_date()
            cursor.execute("SELECT id FROM tasks WHERE date = ?", (selected_date,))
            tasks = cursor.fetchall()

            if tasks:
                last_task_id = tasks[-1][0]
                cursor.execute("DELETE FROM tasks WHERE id = ?", (last_task_id,))
                conn.commit()
                update_task_list(selected_date)
                messagebox.showinfo("Task Deleted", "Last task for the selected date has been removed.")
            else:
                messagebox.showwarning("No Tasks", "No tasks to delete for the selected date.")

        def update_task_list(selected_date):
            taskList.delete(0, tk.END)
            cursor.execute("SELECT task FROM tasks WHERE date = ?", (selected_date,))
            tasks = cursor.fetchall()

            if tasks:
                for i, task in enumerate(tasks, 1):
                    taskList.insert(tk.END, f"{i}. {task[0]}")
            else:
                taskList.insert(tk.END, "No tasks for this date.")

        def show_tasks_for_date():
            selected_date = calendar.get_date()
            update_task_list(selected_date)

        toDoListFm = tk.Frame(PagesFm)

        calendar = Calendar(toDoListFm, selectmode="day", date_pattern="yyyy-mm-dd")
        calendar.place(x=20, y=20, width=300, height=200)

        taskInput = tk.Entry(toDoListFm, font=('Bold', 12))
        taskInput.insert(tk.END,"Enter your task here")
        taskInput.place(x=20, y=230, width=200)

        addTaskBtn = tk.Button(toDoListFm, text='Add Task', font=('Bold', 12), bg=bg_color, fg='white',
                                command=add_task)
        addTaskBtn.place(x=230, y=228)

        deleteTaskBtn = tk.Button(toDoListFm, text='Delete Last Task', font=('Bold', 12), bg='red', fg='white',
                                   command=delete_task)
        deleteTaskBtn.place(x=20, y=260)

        showTaskBtn = tk.Button(toDoListFm, text='Show Tasks', font=('Bold', 12), bg='blue', fg='white',
                                 command=show_tasks_for_date)
        showTaskBtn.place(x=230, y=260)

        taskList = tk.Listbox(toDoListFm, font=('Bold', 12))
        taskList.place(x=20, y=300, width=300, height=200)

        toDoListFm.pack(fill=tk.BOTH, expand=True)

    PagesFm = tk.Frame(dashboadrFm)
    PagesFm.place(x=122, y=5, width=350, height=550)
    HomePage()

    dashboadrFm.pack(pady=5)
    dashboadrFm.pack_propagate(False)
    dashboadrFm.configure(width=480, height=580)

    def viewDetailsPage():
        pass
    PagesFm = tk.Frame(dashboadrFm)
    PagesFm.place(x=122,y=5, width=350, height=550)
    HomePage()
    
    

    dashboadrFm.pack(pady=5)
    dashboadrFm.pack_propagate(False)
    dashboadrFm.configure(width=480, height=580)

# initDatabase()
# StudentDashBoard(Student_id=280810)
# TeacherDashBoard(Student_id=280810)
# AddTeacherAccountPage()
# studentCardPage()
# drawStudentcard()
TeacherDashboard(Teacher_id='020035')
# TeacherLoginPage()
# AdminLoginPage()
# StudentLoginPage()
# WelcomePage()
# TeacherDashboard()
# AddStudentAccountPage()
# forgetPasswordPage()
# sendMailToStudent(email='guptavyankatesh617@gmail.com',message ='<h1>i am back bhai</h1>',subject='testing')

# Start the main loop
root.mainloop()
