from re import L
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
        S
    def display(self,windowSurface,x,y):
        image= pygame.draw.circle(windowSurface,(255,255,255),(x,y),10,0)

class compoentTemplate():
    def __init__(self):
        self.dragging= False
    
    def destroy(self):
        self.destroy

    def isDragging(self):
        if self.dragging:
            return True
        else:
            return False

    def drag(self):
        self.dragging = True

    def notDrag(self):
        self.dragging = False




class battery(compoentTemplate):
    def __init__(self,x,y,voltage,voltageGain):
        self.voltage= voltage
        self.voltageGain=voltageGain
        self.x= x
        self.y= y
        self.rect= pygame.Rect(x,y,100,50)
        super()

    def drawBattery(self,surface):
        pygame.draw.rect(surface,(0,255,0),self.rect)

    def updatePosition(self,mousePos):
        self.x,self.y= mousePos
    # mousePos in this method will be given from pygame and inserted into the method.


class resistor(compoentTemplate):
    def __init__(self,x,y):
        self.resistance = 10
        self.x= x
        self.y= y
        self.rect= pygame.Rect(self.x,self.y,100,50)
        super()

    def drawResistor(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)

class wire(compoentTemplate):
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.rect= pygame.Rect(self.x,self.y,50,100)
        
        super()

    def drawWire(self,surface):
        pygame.draw.rect(surface,(124,124,124),self.rect)

class bulb(compoentTemplate):
    def __init__(self,x,y):
        self.brightness= 0
        self.x=x
        self.y= y
        super()

    def drawBulb(self,surface):
        pygame.draw.circle(surface,(255,255,0),(self.x,self.y),5)


class voltmeter(compoentTemplate):
    def __init__ (self,x,y):
        self.x= x
        self.y= y
        self.rect= pygame.Rect(self.x,self.y,100,50)
        super()

    def drawVoltmeter(self,surface):
        pygame.draw.rect(surface,(0,0,255),self.rect)

class ammeter(compoentTemplate):
    def __init__ (self,x,y):
        self.x= x
        self.y= y
        self.rect= pygame.Rect(self.x,self.y,100,50)
        super()

    def drawAmmeter(self,surface):
        pygame.draw.rect(surface,(173,216,230),self.rect)
#_____________________________________________________________

