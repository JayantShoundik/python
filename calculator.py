# creating a calculator
import tkinter as tkinter
from tkinter import messagebox
num1=int(input("enter the 1st number:"));
num2=int(input("enter the 2nd number:"));
print("press 1:+,2:-,3:*,4:/,5:\"float division\"//,6:** \"expoertial\"")
ch=int(input("press:"))
if(ch==1):
    {
        print("result=",num1+num2)
    }
elif(ch==2):
    {
        print("result=",num1-num2)
    }
elif(ch==3):
    {
        print("result=",num1*num2)
    }
elif(ch==4):
    {
        print("result=",num1/num2)
    }
elif(ch==5):
    {
        print("result=",num1//num2)
    }
elif(ch==6):
    {
        print("result=",num1**num2)
    }
root=tk.Tk()
root.title("calculator")
root.geometry("400*300")
label=tk.Label(root,text="Hello Tkinter!",font=("Arial",16))
label.pack()
entry=tk.Entery(root,widht=30)
entry.pack()
