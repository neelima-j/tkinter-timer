from tkinter.ttk import *
from tkinter import *

import os
import time

exercise = {
    'Exercise One':3,    #'Name of Exercise':number of sets
    'Exercise Two':3,    #Exercises with 3 sets have a duration of 30 seconds each
    'Exercise Three':10, #Exercises with 10 sets have duration of 10 seconds each
    'Exercise Four':10,
    'Exercise Five':10
    }

exercise_checkbox = exercise.copy()


def say(word):
    '''
    Takes a string, says it, displays it
    '''
    word = 'say '+word
    os.system(word)
    time.sleep(4)

def announce(reps):
    '''
    announces all the starts and stops for each rep of the exercise
    takes argument of an int reps = 10 or 30 determining number of repeats 
    '''
    for i in reversed(range(0,reps)):
        reps_left.delete(1.0,END)
        reps_left.insert(END,'Seconds, Rep '+str(reps-i)+'/'+str(reps))
        if reps == 3:
            os.system('say go!')
            countdown(30)     #30 seconds for exercises with 3
            progress['value'] += 3.33
        else:
            os.system('say go!')
            countdown(10)     #10 seconds for exercises with 10 reps
            progress['value'] += 1
        os.system('say down')
        root.update()
        if i != 0:
            say(str(i)+' more')
            

def pause():
    '''
    pauses the program for 30 seconds
    displays countdown to resumption
    '''
    countdown_text["fg"]='silver'
    
    for i in reversed(range(31)):
        pause_text.insert(END, 'Resuming in '+str(i))
        frame3.update()
        time.sleep(1)
        pause_text.delete(1.0,END)
#    pause_text.after(0, pause_text.destroy)
    say('Resuming')
    countdown_text["fg"]='green'

    
       


def physio():
    '''
    Deactivates the start button
    Loops through every exercise
    '''
    start["state"] = DISABLED
    for task in exercise:
        say(task)        
        root.update()
        os.system('say Left Leg')
        announce(int(exercise[task]))
        time.sleep(3)
        os.system('say Right leg')
        announce(int(exercise[task]))
        exercise_checkbox[task].toggle()
        root.update()
        
    pause["state"] = DISABLED
    
    say('Physiotherapy Over!')
    '''
    with open('physio.py',"r") as r:
        exec(r.read())
    '''

def countdown(t):
    '''
    a timer showing seconds elapsed
    takes an int in seconds as argument
    '''
    for i in range(1,t+1):
        countdown_text.insert(END, i)
        frame3.update()
        time.sleep(1)
        countdown_text.delete(1.0,END)

        

root = Tk()
root.title('Physio Timer')
root.config(highlightbackground='black',highlightthickness='2')

#root.geometry('600x600')

frame1 = Frame(root,pady=20)
frame2 = LabelFrame(root,text='Progress',padx=10,bd=2,relief=SUNKEN)
frame3 = Frame(root)
frame4 = LabelFrame(root,text='Exercises',padx=15)
frame1.grid(row=0,column=0,columnspan=2)
frame2.grid(row=1,column=0,columnspan=2)
frame3.grid(row=2,column=1)
frame4.grid(row=2,column=0)

#Frame1 : Start, Pause, Exit Buttons
start = Button(frame1, text = 'START', fg = 'green', font = ("Helvetica", 30),
               command = physio)
pause = Button(frame1,text = "PAUSE 30 seconds", fg = 'orange', font = ("Helvetica", 30),
                command = pause)
end = Button(frame1,text = "EXIT", fg = 'red', font = ("Helvetica", 30),
             command = lambda:(root.destroy(),root.quit()))
start.pack(side=LEFT,ipadx=10,pady=5)
pause.pack(side=LEFT,ipadx=10)
end.pack(side=LEFT)



#Frame2 : Progress Bar
s = Style()
s.theme_use("default")
s.configure("TProgressbar", thickness=50, background='#e1f7fa')
progress = Progressbar(frame2, orient = HORIZONTAL, length = 500, mode='determinate',
                       style="TProgressbar")
progress.pack(pady=30)



#Frame 3: Textboxes that show seconds left in exercise, pause info
countdown_text = Text(frame3,width='2',height='1',fg='green',font=("Helvetica",49))
countdown_text.grid(row=0,column=0)

pause_text = Text(frame3,width='20',height='1',fg='orange',font=("Helvetica", 49))
pause_text.grid(row=1,column=0,columnspan=2,padx=(100,0))

reps_left = Text(frame3,width='18',height='1',fg='silver',font=("Helvetica", 39))
reps_left.grid(row=0,column=1)


#Frame4: Generating Checkboxes as per exercises
for task in exercise:
    var = IntVar(value=0)
    l = Checkbutton(frame4, text=task, variable = var, font=("Helvetica", 24))
    l.pack(anchor = 'w')
    exercise_checkbox[task] = l

root.mainloop()

