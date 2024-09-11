import time,threading,tkinter,sqlite3,pygame
from tkinter import *



def WaveSim():
    pass

def CircuitBuilder():
    


def MainMenu():
    global CircuitBuilder,WaveSim
    window= Tk()
    window.geometry("1920x1080")
    window.title("Main Menu")
    waveButton= Button(window,text= "Wave Simulator",background="Light Blue",command=WaveSim,foreground="Black").grid(row=1,padx=10, column=0, pady=10)
    circuitButton=Button(window,text="Circuit Builder",background="Light Blue", command=CircuitBuilder, foreground="Black").grid(row=1,padx=10,column=1,pady=10)
    quitButton=Button(window,text="X",background="red",command=quit,foreground="White").grid(row=0,column=5,padx=10)

    
    window.mainloop()


MainMenu()


#These functions will hold all of my main screens, e.g the main menu and the wave simulator.
#Menu is going to be the last function in the program since it needs to run the other 2 functions that need to be defined before the menu.