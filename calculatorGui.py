from tkinter import *
root=Tk()
def process():
     num1=Entry.get(E1)
     num2=Entry.get(E2)
     operator=Entry.get(E3)
     if operator=="+":
          ans=(float(num1)+float(num2))
     if operator=="-":
          ans=(float(num1)-float(num2)) 
     if operator=="*":
          ans=(float(num1)*float(num2)) 
     if operator=="/":
          ans=(float(num1)/float(num2))
     if operator=="//":
          ans=(float(num1)//float(num2))
     Entry.insert(E4,0,ans)
     print(ans)
#root=Tk()
root.geometry("500x200")     
L1=Label(root,text="My Calculator").grid(row=0,column=1)
L2=Label(root,text="num1").grid(row=1,column=0)
L3=Label(root,text="num2").grid(row=2,column=0)
L4=Label(root,text="operator").grid(row=3,column=0)
L5=Label(root,text="ans").grid(row=4,column=0)
E1=Entry(root,bd=3)
E1.grid(row=1,column=1)
E2=Entry(root,bd=3)
E2.grid(row=2,column=1)
E3=Entry(root,bd=3)
E3.grid(row=3,column=1)
E4=Entry(root,bd=3)
E4.grid(row=4,column=1)
B=Button(root,bd=3,text="Submit",command=process).grid(row=5,column=1)
root.mainloop()
