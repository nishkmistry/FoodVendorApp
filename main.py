import tkinter as tk
from tkinter.ttk import *
from tkinter import PhotoImage
from time import strftime 
import pyodbc
from PIL import Image, ImageTk
import random
from threading import Timer
import time

global food1
food1=0
def clf1():
        global root, food1
        food1 += 1
        global foodquantity1
        foodquantity1['text'] = str(food1)
def rlf1():
        global root, food1
        food1 -= 1
        global foodquantity1
        foodquantity1['text'] = str(food1)
global food2
food2=0
def clf2():
        global root, food2
        food2 += 1
        global foodquantity2
        foodquantity2['text'] = str(food2)
def rlf2():
        global root, food2
        food2 -= 1
        global foodquantity2
        foodquantity2['text'] = str(food1)
global food3
food3=0
def clf3():
        global root, food3
        food3 += 1
        global foodquantity3
        foodquantity3['text'] = str(food3)
def rlf3():
        global root, food3
        food3 -= 1
        global foodquantity3
        foodquantity3['text'] = str(food3)
global food4
food4=0
def clf4():
        global root, food4
        food4 += 1
        global foodquantity4
        foodquantity4['text'] = str(food4)
def rlf4():
        global root, food4
        food4 -= 1
        global foodquantity4
        foodquantity4['text'] = str(food4)
global food5
food5=0
def clf5():
        
        global root, food5
        food5 += 1
        global foodquantity5
        foodquantity5['text'] = str(food5)
def rlf5():
        
        global root, food5
        food5 -= 1
        global foodquantity5
        foodquantity5['text'] = str(food5)
global food6
food6=0
def clf6():
        global root, food6
        food6 += 1
        global foodquantity6
        foodquantity6['text'] = str(food6)
def rlf6():
        global root, food6
        food6 -= 1
        global foodquantity6
        foodquantity6['text'] = str(food6)
global food7
food7=0
def clf7():
        global root, food7
        food7 += 1
        global foodquantity7
        foodquantity7['text'] = str(food7)
def rlf7():
        global root, food7
        food7 -= 1
        global foodquantity7
        foodquantity7['text'] = str(food7)

def login():
        global entry1
        string1= entry1.get()
        #label.configure(text=string)
        #print(string1)
        global entry
        string= entry.get()
        #label.configure(text=string)
        #print(string1)
        t = 0
        #print(t)
        try:
                conn = pyodbc.connect(
                f'DRIVER={{SQL Server}};'
                f'SERVER={"LAPTOP-O5J6SGON\\SQLEXPRESS"};'
                f'DATABASE={"Nis"};'
                f'UID={"sa"};'
                f'PWD={"sa"}'
                )
        
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Table_1")
        
                
                results = cursor.fetchall()

                
                columns = [column[0] for column in cursor.description]
                #print(columns)
                #print(results)
                
                for row in results:
                        #print(row[0].strip(), row[1].strip())
                        if((row[0].strip() == string1) and (row[1].strip() == string)):
                                t=t-1                        
                if(t==-1):
                        customer(string1)
                cursor.close()
                conn.close()
    
        except Exception as e:
                print(f"Error: {e}")
def sp():
        global entry
        if entry['show'] == '*':
                entry['show'] = ''
        else:
                entry['show'] = '*'
def customer(custname):
        global root
        root.destroy()
        root = tk.Tk()
        root.title('Vendor')
        width= root.winfo_screenwidth()               
        height= root.winfo_screenheight()               
        root.geometry("%dx%d" % (width, height))
        gazebo1label=tk.Button(root, text="Gazebo1", font=("Courier 22 bold"), command=g1)
        gazebo1label.place(x=0, y=0)
        gazebo2label=tk.Button(root, text="Gazebo2", font=("Courier 22 bold"), command=g2)
        gazebo2label.place(x=300, y=100)
        dakshinlabel=tk.Button(root, text="Dakshin", font=("Courier 22 bold"), command=dak)
        dakshinlabel.place(x=0, y=100)
        lassilabel=tk.Button(root, text="Lassi House", font=("Courier 22 bold"), command=ls)
        lassilabel.place(x=300, y=0)
        root.mainloop()
