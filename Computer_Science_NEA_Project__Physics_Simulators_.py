import time,threading,tkinter,sqlite3,pygame,os,sys
from turtle import right
from tkinter import *
pygame.init()

screenSizeTk="1920x1080"

def Iteration1Function():
    #this function doesn't od anything
    #It is a place holder function since Tkinter 
    #doesn't allow pass as a command in buttons
    pass

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

class stopwatch()
    def _init_(self,minutes seconds,stopwatchImage):
        self.minutes= minutes
        self.seconds= seconds
        self.stopwatchImage= pygame.draw.square(window, (1,1))
                                        

    
    



#Simulation screens
def WaveSim():
    global screenSizeTk
    windowTkinter= Tk()
    windowTkinter.geometry=(screenSizeTk)
    windowTkinter.title("Wave Simulator")

    WaveGenerator= Frame(windowTkinter,width=160,height=90)
    #Since the Wave simulator is going to be similar to the Circuit Builder
    #the same technique can be used to make the window for the wave medium
    WaveGenerator.grid(row=2)
    os.environ['SDL_WINDOWID'] = str(WaveGenerator.winfo_id()) 
    os.environ['SDL_VIDEODRIVER'] = 'windib'



    windowTkinter.mainloop()
    

def CircuitBuilder():
    global screenSizeTk
    windowTkinter= Tk()
    windowTkinter.geometry=(screenSizeTk)
    windowTkinter.title("Circuit Builder")

    frame= Frame(windowTkinter,width=540,height=360)
    #This will be the building space for the circuit builder. 
    #It will make a Tkinter Frame widget where the pygame window will go
    frame.grid(row=9,column=3)
    os.environ['SDL_WINDOWID'] = str(frame.winfo_id())
    #this uses the OS module to set the pygame window inside of the Tkinter window
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    #pygame elements:
    buildingSpaceSize= (160,90)
    buildingSpace=pygame.display.set_mode(buildingSpaceSize)
    buildingSpace.fill((0,0,0))

    

    #Tkinter Buttons
    batteryButton= Button(windowTkinter,text="Battery",command= Iteration1Function ,foreground="black").grid(row=3,column=0,sticky="w")
    wireButton= Button(windowTkinter,text="Wire",command= Iteration1Function,foreground="black").grid(row=4,column=0,sticky="w")
    resistorButton= Button(windowTkinter,text="Resistor", command=Iteration1Function,foreground="black").grid(row=5,column=0,sticky="w")
    bulbButton= Button(windowTkinter,text="Bulb", command=Iteration1Function,foreground="black").grid(row=6,column=0,sticky="w")
    ammeterButton= Button(windowTkinter,text="Ammeter", command=Iteration1Function,foreground="black").grid(row=7,column=0,sticky="w")
    voltmeterButton=Button(windowTkinter,text="Voltmeter", command=Iteration1Function,foreground="black").grid(row=8,column=0,sticky="w")

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=5)
    backButton= Button(windowTkinter,text="Back",background="light blue",command=windowTkinter.destroy,foreground="black").grid(row=0,column=0,sticky="w")
    




    windowTkinter.mainloop()
    

def MainMenu():
    global CircuitBuilder,WaveSim,screenSizePygame,screenSizeTk
    
    windowTkinter= Tk()
    windowTkinter.geometry(screenSizeTk)
    windowTkinter.title("Main Menu")
    waveButton= Button(windowTkinter,text= "Wave Simulator",background="Light Blue",command=WaveSim,foreground="Black").place(x=100,y=100)
    circuitButton=Button(windowTkinter,text="Circuit Builder",background="Light Blue", command=CircuitBuilder, foreground="Black").place(x=120,y=100)
    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White",height=5,width=10,compound="c").place(x=1700,y=0)

    
    
    windowTkinter.mainloop()


MainMenu()


#These functions will hold all of my main screens, e.g the main menu and the wave simulator.
#Menu is going to be the last function in the program since it needs to run the other 2 functions that need to be defined before the menu.

