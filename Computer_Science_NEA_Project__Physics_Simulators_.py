from re import L
import time,threading,tkinter,sqlite3,pygame,os,sys,math 
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
        pygame.draw.rect(surface,(255,0,255),self.rect)
#_____________________________________________________________

class waveNode():
    #To control the frequency, experiment with 1 wave node and see if I can get it to oscillate up and down before I start making the whole sim
    def __init__(self,x):
        self.y= 180
        self.x=x 
        self.r= 10
        self.rect= pygame.Rect(self.x,self.y,self.r,self.r)
        self.direction= False
        self.amplitude =0
        self.frequency=0
        #self.direction will be used to manage how the wave node is moving, False corrosponds to moving up
        # True corrosponds to moving down.
        # This is to avoid the wave nodes from oscillating between their amplitude and their amplitudes-1. 
         

    def drawNode(self,surface):
        pygame.draw.circle(surface,(0,0,255),(self.x,self.y),self.r)

    def givepos(self,nextNode):
        pass


    def increaseAmp(self):
        self.amplitude+= 1

    def increaseFreq(self):
        self.frequency+= 1

    def decreaseAmp(self):
        self.amplitude-= 1

    def decreaseFreq(self): 
        self.frequency-=1 

    def oscillate(self,wt):
        wt= wt*self.frequency # when wt is passed in as a paramater it will be 2pi* the elapsed time.  
        displacement= self.amplitude*math.sin(wt) # I am using an equation from simple harmoinic motion to give the displacement of each wave node. 
        return displacement

    def updatePosition(self,y):
        self.y= y
        self.x= self.x
        self.rect.topleft = (self.x, self.y)  




rulerList=[]
class RulerX():
    def __init__(self):
        self.x=125
        self.y=200
        self.rect= pygame.Rect(self.x,self.y,500,30)
        self.colour= (255,255,0)
        self.dragging= False
    
    def drawRuler(self,surface):
        pygame.draw.rect(surface,self.colour,self.rect)
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
class RulerY(RulerX):
    def __init__(self):
        super().__init__()
        self.rect= pygame.Rect(self.x,self.y,30,480)
        self.colour= (255,0,255)
def rulerCreation():
    rulerList.append(RulerX())
    rulerList.append(RulerY())
def rulerDeletion():
    rulerList.clear()
def ToggleRulers():
    if len(rulerList)<2:
        rulerCreation()
    else:
        rulerDeletion()

class stopwatch():
    def __init__(self):
        self.minutes= 0
        self.seconds= 0
        self.StopwatchDisplay= pygame.Rect(50,50,50,50)
        self.startFlag = False
        self.startTime= 0

    def startCount(self):
       self.startFlag = True
       self.startTime= time.perf_counter()
    
    def stopCount(self):
        self.startFlag = False
internalStopwatch= stopwatch()

waveNodeList=[ waveNode(25),waveNode(45),waveNode(65),waveNode(85),waveNode(105)
                  ,waveNode(125),waveNode(145),waveNode(165),waveNode(185),waveNode(205)
                  ,waveNode(225),waveNode(245),waveNode(265),waveNode(285),waveNode(305)
                  ,waveNode(325),waveNode(345),waveNode(365),waveNode(385),waveNode(405)
                  ,waveNode(425),waveNode(445),waveNode(465),waveNode(485),waveNode(505)]#This is the list of nodes that make up the wave medium
# waveNodeList[0].frequency
def resetWave():
    for node in waveNodeList:
        node.y= 180
def increaseAmplitude():
    for node in waveNodeList:
        if node.amplitude == 100:
            pass
        else:
            node.amplitude += 1

def decreaseAmplitude():
    for node in waveNodeList:
        if node.amplitude==0:
            pass
        else:
            node.amplitude -= 1

