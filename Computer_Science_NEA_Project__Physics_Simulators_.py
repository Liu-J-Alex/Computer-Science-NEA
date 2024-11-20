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
        
    def display(self,windowSurface,x,y):
        image= pygame.draw.circle(windowSurface,(255,255,255),(x,y),10,0)

class compoentTemplate():
    def __init__(self):
        self.dragging = False
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 0, 0)  

    def destroy(self):
        self.destroy

    def isDragging(self):
        return self.dragging

    def drag(self):
        self.dragging = True

    def notDrag(self):
        self.dragging = False

    def updatePosition(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)  # Update rect position


class battery(compoentTemplate):
    def __init__(self,x,y,voltage,voltageGain):
        super().__init__()
        self.voltage= voltage
        self.voltageGain=voltageGain
        self.x=x
        self.y= y
        self.rect= pygame.Rect(self.x,self.y,100,50)
        

    def drawBattery(self,surface):
        pygame.draw.rect(surface,(0,255,0),self.rect)



class resistor(compoentTemplate):
    def __init__(self,x,y):
        super().__init__()
        self.resistance = 10
        self.x=x
        self.y= y
        self.rect= pygame.Rect(self.x,self.y,100,50)
        
    def drawResistor(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)

class wire(compoentTemplate):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y= y
        self.rect= pygame.Rect(self.x,self.y,50,100)
       

    def drawWire(self,surface):
        pygame.draw.rect(surface,(124,124,124),self.rect)

class bulb(compoentTemplate):
    def __init__(self,x,y):
        super().__init__()
        self.brightness= 0
        self.x=x
        self.y= y
        self.r=20
        self.rect= pygame.Rect(self.x,self.y,self.r,self.r)
        

    def drawBulb(self,surface):
        pygame.draw.circle(surface,(255,255,0),(self.x,self.y),self.r)


class voltmeter(compoentTemplate):
    def __init__ (self,x,y):
        super().__init__()
        self.x=x
        self.y= y
        self.rect= pygame.Rect(x,y,100,50)
       

    def drawVoltmeter(self,surface):
        pygame.draw.rect(surface,(0,0,255),self.rect)

class ammeter(compoentTemplate):
    def __init__ (self,x,y):
        super().__init__()
        self.x=x
        self.y= y
        self.rect= pygame.Rect(x,y,100,50)
        

    def drawAmmeter(self,surface):
        pygame.draw.rect(surface,(173,216,230),self.rect)
#_____________________________________________________________

class waveNode():
    #To control the frequency, experiment with 1 wave node and see if I can get it to oscillate up and down before I start making the whole sim
    def __init__(self,x):
        self.y= 180
        self.x=x 
        self.r= 20
        self.rect= pygame.Rect(self.x,self.y,self.r,self.r)

    def drawNode(self,surface):
        pygame.draw.circle(surface,(0,0,255),(self.x,self.y),self.r)

    def givepos(self,nextNode):
        pass

class primaryWaveNode(waveNode):
    def __init__(self,amplitude,frequency):
        super.__init__()
        self.amplitude = amplitude
        self.frequency= frequency 
waveNodeList=[ waveNode(25),waveNode(45),waveNode(65),waveNode(85),waveNode(105)
                  ,waveNode(125),waveNode(145),waveNode(165),waveNode(185),waveNode(205)
                  ,waveNode(225),waveNode(245),waveNode(265),waveNode(285),waveNode(305)
                  ,waveNode(325),waveNode(345),waveNode(365),waveNode(385),waveNode(405)
                  ,waveNode(425),waveNode(445),waveNode(465),waveNode(485),waveNode(505)]#This is the list of nodes that make up the wave medium
def resetAmp():
    for node in waveNodeList:
        node.y= 180

   


class referenceLine():
    def __init__(self):
        self.x=0 
        self.y= 180
        self.rect= pygame.Rect(self.x,self.y,160,10)

    def drawRefLine(self,surface):
        pygame.draw.rect(surface,(0,255,0),self.rect)

    def destroy(self):
        self.destroy

refline=[]
def createReferenceLine():
    refline.append(referenceLine)

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

    referenceLineButton= Button(windowTkinter,text="Reference Line",command= createReferenceLine,foreground="Black",).grid(row=2,column=0,sticky="w")
    rulerButton= Button(windowTkinter,text="Ruler",command= Iteration1Function,foreground="Black",).grid(row=3,column=0,sticky="w")
    normalButton=Button(windowTkinter, text="Normal",command=Iteration1Function,foreground="Black").grid(row=4,column=0,sticky="w")
    slowButton= Button(windowTkinter, text="Slow", command= Iteration1Function,foreground="Black").grid(row=5,column=0,sticky="w")
    resetButton=Button(windowTkinter, text="Reset Wave",command= resetAmp,foreground="Black").grid(row=6,column=0,sticky="w")

    amplidtudeButtonInc=Button(windowTkinter,text="Increase Amplitude",command= Iteration1Function,foreground="Black").grid(row=7,column=1,sticky="s")
    amplidtudeButtonDec= Button(windowTkinter,text="Decrease Amplitude",command= Iteration1Function,foreground="Black").grid(row=7,column=2,sticky="s")

    frequencyButtonInc=Button(windowTkinter,text="Increase Frequency",command= Iteration1Function,foreground="Black").grid(row=7,column=4,sticky="s")
    frequencyButtonDec= Button(windowTkinter,text="Decrease Frequency",command= Iteration1Function,foreground="Black").grid(row=7,column=5,sticky="s")

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=100)
    backButton= Button(windowTkinter,text="Back",background="light blue",command=windowTkinter.destroy,foreground="black").grid(row=0,column=0,sticky="w")


    nodeNumber=len(waveNodeList)

    
    def update_pygame():# this funtion will act as the main gameloop for pygame, using recursion instead of a while loop
       waveMedium.fill((0, 0, 0))  
       
       for nodes in range(0,nodeNumber):
           nodes.drawNode# This loop iterates through the waveNodeList for all of the wave node objects and takes in each object's x and y attribbutes


                                                                              

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




        for events in pygame.event.get():# I can use this for loop to get events as if this were a traditional pygame game loop
            if events == pygame.QUIT:
                pygame.quit
                sys.exit


            if events.type == pygame.MOUSEBUTTONDOWN:
                for compoentType in compList: 
                    for component in compoentType:
                        Area= component.rect
                        if Area.collidepoint(pygame.mouse.get_pos()) and pygame.MOUSEBUTTONDOWN:
                            #This statement is used to check if a component is being hovered over 
                            #and if the mousebutton is being left clicked at the same time

                            component.drag()  #this statment uses the drag method from my comonent template method, which sets the dragging state to be true      
                            print("Dragging")

                        if component.isDragging(): 
                            component.x,component.y= pygame.mouse.get_pos()
                            component.updatePosition(component.x,component.y)
                            #This bit of code moves the position of the square to the position of the cursor

                        if component.isDragging and pygame.MOUSEBUTTONUP:
                            component.notDrag()
                            print("Hovering")


                # for compoentType in compList: 
                #     for component in compoentType:
                #         Area= component.rect
               
                #         if component.isDragging and pygame.MOUSEBUTTONUP:
                #             component.notDrag()
                #             print("Hovering")




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
