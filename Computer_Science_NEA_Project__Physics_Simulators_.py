import time,threading,tkinter,sqlite3,pygame,os,sys
from turtle import right
from tkinter import *

import pygame.rect
pygame.init()

screenSizeTk="1920x1080"
TESTCOLOUR=(128,128,128)

def Iteration1Function():
    #this function doesn't od anything
    #It is a place holder function since Tkinter 
    #doesn't allow pass as a command in buttons
    pass

# Circuit Builder Classes
class electron():
    def _init_(self,voltage,speed,direction):
        self.voltage= voltage
        self.speed=speed
        self.direction= direction
        
    def display(self,windowSurface,x,y):
        image= pygame.draw.circle(windowSurface,(255,255,255),(x,y),10,0)

class battery():
    def __init__(self,voltage,voltageGain):
        self.voltage= voltage
        self.voltageGain=voltageGain

    def display(self,window,xPos,yPos):
        image=pygame.draw.rect(window,(128,0,128),pygame.Rect(xPos,yPos,10,5))


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

class stopwatch():
   def _init__(self,StopwatchDisplay,minutes=0,seconds=0):
        self.minutes= minutes
        self.seconds= seconds
        self.StopwatchDisplay= StopwatchDisplay
                                        

    
def batteryCreation(window):
    component= battery(10,10)
    component.display(window,10,10)
    pygame.display.update()



#Simulation screens
def WaveSim():
    global screenSizeTk
    windowTkinter= Tk()
    windowTkinter.geometry=(screenSizeTk)
    windowTkinter.title("Wave Simulator")

    WaveGenerator= Frame(windowTkinter,width=540,height=360)
    #Since the Wave simulator is going to be similar to the Circuit Builder
    #the same technique can be used to make the window for the wave medium
    WaveGenerator.grid(row=6,column=3)
    os.environ['SDL_WINDOWID'] = str(WaveGenerator.winfo_id()) 
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    waveMedium= pygame.display.set_mode((160,90))
    #Tkinter Buttons

    referenceLineButton= Button(windowTkinter,text="Reference Line",command= Iteration1Function,foreground="Black",).grid(row=2,column=0,sticky="w")
    rulerButton= Button(windowTkinter,text="Ruler",command= Iteration1Function,foreground="Black",).grid(row=3,column=0,sticky="w")
    normalButton=Button(windowTkinter, text="Normal",command=Iteration1Function,foreground="Black").grid(row=4,column=0,sticky="w")
    slowButton= Button(windowTkinter, text="Slow", command= Iteration1Function,foreground="Black").grid(row=5,column=0,sticky="w")
    resetButton=Button(windowTkinter, text="Reset Wave",command= Iteration1Function,foreground="Black").grid(row=6,column=0,sticky="w")

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=5)
    backButton= Button(windowTkinter,text="Back",background="light blue",command=windowTkinter.destroy,foreground="black").grid(row=0,column=0,sticky="w")

    pygame.display.update()
    def update_pygame():# this funtion will act as the main gameloop for pygame, using recursion instead of a while loop
       waveMedium.fill((0, 0, 0))  
       square = pygame.draw.rect(waveMedium, TESTCOLOUR, pygame.Rect(100, 100, 100, 100),0)


       pygame.display.update()
       # schedule the next update using recursion
       windowTkinter.after(16, update_pygame)

    # Start the Pygame updating loop
    windowTkinter.after(16, update_pygame)

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

    

    #Tkinter Buttons
    clearButton= Button(windowTkinter,text="Clear",command=Iteration1Function,foreground="white",background="red").grid(row=9,column=0,sticky="w")
    batteryButton= Button(windowTkinter,text="Battery",command= batteryCreation(buildingSpace),foreground="black").grid(row=3,column=0,sticky="w")
    wireButton= Button(windowTkinter,text="Wire",command= Iteration1Function,foreground="black").grid(row=4,column=0,sticky="w")
    resistorButton= Button(windowTkinter,text="Resistor", command=Iteration1Function,foreground="black").grid(row=5,column=0,sticky="w")
    bulbButton= Button(windowTkinter,text="Bulb", command=Iteration1Function,foreground="black").grid(row=6,column=0,sticky="w")
    ammeterButton= Button(windowTkinter,text="Ammeter", command=Iteration1Function,foreground="black").grid(row=7,column=0,sticky="w")
    voltmeterButton=Button(windowTkinter,text="Voltmeter", command=Iteration1Function,foreground="black").grid(row=8,column=0,sticky="w")

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=5)
    backButton= Button(windowTkinter,text="Back",background="light blue",command=windowTkinter.destroy,foreground="black").grid(row=0,column=0,sticky="w")
    
    pygame.display.update()
    def update_pygame():# this funtion will act as the main gameloop for pygame, using recursion instead of a while loop
        buildingSpace.fill((0,0,0))  
        


        for events in pygame.event.get():# I can use this for loop to get events as if this were a traditional pygame game loop
            if events == pygame.QUIT:
                pygame.quit
                sys.exit


        pygame.display.update()
        # schedule the next update using recursion
        windowTkinter.after(100, update_pygame)

    # Start the Pygame updating loop
    windowTkinter.after(100, update_pygame)

    windowTkinter.mainloop()
    
    

def MainMenu():
    global CircuitBuilder,WaveSim,screenSizePygame,screenSizeTk
    
    windowTkinter= Tk()
    windowTkinter.geometry(screenSizeTk)
    windowTkinter.title("Main Menu")


    waveButton= Button(windowTkinter,text= "Wave Simulator",background="Light Blue",command=WaveSim,foreground="Black").grid(row=2,column=3)
    circuitButton=Button(windowTkinter,text="Circuit Builder",background="Light Blue", command=CircuitBuilder, foreground="Black").grid(row=2,column=2)

    waveLabel= Label(windowTkinter,text="This is a wave simulation").grid(row=3,column=3)
    circuitLabel= Label(windowTkinter,text="This is a Circuit Builder").grid(row=3,column=2)

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White",).grid(row=0,column=5)

    
    
    windowTkinter.mainloop()


MainMenu()


#These functions will hold all of my main screens, e.g the main menu and the wave simulator.
#Menu is going to be the last function in the program since it needs to run the other 2 functions that need to be defined before the menu.

