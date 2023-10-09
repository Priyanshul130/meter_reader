from tkinter import *
from tkinter.ttk import *
import smtplib
# create tkinter window 
window= Tk()
#add title
window.title("METER READING")
#add dimensions 
window.geometry("900x300")

#heading 
heading1 = Label(window, text = "meter reader",font="bold, 30 ")
heading1.grid(row=0,column=1,padx=20,pady=20)

res0=Label(window,text= "result-",font="bold,15")
res1=Label(window)


#label and entry box 
label1= Label(window, text = "Enter this Month Reading(KWH):",font="bold, 15")
label1.grid(row=1,column=0,padx=10)
entry1 = Entry(window, width = 50) 
entry1.grid(row=1,column=1,pady = 20,padx=20)

#label and entry box 
label2= Label(window, text = "Enter last Month Reading(KWH):",font="bold, 15")
label2.grid(row=2,column=0,padx=10)
entry2 = Entry(window, width = 50) 
entry2.grid(row=2,column=1,pady = 20,padx=20)

text_ans=Entry(window)

res0.grid(row=4,column=1)
res1.grid(row=4,column=2)
#text_ans.grid(row=4,column=2)

#add function here
def reader():
    num1=float(entry1.get())
    num2=float(entry2.get())
    ans=num1-num2
    
    res1.configure(text=ans*7,font="bold,15,")
    ans1=''
    ans1.set(res1)    

def send():
    result1=float(entry1.get())
    result2=float(entry2.get())
    answer=result1-result2
    ans1=answer*7
    
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    send_email=input("enter email to send messages - ")
    server.login("YOUR E-mail ID","PASSWORD")
    server.sendmail("YOUR E-MAIL",send_email,ans)

  
#button
value=Button(window,text="FIND",command=reader)
send_message=Button(window,text="SEND MESSAGE",command=send)


#place the button

value.grid(row=2,column=4,padx=50)
send_message.grid(row=3,column=4,padx=50)




window.mainloop()
server.quit()
    
