import time,threading,tkinter,sqlite3,pygame,os,sys
from turtle import right
from tkinter import *

from pygame.draw import circle
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
    def __init__(self,voltage,voltageGain,x,y):
        self.voltage= voltage
        self.voltageGain=voltageGain
        self.rect= pygame.Rect(x,y,100,50)


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
    def __init__(self,x,y):
        self.displacement= 0
        self.nextNode= 1
        self.colour= (0,255,0)
        self.x= x
        self.y= y
        self.pos=(x,y)



class stopwatch():
   def __init__(self,StopwatchDisplay,minutes=0,seconds=0):
        self.minutes= minutes
        self.seconds= seconds
        self.StopwatchDisplay= StopwatchDisplay
                                        

    




#Simulation screens
def WaveSim():
    global screenSizeTk
    windowTkinter= Tk()
    windowTkinter.geometry=(screenSizeTk)
    windowTkinter.title("Wave Simulator")

    WaveGenerator= Frame(windowTkinter,width=540,height=360)
    #Since the Wave simulator is going to be similar to the Circuit Builder
    #the same technique can be used to make the window for the wave medium
    WaveGenerator.grid(row=6,column=1,columnspan=10)
    os.environ['SDL_WINDOWID'] = str(WaveGenerator.winfo_id()) 
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    waveMedium= pygame.display.set_mode((160,90))
    #Tkinter Buttons

    referenceLineButton= Button(windowTkinter,text="Reference Line",command= Iteration1Function,foreground="Black",).grid(row=2,column=0,sticky="w")
    rulerButton= Button(windowTkinter,text="Ruler",command= Iteration1Function,foreground="Black",).grid(row=3,column=0,sticky="w")
    normalButton=Button(windowTkinter, text="Normal",command=Iteration1Function,foreground="Black").grid(row=4,column=0,sticky="w")
    slowButton= Button(windowTkinter, text="Slow", command= Iteration1Function,foreground="Black").grid(row=5,column=0,sticky="w")
    resetButton=Button(windowTkinter, text="Reset Wave",command= Iteration1Function,foreground="Black").grid(row=6,column=0,sticky="w")

    amplidtudeButtonInc=Button(windowTkinter,text="Increase Amplitude",command= Iteration1Function,foreground="Black").grid(row=7,column=1,sticky="s")
    amplidtudeButtonDec= Button(windowTkinter,text="Decrease Amplitude",command= Iteration1Function,foreground="Black").grid(row=7,column=2,sticky="s")

    frequencyButtonInc=Button(windowTkinter,text="Increase Frequency",command= Iteration1Function,foreground="Black").grid(row=7,column=4,sticky="s")
    frequencyButtonDec= Button(windowTkinter,text="Decrease Frequency",command= Iteration1Function,foreground="Black").grid(row=7,column=5,sticky="s")

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=100)
    backButton= Button(windowTkinter,text="Back",background="light blue",command=windowTkinter.destroy,foreground="black").grid(row=0,column=0,sticky="w")

    waveNodeList=[waveNode(10,50),waveNode(10,10),waveNode(10,10),waveNode(10,10),waveNode(10,10),waveNode(10,10),waveNode(10,10),waveNode(10,10)]#This is the list of nodes that make up the wave medium
    nodeNumber=len(waveNodeList)

    
    def update_pygame():# this funtion will act as the main gameloop for pygame, using recursion instead of a while loop
       waveMedium.fill((0, 0, 0))  
       
       for nodes in range(0,nodeNumber):
           pygame.draw.circle(waveMedium,waveNodeList[nodes].colour,(waveNodeList[nodes].pos),10)# This loop iterates through the waveNodeList for all of the wave node objects and takes in each object's x and y attribbutes
                                                                                               

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
    componentList=[]#This List holds all of the compoents for the circuit builder
    componentNumber=len(componentList)#This number is the number of components in the list

    def componentCreation():
        componentList.append(battery(100,100,100,100))
        print("Batery has been added")
        componentNumber=len(componentList)
    
    #Tkinter Buttons
    clearButton= Button(windowTkinter,text="Clear",command=Iteration1Function,foreground="white",background="red").grid(row=9,column=0,sticky="w")
    batteryButton= Button(windowTkinter,text="Battery",command= componentCreation,foreground="black").grid(row=3,column=0,sticky="w")
    wireButton= Button(windowTkinter,text="Wire",command= Iteration1Function,foreground="black").grid(row=4,column=0,sticky="w")
    resistorButton= Button(windowTkinter,text="Resistor", command=Iteration1Function,foreground="black").grid(row=5,column=0,sticky="w")
    bulbButton= Button(windowTkinter,text="Bulb", command=Iteration1Function,foreground="black").grid(row=6,column=0,sticky="w")
    ammeterButton= Button(windowTkinter,text="Ammeter", command=Iteration1Function,foreground="black").grid(row=7,column=0,sticky="w")
    voltmeterButton=Button(windowTkinter,text="Voltmeter", command=Iteration1Function,foreground="black").grid(row=8,column=0,sticky="w")

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=5)
    backButton= Button(windowTkinter,text="Back",background="light blue",command=windowTkinter.destroy,foreground="black").grid(row=0,column=0,sticky="w")
    
            
    
    def update_pygame():# this funtion will act as the main gameloop for pygame, using recursion instead of a while loop
        buildingSpace.fill((0,0,0))  
        for compoent in range(0,componentNumber):# This loop iterates through the Components list and draws the them to the screen
            pygame.draw.rect(buildingSpace,(0,255,0),componentList[compoent].rect)

        
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

