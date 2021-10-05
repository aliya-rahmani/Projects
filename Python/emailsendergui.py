import smtplib
import tkinter as tk
# from tkinter import ttk

#before this you must turn on less secure apps on your email on google

class Emailsender():
    def __init__(self,root):
        self.root=root
        self.root.title('Email Sender')
        self.root.geometry('1350x700+0+0')

        self.GMAIL_ID = 'Enter your email'
        self.GMAIL_PSWD = 'enter your password' 
        self.subvar=tk.StringVar()
        self.tovar=tk.StringVar()

        title= tk.Label(self.root, text='Email Sending Program',bd=5,relief='groove',font=('centaur', 40,'bold'),bg='steel blue',fg='white')
        title.pack(side='top',fill='x')


        manage_Frame = tk.Frame(self.root,bd=4,relief='ridge',bg='steel blue')
        manage_Frame.pack(fill='both',expand='yes')

        tolbl=tk.Label(manage_Frame,text='Please enter receiver\'s Email-Id : ',font=('centaur', 30,'bold'),bg='steel blue',fg='white')
        tolbl.grid(row=0,column=0)

        to=tk.Entry(manage_Frame,textvariable=self.tovar,width=40,font=('centaur', 20,'bold'))
        to.grid(row=0,column=1)

        subjectlbl = tk.Label(manage_Frame,text='Please Enter your subject : ',font=('centaur', 30,'bold'),bg='steel blue',fg='white')
        subjectlbl.grid(row=1,column=0)

        subject=tk.Entry(manage_Frame,textvariable=self.subvar,width=40,font=('centaur', 20,'bold'))
        subject.grid(row=1,column=1)

        msglbl=tk.Label(manage_Frame,text='Please Enter your message : ',font=('centaur', 30,'bold'),bg='steel blue',fg='white')
        msglbl.grid(row=2,column=0)

        self.msg=tk.Text(manage_Frame,font=('centaur', 12,'bold'))
        self.msg.grid(row=2,column=1)

        mailbtn=tk.Button(manage_Frame,text='Send Email',command=self.combo,width=10,height=3).grid(row=3,column=1)
        mailbtn=tk.Button(manage_Frame,text='Clear',command=self.clear,width=10,height=3).grid(row=3,column=0)


    def sendEmail(self,to,sub,msg):
        try:
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(self.GMAIL_ID,self.GMAIL_PSWD)
            s.sendmail(self.GMAIL_ID,to,f'Subject: {sub}\n\n{msg}')
            s.close()
        except:
            win=tk.Toplevel(self.root)
            win.geometry('300x50+0+0')
            lbl=tk.Label(win,text='Something went wrong !! \n please check all credentials !!').pack()
        else:
            self.subvar.set('')
            self.msg.delete('1.0','end')
            self.tovar.set('')
            win1=tk.Toplevel(self.root)
            win1.geometry('300x50+0+0')
            lbl=tk.Label(win1,text='Email sent successfully !!').pack()
    def clear(self):
        self.subvar.set('')
        self.msg.delete('1.0','end')
        self.tovar.set('')
    def combo(self):
        self.sendEmail(self.tovar.get(),self.subvar.get(),self.msg.get('1.0','end'))



root=tk.Tk()
ob=Emailsender(root)
root.mainloop()