def increaseFrequency():
    if waveNodeList[0].frequency == 5:
        pass
    elif waveNodeList[0].frequency == 0:
        internalStopwatch.startCount()
        waveNodeList[0].frequency += 1
        print(waveNodeList[0].frequency)
        
    else: 
        waveNodeList[0].frequency+=1
        print(waveNodeList[0].frequency)
    

def decreaseFrequency():
    if waveNodeList[0].frequency == 0:
        pass
    elif waveNodeList[0].frequency == 0:
        internalStopwatch.stopCount()
    else: 
        waveNodeList[0].frequency -= 1
        print(waveNodeList[0].frequency)



class referenceLine():
    def __init__(self):
        self.x=0 
        self.y= 177
        self.rect= pygame.Rect(self.x,self.y,510,6)

    def drawRefLine(self,surface):
        pygame.draw.rect(surface,(0,255,0),self.rect)
refline=[]
def createReferenceLine():
    refline.append(referenceLine())
def destroyReferenceLine():
    refline.clear()
def toggleReferenceLine():
    if len(refline) == 0:
        createReferenceLine()
    else:
        destroyReferenceLine()
    


                                        
#Simulation screens
def WaveSim():
    global screenSizeTk
    windowTkinter= Tk()
    windowTkinter.geometry=(screenSizeTk)
    windowTkinter.title("Wave Simulator")

    WaveGenerator= Frame(windowTkinter,width=540,height=360)
    #Since the Wave simulator is going to be similar to the Circuit Builder
    #the same technique can be used to make the window for the wave medium
    WaveGenerator.grid(row=10,column=1,columnspan=10)
    os.environ['SDL_WINDOWID'] = str(WaveGenerator.winfo_id()) 
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    screenSize= (160,90)
    waveMedium= pygame.display.set_mode(screenSize)

    stopwatch1= stopwatch()
    nodeNumber=len(waveNodeList)

    
    def update_pygame():# this funtion will act as the main gameloop for pygame, using recursion instead of a while loop
        waveMedium.fill((0,0,0))  
        for events in pygame.event.get():# I can use this for loop to get events as if this were a traditional pygame game loop
            if events == pygame.QUIT:
                pygame.quit
                sys.exit

            if events.type == pygame.MOUSEBUTTONUP: 
                # This code checks if the mouse button has been released for each compoent  
                for Ruler in rulerList:
                    #It is then checked if the components state is still dragging
                    if Ruler.isDragging():
                        Ruler.notDrag()

            elif events.type == pygame.MOUSEBUTTONDOWN:
                for Ruler in rulerList:
                        Area = Ruler.rect
                        if Area.collidepoint(pygame.mouse.get_pos()):
                            Ruler.drag()  #This statement is used to check if a component is being hovered over 
                                               #and then the dragging state of the component will be set to true, allowing for it to be dragged

        if pygame.mouse.get_pressed()[0]:  #Checks if the left mouse button is being pressed
            for Ruler in rulerList:
                if Ruler.isDragging(): #Checks if the component can be dragged
                    Ruler.x, Ruler.y = pygame.mouse.get_pos()
                    Ruler.updatePosition(Ruler.x, Ruler.y ) #Changes the position of the object
                    

        elapsedTime=0
        if waveNodeList[0].frequency>0:
            internalcurrentTime= time.perf_counter()
            internaltimeDiff= internalcurrentTime - internalStopwatch.startTime
            elapsedTime = round(internaltimeDiff,2)
            print(elapsedTime)


        for node in waveNodeList:
            wt= 2*math.pi*elapsedTime
            displacement= node.oscillate(wt) #I am using an equation from simple harmonic motion.
                                             # Because it can give the displacement of each node.
                                             # and accounts for when each node is at its amplitude aswell
                                             # When each node reach their amplitudes, they travel back as teh sin function will return negative
            dy= node.y + displacement
            node.updatePosition(dy)

            node.drawNode(waveMedium)



        if stopwatch1.startFlag == True:
            currentTime= time.perf_counter()
            timeDiff= currentTime - stopwatch1.startTime
            timeDiff = round(timeDiff,2)
            print(timeDiff)
        for line in refline:
            line.drawRefLine(waveMedium)
        for ruler in rulerList:
            ruler.drawRuler(waveMedium)

        

        pygame.display.update()
        # schedule the next update using recursion
        windowTkinter.after(100, update_pygame)
    #Tkinter Buttons

    referenceLineButton= Button(windowTkinter,text="Reference Line",command= toggleReferenceLine,foreground="Black",).grid(row=2,column=0,sticky="w")
    startStopwatchButton= Button(windowTkinter,text="Start Stopwatch",command= stopwatch1.startCount,foreground="Black",).grid(row=3,column=0,sticky="w")
    stopStopwatchButton= Button(windowTkinter,text="Stop Stopwatch",command= stopwatch1.stopCount,foreground="Black",).grid(row=4,column=0,sticky="w")
    rulerButton= Button(windowTkinter,text="Ruler",command= ToggleRulers,foreground="Black",).grid(row=5,column=0,sticky="w")
    normalButton=Button(windowTkinter, text="Normal",command=Iteration1Function,foreground="Black").grid(row=6,column=0,sticky="w")
    slowButton= Button(windowTkinter, text="Slow", command= Iteration1Function,foreground="Black").grid(row=7,column=0,sticky="w")
    resetButton=Button(windowTkinter, text="Reset Wave",command= resetWave,foreground="Black").grid(row=10,column=0,sticky="w")

    amplidtudeButtonInc=Button(windowTkinter,text="Increase Amplitude",command= increaseAmplitude,foreground="Black").grid(row=11,column=1,sticky="s")
    amplidtudeButtonDec= Button(windowTkinter,text="Decrease Amplitude",command= decreaseAmplitude,foreground="Black").grid(row=11,column=2,sticky="s")

    frequencyButtonInc=Button(windowTkinter,text="Increase Frequency",command= increaseFrequency,foreground="Black").grid(row=11,column=4,sticky="s")
    frequencyButtonDec= Button(windowTkinter,text="Decrease Frequency",command= decreaseFrequency,foreground="Black").grid(row=11,column=5,sticky="s")

    quitButton=Button(windowTkinter,text="X",background="red",command=quit,foreground="White").grid(row=0,column=100)
    backButton= Button(windowTkinter,text="Back",background="light blue",command=windowTkinter.destroy,foreground="black").grid(row=0,column=0,sticky="w")


    # Start the Pygame updating loop
    windowTkinter.after(100, update_pygame)
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
            CompType.clear()
            #.clear() clears each of the lists of their object instances

        buildingSpace.fill((0,0,0))
       



    def update_pygame():# this funtion will act as the main gameloop for pygame, using recursion instead of a while loop
        buildingSpace.fill((0,0,0))  



        for events in pygame.event.get():# I can use this for loop to get events as if this were a traditional pygame game loop
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if events.type == pygame.MOUSEBUTTONUP: 
                # This code checks if the mouse button has been released for each compoent  
                for compoentType in compList:
                    for component in compoentType:
                        #It is then checked if the components state is still dragging
                        if component.isDragging():
                            component.notDrag()

            elif events.type == pygame.MOUSEBUTTONDOWN:
                for compoentType in compList:
                    for component in compoentType:
                        Area = component.rect
                        if Area.collidepoint(pygame.mouse.get_pos()):
                            component.drag()  #This statement is used to check if a component is being hovered over 
                                               #and then the dragging state of the component will be set to true, allowing for it to be dragged

        if pygame.mouse.get_pressed()[0]:  #Checks if the left mouse button is being pressed
            for compoentType in compList:
                for component in compoentType:
                    if component.isDragging(): #Checks if the component can be dragged
                        component.x, component.y = pygame.mouse.get_pos()
                        component.updatePosition(component.x, component.y) #Changes the position of the object
                        





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
