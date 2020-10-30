import tkinter as tink
count = -1
run = False
def var_name(mark):
   def value():
      if run:
         global count
         # Just beore starting
         if count == -1:
            show = "Starting"
         else:
            show = str(count)
         mark['text'] = show
         #Increment the count after
         #every 1 second
         mark.after(1000, value)
         count += 1
   value()
# While Running
def Start(mark):
   global run
   run = True
   var_name(mark)
   start['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'
# While stopped
def Stop():
   global run
   start['state'] = 'normal'
   stop['state'] = 'disabled'
   reset['state'] = 'normal'
   run = False
# For Reset
def Reset(label):
   global count
   count = -1
   if run == False:
      reset['state'] = 'disabled'
      mark['text'] = 'Welcome'
   else:
      mark['text'] = 'Start'

base = tink.Tk()
base.title("PYTHON STOPWATCH")
base.minsize(width=300, height=200)
mark = tink.Label(base, text="Welcome", fg="blue", font="Times 25 bold",bg="white")
mark.pack()
start = tink.Button(base, text='Start',width=25, command=lambda: Start(mark))
stop = tink.Button(base, text='Stop', width=25, state='disabled', command=Stop)
reset = tink.Button(base, text='Reset',width=25, state='disabled', command=lambda: Reset(mark))
start.pack()
stop.pack()
reset.pack()
base.mainloop()
