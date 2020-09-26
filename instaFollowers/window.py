from tkinter import *
import threading
from main import run
import main
import json
class MyWindow:
    def __init__(self, win):
        self.win = win
        self.lbl1=Label(win, text='Your Email')
        self.lbl2=Label(win, text='Your Password')
        self.lbl3=Label(win, text='Insert Hashtag')
        self.lbl4=Label(win, text='Error: Please fill empty fields')

        self.email = self.t1=Entry()
        self.password = self.t2=Entry()
        self.password.config(show="*")
        self.hashtag = self.t3=Entry()

        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        self.b1=Button(win, text='Quit', command=self.stop_program)
        self.b2=Button(win, text='Run', command= self.runprogram)
        self.b2.bind('<Button-1>')
        self.b1.place(x=100, y=200)
        self.b2.place(x=200, y=200)

    def runprogram(self):
            if((self.email.get() != "") & (self.password.get() != "") & (self.hashtag.get() != "")):
                self.newProcess = threading.Thread(target=run, args=(self.email.get(),self.password.get(),self.hashtag.get())).start()
            else:
                self.lbl4.place(x=200, y=250)

    def stop_program(self):
        self.win.destroy()
        exit_program()


#---------------
def exit_program():
    with open('run.json', 'w') as f:
        newdata = {"process": {"running": 0}}
        f.write(json.dumps(newdata, indent=2))
    f.close()

def start_program():
    with open('settings.json', 'w') as f:
        newdata = {"process": {"running": 1}}
        f.write(json.dumps(newdata, indent=2))
    f.close()

#---------------

window=Tk()
start_program()
mywin=MyWindow(window)
window.title('Instagram bot')
window.geometry("500x300+10+10")
window.mainloop()
#----My Changes
