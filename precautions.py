import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import webbrowser



##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Tips")
img = Image.open("E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/111.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
#####For background Image
#loading the images

image2 =Image.open('E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/yoga1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)

logo_label=tk.Label()
logo_label.place(x=0,y=0)

x=1


label_l1 = tk.Label(root, text="Yoga Pose Detection Using Machine Learning",font=("Times New Roman", 18, 'bold'),
                    background="#647C90", fg="white", width=50, height=2)
label_l1.place(x=0, y=0)



def update_label1(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=600)
    
    image2 =Image.open('E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/p2.jpg')
    image2 =image2.resize((w,h), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=200, y=200)
    
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
def update_cal(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=350, y=400)
    
    
###########################################################################
           

def Benefits():
    
#     
    image2 =Image.open('E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/use.jpg')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=60)
        
def Yoga():

    image2 =Image.open('E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/what.png')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=60)
    
def Types():

    image2 =Image.open('E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/types.jpg')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=60)
    
def Routine():

    image2 =Image.open('E:/COMPUTER-IT-PROTECH SOL/PROTECH GROUPS/24CP04-Yoga Pose Detection/100% code-yoga pose detection/Images/rou.webp')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=60)


def vedio():
  
    from subprocess import call
    call(['python','vedio_link.py'])
 
#################################################################################################################
def window():
    root.destroy()


button1 = tk.Button(root, text="Yoga Benefits", command=Benefits, width=14, height=2,bd=0, font=('times', 15, ' bold '),bg="#647C90",fg="white")
button1.place(x=570, y=0)

button2 = tk.Button(root, text="What Is Yoga", command=Yoga, width=14, height=2, bd=0,font=('times', 15, ' bold '),bg="#647C90",fg="white")
button2.place(x=720, y=0)

button3 = tk.Button(root, text="Types Of Yoga", command=Types, width=14, height=2,bd=0, font=('times', 15, ' bold '),bg="#647C90",fg="white")
button3.place(x=880, y=0)

button4 = tk.Button(root, text="Routine", command=Routine, width=12, height=2,bd=0,bg="#647C90",fg="white", font=('times', 15, ' bold '))
button4.place(x=1050, y=0)

button4 = tk.Button(root, text="Links Of Videos", command=vedio,width=14, height=2,bd=0,bg="#647C90",fg="white", font=('times', 15, ' bold '))
button4.place(x=1200, y=0)


root.mainloop()
