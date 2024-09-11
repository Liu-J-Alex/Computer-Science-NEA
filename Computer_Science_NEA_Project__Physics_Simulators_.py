import time,threading,tkinter,sqlite3,pygame
from tkinter import *
pygame.init()

screenSizeTk="1920x1080"
screenSizePygame=(1920,1080)


# Circuit Builder Classes
class electron():
    def _init_(self,voltage,speed,direction,ElectronImage,window):
        self.voltage= voltage
        self.speed=speed
        self.direction= direction
        self.ElectronImage= pygame.draw.circle(window,(255,255,0),(1,1),4.0) # In a final solution, I would replace this with an actual asset rather than a yellow pygame circle

    def display(window):
        image= pygame.draw.circle(window,(255,255,0),(1,1),4)

class battery():
    pass

class resistor():
    pass

class wire():
    pass

class voltmeter():
    pass

class ammeter():
    pass
#_____________________________________________________________

class waveNode():
    def _init_(self,displacement,nextNode):
        self.displacement= displacement
        self.nextNode= nextNode





#Simulation screens
def WaveSim():
    pass

def CircuitBuilder():

    pass
    

def MainMenu():
    global CircuitBuilder,WaveSim,screenSizePygame,screenSizeTk
    windowPygame=pygame.display.set(screenSizePygame)

    windowTkinter= Tk()
    windowTkinter.geometry(screenSizeTk)
    windowTkinter.title("Main Menu")
    waveButton= Button(windowTkinter,text= "Wave Simulator",background="Light Blue",command=WaveSim,foreground="Black").grid(row=1,padx=10, column=0, pady=10)
    circuitButton=Button(windowTkinter,text="Circuit Builder",background="Light Blue", command=CircuitBuilder, foreground="Black").grid(row=1,padx=10,column=1,pady=10)
    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=5,padx=10)

    electron1=electron.display(window)
    
    window.mainloop()


MainMenu()


#These functions will hold all of my main screens, e.g the main menu and the wave simulator.
#Menu is going to be the last function in the program since it needs to run the other 2 functions that need to be defined before the menu.
