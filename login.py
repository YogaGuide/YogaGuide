import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import cv2

##############################################+=============================================================
root = tk.Tk()
root.configure(background="skyblue")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")
img = Image.open("E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/111.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
img = Image.open("E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/111.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)


username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/yoga4.png')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)







def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()



def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, username TEXT, Email TEXT, password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            
            from subprocess import call
            call(["python","Home.py"])
            root.destroy()
            
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')
          
          
           



        
Login_frame=tk.Frame(root,bg="#A5ABA0")
Login_frame.place(x=850,y=0)
        
logolbl=tk.Label(Login_frame,text="Login Here",font=("Algerian", 30, "bold","italic"),bd=5,bg="#A5ABA0",fg="#000000").grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username", compound=LEFT,font=("Times new roman", 20, "bold"),bg="#A5ABA0").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=3,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password", compound=LEFT,font=("Times new roman", 20, "bold"),bg="#A5ABA0").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=3,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="#0000FF",fg="#000000", bd=1)
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="#008000",fg="#000000", bd=1)
btn_reg.grid(row=3,column=0,pady=10)
        
        
    

root.mainloop()