class waveNode():
    def __init__(self,x,y):
        self.displacement= 0
        self.nextNode= 1
        self.colour= (0,255,0)
        self.x= x
        self.y= y
        self.pos=(x,y)

    def reset(self):
        self.y= 180


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

    waveNodeList=[ waveNode(25,180),waveNode(45,180),waveNode(65,180),waveNode(85,180),waveNode(105,180)
                  ,waveNode(125,180),waveNode(145,180),waveNode(165,180),waveNode(185,180),waveNode(205,180)
                  ,waveNode(225,180),waveNode(245,180),waveNode(265,180),waveNode(285,180),waveNode(305,180)
                  ,waveNode(325,180),waveNode(345,180),waveNode(365,180),waveNode(385,180),waveNode(405,180)
                  ,waveNode(425,180),waveNode(445,180),waveNode(465,180),waveNode(485,180),waveNode(505,180)]#This is the list of nodes that make up the wave medium


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


    # componentList=[]#This List holds all of the compoents for the circuit builder
    # componentNumber=len(componentList)#This number is the number of components in the list
    # def componentCreation():
    #     componentList.append(battery(10,10,10,10))
    #     componentNumber= len(componentList)

    BatteryList=[]
    BatteryNumber=len(BatteryList)
    def BatteryCreation():
        BatteryList.append(battery(10,10,10,10))
    ResistorList=[]
    ResistorNumber=len(ResistorList)
    def ResistorCreation():
        ResistorList.append(resistor(10,10))
    WireList=[]
    WireNumber=len(WireList)
    def WireCreation():
        WireList.append(wire(10,10))
    BulbList=[]
    BulbNumber=len(BulbList)
    def BulbCreation():
        BulbList.append(bulb(10,10))
    VoltmeterList=[]
    VoltmeterNumber=len(VoltmeterList)
    def VoltmeterCreation():
        VoltmeterList.append(voltmeter(10,10))

    AmmeterList=[]
    AmmeterNumber=len(AmmeterList)
    def AmmeterCreation():
        AmmeterList.append(ammeter(10,10))

    compList=[BatteryList,ResistorList,WireList,BulbList,VoltmeterList,AmmeterList]
    def clearScreen():
        for CompType in compList:
            for CompObject in CompType:
                CompObject.destroy
        buildingSpace.fill((0,0,0))
        return compList
        #In this procceedure I am storing the individual component Lists in 1 2d array 
        #that I can search through and pop the individual objects in each list. 


    def update_pygame():# this funtion will act as the main gameloop for pygame, using recursion instead of a while loop
        buildingSpace.fill((0,0,0))  
        for battery in BatteryList:# This loop iterates through the Battery list and draws the them to the screen
            battery.drawBattery(buildingSpace)

        for resistor in ResistorList:
            resistor.drawResistor(buildingSpace)

        for bulb in BulbList:
            bulb.drawBulb(buildingSpace)
            
        for wire in WireList:
            wire.drawWire(buildingSpace)
            
        for ammeter in AmmeterList:
            ammeter.drawAmmeter(buildingSpace)

        for voltmeter in VoltmeterList:
            voltmeter.drawVoltmeter(buildingSpace)


        for events in pygame.event.get():# I can use this for loop to get events as if this were a traditional pygame game loop
            if events == pygame.QUIT:
                pygame.quit
                sys.exit

            elif events == pygame.MOUSEBUTTONDOWN:
                if 


        pygame.display.update()
        # schedule the next update using recursion
        windowTkinter.after(100, update_pygame)
    
    #Tkinter Buttons
    clearButton= Button(windowTkinter,text="Clear",command=clearScreen,foreground="white",background="red").grid(row=9,column=0,sticky="w")
    batteryButton= Button(windowTkinter,text="Battery",command= BatteryCreation,foreground="black").grid(row=3,column=0,sticky="w")
    wireButton= Button(windowTkinter,text="Wire",command= WireCreation,foreground="black").grid(row=4,column=0,sticky="w")
    resistorButton= Button(windowTkinter,text="Resistor", command=ResistorCreation,foreground="black").grid(row=5,column=0,sticky="w")
    bulbButton= Button(windowTkinter,text="Bulb", command=BulbCreation,foreground="black").grid(row=6,column=0,sticky="w")
    ammeterButton= Button(windowTkinter,text="Ammeter", command=AmmeterCreation,foreground="black").grid(row=7,column=0,sticky="w")
    voltmeterButton=Button(windowTkinter,text="Voltmeter", command= VoltmeterCreation,foreground="black").grid(row=8,column=0,sticky="w")

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=5)
    backButton= Button(windowTkinter,text="Back",background="light blue",command=windowTkinter.destroy,foreground="black").grid(row=0,column=0,sticky="w")
    
            
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

# import pygame
# import tkinter as tk

# class Square:
#     def __init__(self, x, y, size, color):
#         self.x = x
#         self.y = y
#         self.size = size
#         self.color = color

#     def draw(self, surface):
#         pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen_width, self.screen_height = 800, 600
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         pygame.display.set_caption("Square Drawer")

#         self.root = tk.Tk()
#         self.root.title("Tkinter GUI")
#         self.root.geometry("400x100")  # Adjust the window size

#         self.squares = []

#     def draw_square(self, x, y):# Adds the square to the squares list
#         size = 50
#         color = (255, 0, 0)  # Red

#         new_square = Square(x, y, size, color)
#         self.squares.append(new_square)

#     def print_squares(self): # Prints the coordinates of the squares on the pygame screen
#         print("Array of squares:") 
#         for square in self.squares:
#             print(f"({square.x}, {square.y})")
#         print(self.squares)

#     def run(self):
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     if event.button == 1:  # Left mouse button
#                         x, y = event.pos
#                         self.draw_square(x, y) # Adds an instance of square to the squares list
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_SPACE:
#                         self.print_squares()

#             self.screen.fill((255, 255, 255))  # White background

#             for square in self.squares:# Draws the squares to the pygame screen
#                 square.draw(self.screen)

#             pygame.display.update()

#         pygame.quit()
#         self.root.mainloop()

# if __name__ == "__main__":
#     game = Game()
#     game.run()