def ls():
        global root
        root.destroy()
        root = tk.Tk()
        root.title('Lassi House')
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height*5))
        x1=0
        y1=0
        foodname1=tk.Label(root, text="Tea", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname1.place(x=x1, y=y1)
        foodpic1fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\tea.png")
        foodpic1resize_image = foodpic1fetch.resize((100, 100))
        foodpic1resize_imagefetch = ImageTk.PhotoImage(foodpic1resize_image)
        foodpic1 = tk.Label(root, image=foodpic1resize_imagefetch)
        y1+=35
        foodpic1.place(x=x1, y= y1)
        foodprice1=tk.Label(root, text="Rs.15", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice1.place(x=x1,y=y1)
        foodbuy1=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf1)
        y1+=25
        foodbuy1.place(x=x1,y=y1)
        foodrem1=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf1)
        y1+=25
        foodrem1.place(x=x1, y=y1)
        global foodquantity1
        foodquantity1=tk.Label(root, text=str(food1), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity1.place(x=x1, y=y1)


        foodname2=tk.Label(root, text="Coffee", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname2.place(x=x1, y=y1)
        foodpic2fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\coffee.png")
        foodpic2resize_image = foodpic2fetch.resize((100, 100))
        foodpic2resize_imagefetch = ImageTk.PhotoImage(foodpic2resize_image)
        foodpic2 = tk.Label(root, image=foodpic2resize_imagefetch)
        y1+=35
        foodpic2.place(x=x1, y=y1)
        foodprice2=tk.Label(root, text="Rs.15", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice2.place(x=x1, y=y1)
        foodbuy2=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf2)
        y1+=25
        foodbuy2.place(x=x1, y=y1)
        foodrem2=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf2)
        y1+=25
        foodrem2.place(x=x1, y=y1)
        global foodquantity2
        foodquantity2=tk.Label(root, text=str(food2), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity2.place(x=x1, y=y1)


        foodname3=tk.Label(root, text="Filter Coffee", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname3.place(x=x1, y=y1)
        foodpic3fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\filtercoffee.png")
        foodpic3resize_image = foodpic3fetch.resize((100, 100))
        foodpic3resize_imagefetch = ImageTk.PhotoImage(foodpic3resize_image)
        foodpic3 = tk.Label(root, image=foodpic3resize_imagefetch)
        y1+=35
        foodpic3.place(x=x1, y=y1)
        foodprice3=tk.Label(root, text="Rs.25", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice3.place(x=x1, y=y1)
        foodbuy3=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf3)
        y1+=25
        foodbuy3.place(x=x1, y=y1)
        foodrem3=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf3)
        y1+=25
        foodrem3.place(x=x1, y=y1)
        global foodquantity3
        foodquantity3=tk.Label(root, text=str(food3), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity3.place(x=x1, y=y1)

        x1=150
        y1=0
        foodname4=tk.Label(root, text="Badam or Ragi Malt", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname4.place(x=x1, y=y1)
        foodpic4fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\badam.png")
        foodpic4resize_image = foodpic4fetch.resize((100, 100))
        foodpic4resize_imagefetch = ImageTk.PhotoImage(foodpic4resize_image)
        foodpic4 = tk.Label(root, image=foodpic4resize_imagefetch)
        y1+=35
        foodpic4.place(x=x1, y=y1)
        foodprice4=tk.Label(root, text="Rs.30", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice4.place(x=x1, y=y1)
        foodbuy4=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf4)
        y1+=25
        foodbuy4.place(x=x1, y=y1)
        foodrem4=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf4)
        y1+=25
        foodrem4.place(x=x1, y=y1)
        global foodquantity4
        foodquantity4=tk.Label(root, text=str(food4), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity4.place(x=x1, y=y1)


        foodname5=tk.Label(root, text="Nannari sarbath", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname5.place(x=x1, y=y1)
        foodpic5fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\nannarisarbath.png")
        foodpic5resize_image = foodpic5fetch.resize((100, 100))
        foodpic5resize_imagefetch = ImageTk.PhotoImage(foodpic5resize_image)
        foodpic5 = tk.Label(root, image=foodpic5resize_imagefetch)
        y1+=35
        foodpic5.place(x=x1, y=y1)
        foodprice5=tk.Label(root, text="Rs.30", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice5.place(x=x1, y=y1)
        foodbuy5=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf5)
        y1+=25
        foodbuy5.place(x=x1, y=y1)
        foodrem5=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf5)
        y1+=25
        foodrem5.place(x=x1, y=y1)
        global foodquantity5
        foodquantity5=tk.Label(root, text=str(food5), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity5.place(x=x1, y=y1)


        foodname6=tk.Label(root, text="Buttermilk", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname6.place(x=x1, y=y1)
        foodpic6fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\buttermilk.png")
        foodpic6resize_image = foodpic6fetch.resize((100, 100))
        foodpic6resize_imagefetch = ImageTk.PhotoImage(foodpic6resize_image)
        foodpic6 = tk.Label(root, image=foodpic6resize_imagefetch)
        y1+=35
        foodpic6.place(x=x1, y=y1)
        foodprice6=tk.Label(root, text="Rs.30", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice6.place(x=x1, y=y1)
        foodbuy6=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf6)
        y1+=25
        foodbuy6.place(x=x1, y=y1)
        foodrem6=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf6)
        y1+=25
        foodrem6.place(x=x1, y=y1)
        global foodquantity6
        foodquantity6=tk.Label(root, text=str(food6), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity6.place(x=x1, y=y1)

        x1=400
        y1=0
        foodname7=tk.Label(root, text="Rose milk", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname7.place(x=x1, y=y1)
        foodpic7fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\rosemilk.png")
        foodpic7resize_image = foodpic7fetch.resize((100, 100))
        foodpic7resize_imagefetch = ImageTk.PhotoImage(foodpic7resize_image)
        foodpic7 = tk.Label(root, image=foodpic7resize_imagefetch)
        y1+=35
        foodpic7.place(x=x1, y=y1)
        foodprice7=tk.Label(root, text="Rs.50", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice7.place(x=x1, y=y1)
        foodbuy7=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf7)
        y1+=25
        foodbuy7.place(x=x1, y=y1)
        foodrem7=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf7)
        y1+=25
        foodrem7.place(x=x1, y=y1)
        global foodquantity7
        foodquantity7=tk.Label(root, text=str(food7), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity7.place(x=x1, y=y1)
        Cart=tk.Button(root, text="Cart", font=("Arial", 12, "bold"),bg="white",fg="Black", command=cartla)
        Cart.place(x=(width-100), y=0)
        #verscrollbar = AutoScrollbar(root)
        root.mainloop()
def cartla():
        global root
        #print("Hello, Cart clicked")
        ql = [food1, food2, food3, food4, food5, food6, food7]
        qnl = ["Tea", "Coffee", "Filter Coffee", "Ragi Malt", "Nannari Sarbath", "Buttermilk", "Rose Milk"]
        wtr = [3, 5, 13, 7]
        fp=[15, 15, 25, 30, 30, 30, 50]
        root.destroy()
        root = tk.Tk()
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.title('Billing window')
        titlelable=tk.Label(root, text="Billing window", font=("Arial", 32, "bold"),bg="white",fg="Black")
        titlelable.pack()
        j=0
        j1=0
        j2=0
        k=0
        col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = "Name --------------------- Price ----------- Waiting Time")
        col.pack()
        for i in ql:
            if i>0:
                    j1 = random.choice(wtr)
                    col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = qnl[k] + " --------------------- " + str(ql[k] * fp[k]) + " --------------------- " + str(j1))
                    col.pack()
                    j=j+(ql[k] * fp[k])
                    j2=j2+j1
            k+=1
        col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = "Total --------------------- " + str(j) + " --------------------- " + str(j2))
        col.pack()
        paybtn=tk.Button(root, text="Pay", font=("Arial", 12, "bold"),bg="white",fg="Black", command=lambda:pay(j2))
        paybtn.pack()
        root.mainloop()
def dak():
        global root
        root.destroy()
        root = tk.Tk()
        root.title('Dakshin')
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height*5))
        x1=0
        y1=0
        foodname1=tk.Label(root, text="Omelette", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname1.place(x=x1, y=y1)
        foodpic1fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\omelette.png")
        foodpic1resize_image = foodpic1fetch.resize((100, 100))
        foodpic1resize_imagefetch = ImageTk.PhotoImage(foodpic1resize_image)
        foodpic1 = tk.Label(root, image=foodpic1resize_imagefetch)
        y1+=35
        foodpic1.place(x=x1, y= y1)
        foodprice1=tk.Label(root, text="Rs.30", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice1.place(x=x1,y=y1)
        foodbuy1=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf1)
        y1+=25
        foodbuy1.place(x=x1,y=y1)
        foodrem1=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf1)
        y1+=25
        foodrem1.place(x=x1, y=y1)
        global foodquantity1
        foodquantity1=tk.Label(root, text=str(food1), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity1.place(x=x1, y=y1)


        foodname2=tk.Label(root, text="Chocolate Swiss Roll", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname2.place(x=x1, y=y1)
        foodpic2fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\chocolateswissroll.png")
        foodpic2resize_image = foodpic2fetch.resize((100, 100))
        foodpic2resize_imagefetch = ImageTk.PhotoImage(foodpic2resize_image)
        foodpic2 = tk.Label(root, image=foodpic2resize_imagefetch)
        y1+=35
        foodpic2.place(x=x1, y=y1)
        foodprice2=tk.Label(root, text="Rs.50", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice2.place(x=x1, y=y1)
        foodbuy2=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf2)
        y1+=25
        foodbuy2.place(x=x1, y=y1)
        foodrem2=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf2)
        y1+=25
        foodrem2.place(x=x1, y=y1)
        global foodquantity2
        foodquantity2=tk.Label(root, text=str(food2), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity2.place(x=x1, y=y1)


        foodname3=tk.Label(root, text="Veg Roll", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname3.place(x=x1, y=y1)
        foodpic3fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\vegroll.png")
        foodpic3resize_image = foodpic3fetch.resize((100, 100))
        foodpic3resize_imagefetch = ImageTk.PhotoImage(foodpic3resize_image)
        foodpic3 = tk.Label(root, image=foodpic3resize_imagefetch)
        y1+=35
        foodpic3.place(x=x1, y=y1)
        foodprice3=tk.Label(root, text="Rs.30", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice3.place(x=x1, y=y1)
        foodbuy3=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf3)
        y1+=25
        foodbuy3.place(x=x1, y=y1)
        foodrem3=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf3)
        y1+=25
        foodrem3.place(x=x1, y=y1)
        global foodquantity3
        foodquantity3=tk.Label(root, text=str(food3), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity3.place(x=x1, y=y1)

        x1=150
        y1=0
        foodname4=tk.Label(root, text="Fries", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname4.place(x=x1, y=y1)
        foodpic4fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\fries.png")
        foodpic4resize_image = foodpic4fetch.resize((100, 100))
        foodpic4resize_imagefetch = ImageTk.PhotoImage(foodpic4resize_image)
        foodpic4 = tk.Label(root, image=foodpic4resize_imagefetch)
        y1+=35
        foodpic4.place(x=x1, y=y1)
        foodprice4=tk.Label(root, text="Rs.60", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice4.place(x=x1, y=y1)
        foodbuy4=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf4)
        y1+=25
        foodbuy4.place(x=x1, y=y1)
        foodrem4=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf4)
        y1+=25
        foodrem4.place(x=x1, y=y1)
        global foodquantity4
        foodquantity4=tk.Label(root, text=str(food4), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity4.place(x=x1, y=y1)


        foodname5=tk.Label(root, text="Egg Wrap", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname5.place(x=x1, y=y1)
        foodpic5fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\eggwrap.png")
        foodpic5resize_image = foodpic5fetch.resize((100, 100))
        foodpic5resize_imagefetch = ImageTk.PhotoImage(foodpic5resize_image)
        foodpic5 = tk.Label(root, image=foodpic5resize_imagefetch)
        y1+=35
        foodpic5.place(x=x1, y=y1)
        foodprice5=tk.Label(root, text="Rs.70", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice5.place(x=x1, y=y1)
        foodbuy5=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf5)
        y1+=25
        foodbuy5.place(x=x1, y=y1)
        foodrem5=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf5)
        y1+=25
        foodrem5.place(x=x1, y=y1)
        global foodquantity5
        foodquantity5=tk.Label(root, text=str(food5), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity5.place(x=x1, y=y1)


        foodname6=tk.Label(root, text="Chicken Momos", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname6.place(x=x1, y=y1)
        foodpic6fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\chickenmomos.png")
        foodpic6resize_image = foodpic6fetch.resize((100, 100))
        foodpic6resize_imagefetch = ImageTk.PhotoImage(foodpic6resize_image)
        foodpic6 = tk.Label(root, image=foodpic6resize_imagefetch)
        y1+=35
        foodpic6.place(x=x1, y=y1)
        foodprice6=tk.Label(root, text="Rs.80", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice6.place(x=x1, y=y1)
        foodbuy6=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf6)
        y1+=25
        foodbuy6.place(x=x1, y=y1)
        foodrem6=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf6)
        y1+=25
        foodrem6.place(x=x1, y=y1)
        global foodquantity6
        foodquantity6=tk.Label(root, text=str(food6), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity6.place(x=x1, y=y1)

        x1=400
        y1=0
        foodname7=tk.Label(root, text="Cheese Corn Nuggets", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname7.place(x=x1, y=y1)
        foodpic7fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\cheesecornnuggets.png")
        foodpic7resize_image = foodpic7fetch.resize((100, 100))
        foodpic7resize_imagefetch = ImageTk.PhotoImage(foodpic7resize_image)
        foodpic7 = tk.Label(root, image=foodpic7resize_imagefetch)
        y1+=35
        foodpic7.place(x=x1, y=y1)
        foodprice7=tk.Label(root, text="Rs.70", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice7.place(x=x1, y=y1)
        foodbuy7=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf7)
        y1+=25
        foodbuy7.place(x=x1, y=y1)
        foodrem7=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf7)
        y1+=25
        foodrem7.place(x=x1, y=y1)
        global foodquantity7
        foodquantity7=tk.Label(root, text=str(food7), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity7.place(x=x1, y=y1)
        Cart=tk.Button(root, text="Cart", font=("Arial", 12, "bold"),bg="white",fg="Black", command=cartla3)
        Cart.place(x=(width-100), y=0)
        #verscrollbar = AutoScrollbar(root)
        root.mainloop()
def cartla3():
        global root
        #print("Hello, Cart clicked")
        ql = [food1, food2, food3, food4, food5, food6, food7]
        qnl = ["Omelette", "Chocolate Swiss Roll", "Veg Roll", "Fries", "Egg Wrap", "Chicken Momos", "Cheese Corn Nuggets"]
        wtr = [3, 5, 13, 7]
        fp=[30, 50, 30, 60, 70, 80, 70]
        root.destroy()
        root = tk.Tk()
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.title('Billing window')
        titlelable=tk.Label(root, text="Billing window", font=("Arial", 32, "bold"),bg="white",fg="Black")
        titlelable.pack()
        j=0
        j1=0
        j2=0
        k=0
        col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = "Name --------------------- Price ----------- Waiting Time")
        col.pack()
        for i in ql:
            if i>0:
                    j1 = random.choice(wtr)
                    col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = qnl[k] + " --------------------- " + str(ql[k] * fp[k]) + " --------------------- " + str(j1))
                    col.pack()
                    j=j+(ql[k] * fp[k])
                    j2=j2+j1
            k+=1
        col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = "Total --------------------- " + str(j) + " --------------------- " + str(j2))
        col.pack()
        paybtn=tk.Button(root, text="Pay", font=("Arial", 12, "bold"),bg="white",fg="Black", command=lambda:pay(j2))
        paybtn.pack()
        root.mainloop()
def g1():
        global root
        root.destroy()
        root = tk.Tk()
        root.title('Gazebo 1')
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height*5))
        x1=0
        y1=0
        foodname1=tk.Label(root, text="Idli", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname1.place(x=x1, y=y1)
        foodpic1fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\idli.png")
        foodpic1resize_image = foodpic1fetch.resize((100, 100))
        foodpic1resize_imagefetch = ImageTk.PhotoImage(foodpic1resize_image)
        foodpic1 = tk.Label(root, image=foodpic1resize_imagefetch)
        y1+=35
        foodpic1.place(x=x1, y= y1)
        foodprice1=tk.Label(root, text="Rs.35", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice1.place(x=x1,y=y1)
        foodbuy1=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf1)
        y1+=25
        foodbuy1.place(x=x1,y=y1)
        foodrem1=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf1)
        y1+=25
        foodrem1.place(x=x1, y=y1)
        global foodquantity1
        foodquantity1=tk.Label(root, text=str(food1), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity1.place(x=x1, y=y1)


        foodname2=tk.Label(root, text="Sambar Rice", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname2.place(x=x1, y=y1)
        foodpic2fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\sambarrice.png")
        foodpic2resize_image = foodpic2fetch.resize((100, 100))
        foodpic2resize_imagefetch = ImageTk.PhotoImage(foodpic2resize_image)
        foodpic2 = tk.Label(root, image=foodpic2resize_imagefetch)
        y1+=35
        foodpic2.place(x=x1, y=y1)
        foodprice2=tk.Label(root, text="Rs.60", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice2.place(x=x1, y=y1)
        foodbuy2=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf2)
        y1+=25
        foodbuy2.place(x=x1, y=y1)
        foodrem2=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf2)
        y1+=25
        foodrem2.place(x=x1, y=y1)
        global foodquantity2
        foodquantity2=tk.Label(root, text=str(food2), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity2.place(x=x1, y=y1)


        foodname3=tk.Label(root, text="Pani Poori", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname3.place(x=x1, y=y1)
        foodpic3fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\panipoori.png")
        foodpic3resize_image = foodpic3fetch.resize((100, 100))
        foodpic3resize_imagefetch = ImageTk.PhotoImage(foodpic3resize_image)
        foodpic3 = tk.Label(root, image=foodpic3resize_imagefetch)
        y1+=35
        foodpic3.place(x=x1, y=y1)
        foodprice3=tk.Label(root, text="Rs.50", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice3.place(x=x1, y=y1)
        foodbuy3=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf3)
        y1+=25
        foodbuy3.place(x=x1, y=y1)
        foodrem3=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf3)
        y1+=25
        foodrem3.place(x=x1, y=y1)
        global foodquantity3
        foodquantity3=tk.Label(root, text=str(food3), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity3.place(x=x1, y=y1)

        x1=150
        y1=0
        foodname4=tk.Label(root, text="Vegetable Soup", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname4.place(x=x1, y=y1)
        foodpic4fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\vegetablesoup.png")
        foodpic4resize_image = foodpic4fetch.resize((100, 100))
        foodpic4resize_imagefetch = ImageTk.PhotoImage(foodpic4resize_image)
        foodpic4 = tk.Label(root, image=foodpic4resize_imagefetch)
        y1+=35
        foodpic4.place(x=x1, y=y1)
        foodprice4=tk.Label(root, text="Rs.50", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice4.place(x=x1, y=y1)
        foodbuy4=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf4)
        y1+=25
        foodbuy4.place(x=x1, y=y1)
        foodrem4=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf4)
        y1+=25
        foodrem4.place(x=x1, y=y1)
        global foodquantity4
        foodquantity4=tk.Label(root, text=str(food4), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity4.place(x=x1, y=y1)


        foodname5=tk.Label(root, text="Spring Potato", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname5.place(x=x1, y=y1)
        foodpic5fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\springpotato.png")
        foodpic5resize_image = foodpic5fetch.resize((100, 100))
        foodpic5resize_imagefetch = ImageTk.PhotoImage(foodpic5resize_image)
        foodpic5 = tk.Label(root, image=foodpic5resize_imagefetch)
        y1+=35
        foodpic5.place(x=x1, y=y1)
        foodprice5=tk.Label(root, text="Rs.50", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice5.place(x=x1, y=y1)
        foodbuy5=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf5)
        y1+=25
        foodbuy5.place(x=x1, y=y1)
        foodrem5=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf5)
        y1+=25
        foodrem5.place(x=x1, y=y1)
        global foodquantity5
        foodquantity5=tk.Label(root, text=str(food5), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity5.place(x=x1, y=y1)


        foodname6=tk.Label(root, text="Regular Chicken Shawarma", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname6.place(x=x1, y=y1)
        foodpic6fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\regularchickenshawarma.png")
        foodpic6resize_image = foodpic6fetch.resize((100, 100))
        foodpic6resize_imagefetch = ImageTk.PhotoImage(foodpic6resize_image)
        foodpic6 = tk.Label(root, image=foodpic6resize_imagefetch)
        y1+=35
        foodpic6.place(x=x1, y=y1)
        foodprice6=tk.Label(root, text="Rs.90", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice6.place(x=x1, y=y1)
        foodbuy6=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf6)
        y1+=25
        foodbuy6.place(x=x1, y=y1)
        foodrem6=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf6)
        y1+=25
        foodrem6.place(x=x1, y=y1)
        global foodquantity6
        foodquantity6=tk.Label(root, text=str(food6), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity6.place(x=x1, y=y1)

        x1=400
        y1=0
        foodname7=tk.Label(root, text="Masala Poori", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname7.place(x=x1, y=y1)
        foodpic7fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\masalapoori.png")
        foodpic7resize_image = foodpic7fetch.resize((100, 100))
        foodpic7resize_imagefetch = ImageTk.PhotoImage(foodpic7resize_image)
        foodpic7 = tk.Label(root, image=foodpic7resize_imagefetch)
        y1+=35
        foodpic7.place(x=x1, y=y1)
        foodprice7=tk.Label(root, text="Rs.60", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice7.place(x=x1, y=y1)
        foodbuy7=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf7)
        y1+=25
        foodbuy7.place(x=x1, y=y1)
        foodrem7=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf7)
        y1+=25
        foodrem7.place(x=x1, y=y1)
        global foodquantity7
        foodquantity7=tk.Label(root, text=str(food7), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity7.place(x=x1, y=y1)
        Cart=tk.Button(root, text="Cart", font=("Arial", 12, "bold"),bg="white",fg="Black", command=cartla1)
        Cart.place(x=(width-100), y=0)
        #verscrollbar = AutoScrollbar(root)
        root.mainloop()
def cartla1():
        global root
        #print("Hello, Cart clicked")
        ql = [food1, food2, food3, food4, food5, food6, food7]
        qnl = ["Idli", "Sambar Rice", "Pani Poori", "Vegetable Soup", "Spring Potato", "Regular Chicken Shawarma", "Masala Poori"]
        wtr = [3, 5, 13, 7]
        fp=[35, 60, 50, 50, 50, 90, 60]
        root.destroy()
        root = tk.Tk()
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.title('Billing window')
        titlelable=tk.Label(root, text="Billing window", font=("Arial", 32, "bold"),bg="white",fg="Black")
        titlelable.pack()
        j=0
        j1=0
        j2=0
        k=0
        col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = "Name --------------------- Price ----------- Waiting Time")
        col.pack()
        for i in ql:
            if i>0:
                    j1 = random.choice(wtr)
                    col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = qnl[k] + " --------------------- " + str(ql[k] * fp[k]) + " --------------------- " + str(j1))
                    col.pack()
                    j=j+(ql[k] * fp[k])
                    j2=j2+j1
            k+=1
        col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = "Total --------------------- " + str(j) + " --------------------- " + str(j2))
        col.pack()
        paybtn=tk.Button(root, text="Pay", font=("Arial", 12, "bold"),bg="white",fg="Black", command=lambda:pay(j2))
        paybtn.pack()
        root.mainloop()
def pay(v):
        global root
        root.destroy()
        root = tk.Tk()
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.title("Waiting Window")
        waitimg = Image.open(r"C:\Users\Nishk\Documents\Python\Application\wait.gif")
        waitimgresize_image = waitimg.resize((100, 100))
        waitimgresize_imagefetch = ImageTk.PhotoImage(waitimgresize_image)
        waitimge = tk.Label(root, image=waitimgresize_imagefetch)
        waitimge.pack()
        time.sleep(v)
        notify()
        root.mainloop()

def notify():
        global root
        root.destroy()
        root = tk.Tk()
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.title("Good Bye")
        co=tk.Label(root, font = ('Calibri', 48, 'bold'), text = "Thank you")
        co.pack()
        co1=tk.Label(root, font = ('Calibri', 24, 'bold'), text = "Your order is ready to takeaway.")
        co1.pack()
        root.mainloop()
def g2():
        global root
        root.destroy()
        root = tk.Tk()
        root.title('Gazebo 2')
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        x1=0
        y1=0
        foodname1=tk.Label(root, text="Veg Cheese\nSandwich", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname1.place(x=x1, y=y1)
        foodpic1fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\vegcheesesandwich.png")
        foodpic1resize_image = foodpic1fetch.resize((100, 100))
        foodpic1resize_imagefetch = ImageTk.PhotoImage(foodpic1resize_image)
        foodpic1 = tk.Label(root, image=foodpic1resize_imagefetch)
        y1+=40
        foodpic1.place(x=x1, y= y1)
        foodprice1=tk.Label(root, text="Rs.40", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice1.place(x=x1,y=y1)
        foodbuy1=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf1)
        y1+=25
        foodbuy1.place(x=x1,y=y1)
        foodrem1=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf1)
        y1+=25
        foodrem1.place(x=x1, y=y1)
        global foodquantity1
        foodquantity1=tk.Label(root, text=str(food1), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity1.place(x=x1, y=y1)


        foodname2=tk.Label(root, text="Chicken Cheese\nSandwich", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname2.place(x=x1, y=y1)
        foodpic2fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\chickencheesesandwich.png")
        foodpic2resize_image = foodpic2fetch.resize((100, 100))
        foodpic2resize_imagefetch = ImageTk.PhotoImage(foodpic2resize_image)
        foodpic2 = tk.Label(root, image=foodpic2resize_imagefetch)
        y1+=40
        foodpic2.place(x=x1, y=y1)
        foodprice2=tk.Label(root, text="Rs.70", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice2.place(x=x1, y=y1)
        foodbuy2=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf2)
        y1+=25
        foodbuy2.place(x=x1, y=y1)
        foodrem2=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf2)
        y1+=25
        foodrem2.place(x=x1, y=y1)
        global foodquantity2
        foodquantity2=tk.Label(root, text=str(food2), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity2.place(x=x1, y=y1)


        foodname3=tk.Label(root, text="Chicken 65 Wrap", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname3.place(x=x1, y=y1)
        foodpic3fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\chicken65wrap.png")
        foodpic3resize_image = foodpic3fetch.resize((100, 100))
        foodpic3resize_imagefetch = ImageTk.PhotoImage(foodpic3resize_image)
        foodpic3 = tk.Label(root, image=foodpic3resize_imagefetch)
        y1+=35
        foodpic3.place(x=x1, y=y1)
        foodprice3=tk.Label(root, text="Rs.100", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice3.place(x=x1, y=y1)
        foodbuy3=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf3)
        y1+=25
        foodbuy3.place(x=x1, y=y1)
        foodrem3=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf3)
        y1+=25
        foodrem3.place(x=x1, y=y1)
        global foodquantity3
        foodquantity3=tk.Label(root, text=str(food3), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity3.place(x=x1, y=y1)

        x1=150
        y1=0
        foodname4=tk.Label(root, text="Paneer Wrap", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname4.place(x=x1, y=y1)
        foodpic4fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\paneerwrap.png")
        foodpic4resize_image = foodpic4fetch.resize((100, 100))
        foodpic4resize_imagefetch = ImageTk.PhotoImage(foodpic4resize_image)
        foodpic4 = tk.Label(root, image=foodpic4resize_imagefetch)
        y1+=35
        foodpic4.place(x=x1, y=y1)
        foodprice4=tk.Label(root, text="Rs.80", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice4.place(x=x1, y=y1)
        foodbuy4=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf4)
        y1+=25
        foodbuy4.place(x=x1, y=y1)
        foodrem4=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf4)
        y1+=25
        foodrem4.place(x=x1, y=y1)
        global foodquantity4
        foodquantity4=tk.Label(root, text=str(food4), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity4.place(x=x1, y=y1)


        foodname5=tk.Label(root, text="Samosa", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname5.place(x=x1, y=y1)
        foodpic5fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\samosa.png")
        foodpic5resize_image = foodpic5fetch.resize((100, 100))
        foodpic5resize_imagefetch = ImageTk.PhotoImage(foodpic5resize_image)
        foodpic5 = tk.Label(root, image=foodpic5resize_imagefetch)
        y1+=35
        foodpic5.place(x=x1, y=y1)
        foodprice5=tk.Label(root, text="Rs.20", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice5.place(x=x1, y=y1)
        foodbuy5=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf5)
        y1+=25
        foodbuy5.place(x=x1, y=y1)
        foodrem5=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf5)
        y1+=25
        foodrem5.place(x=x1, y=y1)
        global foodquantity5
        foodquantity5=tk.Label(root, text=str(food5), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity5.place(x=x1, y=y1)


        foodname6=tk.Label(root, text="Veg Momos", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=50
        foodname6.place(x=x1, y=y1)
        foodpic6fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\vegmomos.png")
        foodpic6resize_image = foodpic6fetch.resize((100, 100))
        foodpic6resize_imagefetch = ImageTk.PhotoImage(foodpic6resize_image)
        foodpic6 = tk.Label(root, image=foodpic6resize_imagefetch)
        y1+=35
        foodpic6.place(x=x1, y=y1)
        foodprice6=tk.Label(root, text="Rs.60", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice6.place(x=x1, y=y1)
        foodbuy6=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf6)
        y1+=25
        foodbuy6.place(x=x1, y=y1)
        foodrem6=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf6)
        y1+=25
        foodrem6.place(x=x1, y=y1)
        global foodquantity6
        foodquantity6=tk.Label(root, text=str(food6), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity6.place(x=x1, y=y1)

        x1=400
        y1=0
        foodname7=tk.Label(root, text="Chocolate Truffle", font=("Arial", 12, "bold"),bg="white",fg="Black")
        foodname7.place(x=x1, y=y1)
        foodpic7fetch = Image.open(r"C:\Users\Nishk\Documents\Python\Application\food\chocolatetruffle.png")
        foodpic7resize_image = foodpic7fetch.resize((100, 100))
        foodpic7resize_imagefetch = ImageTk.PhotoImage(foodpic7resize_image)
        foodpic7 = tk.Label(root, image=foodpic7resize_imagefetch)
        y1+=35
        foodpic7.place(x=x1, y=y1)
        foodprice7=tk.Label(root, text="Rs.50", font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=110
        foodprice7.place(x=x1, y=y1)
        foodbuy7=tk.Button(root, text="Buy", font=("Arial", 12, "bold"),bg="white",fg="Black", command=clf7)
        y1+=25
        foodbuy7.place(x=x1, y=y1)
        foodrem7=tk.Button(root, text="Remove", font=("Arial", 12, "bold"),bg="white",fg="Black", command=rlf7)
        y1+=25
        foodrem7.place(x=x1, y=y1)
        global foodquantity7
        foodquantity7=tk.Label(root, text=str(food7), font=("Arial", 12, "bold"),bg="white",fg="Black")
        y1+=35
        foodquantity7.place(x=x1, y=y1)
        Cart=tk.Button(root, text="Cart", font=("Arial", 12, "bold"),bg="white",fg="Black", command=cartla2)
        Cart.place(x=(width-100), y=0)
        #verscrollbar = AutoScrollbar(root)
        root.mainloop()
def cartla2():
        global root
        #print("Hello, Cart clicked")
        ql = [food1, food2, food3, food4, food5, food6, food7]
        qnl = ["Veg Cheese Sandwich", "Chicken Cheese Sandwich", "Chicken 65 Wrap", "Paneer Wrap", "Samosa", "Veg Momos", "Chocolate Truffle"]
        wtr = [3, 5, 13, 7]
        fp=[40, 70, 100, 80, 20, 60, 50]
        root.destroy()
        root = tk.Tk()
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.title('Billing window')
        titlelable=tk.Label(root, text="Billing window", font=("Arial", 32, "bold"),bg="white",fg="Black")
        titlelable.pack()
        j=0
        j1=0
        j2=0
        k=0
        col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = "Name --------------------- Price ----------- Waiting Time")
        col.pack()
        for i in ql:
            if i>0:
                    j1 = random.choice(wtr)
                    col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = qnl[k] + " --------------------- " + str(ql[k] * fp[k]) + " --------------------- " + str(j1))
                    col.pack()
                    j=j+(ql[k] * fp[k])
                    j2=j2+j1
            k+=1
        col=tk.Label(root, font = ('Calibri', 14, 'bold'), text = "Total --------------------- " + str(j) + " --------------------- " + str(j2))
        col.pack()
        paybtn=tk.Button(root, text="Pay", font=("Arial", 12, "bold"),bg="white",fg="Black", command=lambda:pay(j2))
        paybtn.pack()
        root.mainloop()

root = tk.Tk() 
root.title('Login Window')
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))
img = tk.PhotoImage(file=r'C:\Users\Nishk\Documents\Python\Application\logo.png')
root.iconphoto(False, img)

l1 = Label(root, text = "Login ID: ")
l1.config(font =("Courier", 14))
l1.pack()
entry1= Entry(root, width= 40)
entry1.focus_set()
entry1.pack()
l = Label(root, text = "Password: ")
l.config(font =("Courier", 14))
l.pack()
entry= Entry(root, width= 40, show='*')
entry.pack()
button1=tk.Button(root, text= "Login",width= 20, command= login)
button1.place(x=((width/2)-135), y=150)
button2=tk.Button(root, text= "Show Password",width=20, command= sp)
button2.place(x=((width/2)-135), y=100)
root.mainloop()