import pyautogui
import random
import time
from tkinter import*
def getSS():
 #time.sleep(3)
 ss = pyautogui.screenshot() 
 n = random.randint(0,1000000000000)
 path = str(n)+".png"
 print(path)
 #ss is a variable and screenshot is a fun that is used to for taking screenshot
 ss.save(path)


def take_ss(): 
 #add_data = entry.get() #stores address
 win.quit()
 getSS()
 

win = Tk() # win is a variable that is used to call the Tk class

win.title("Take screenshot")
win.geometry("1920x1080")
#Add a background color to the Main Window
win.config(bg = '#add123')

#Create a transparent window
win.wm_attributes('-transparentcolor','#add123')
win.resizable(False,FALSE) # to fix the geometry

#entry = Entry ( win,font=("Time New Roman" ,60))  #used to store the file in a given folder
#entry.place(x=20, height=70, width=660,y=50)

button = Button(win, text="Click", font=("Time New Roman" ,20),command=take_ss)  #button is a variable that is used to call the Button fun

button.place(x=900,y=1000,height=40,width=100)   #placement of button
 


win.mainloop() #it is a variable that is used to continuously run it