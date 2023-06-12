from tkinter import *
import pyttsx3
import time
import time as tm
import string
root=Tk()
root.geometry("400x600")
root.title("4KIDZ GIT ")
#This is the second file conflict
engine = pyttsx3.init()
engine.setProperty('rate',160)

#we are inside a conflict branch hopefully this works
#Frames
topFrame=Frame(root,bg="light blue")
topFrame.pack(side="top",fill="x")

thirdFrame=Frame(root,bg="yellow")
thirdFrame.pack(fill="x")

fourthFrame=Frame(root,bg="Red")
fourthFrame.pack(fill="x")

fifthFrame=Frame(root,bg="cyan")
fifthFrame.pack(fill="x")

sixthFrame=Frame(root,bg="dark orange")
sixthFrame.pack(fill="x")

seventhFrame=Frame(root,bg="forest green")
seventhFrame.pack(fill="x")

eightFrame=Frame(root,bg="violet red")
eightFrame.pack(fill="x")


#Lists of aplabets and examples
Letters=list(string.ascii_lowercase)#Results are A-Z
name=["Aeroplane","Bicycle","Car","Dam","Elevator","Fridge","Garage","House","Internet","Jelly","Kite"]
name+=["Land","Money","Nemo","Orange","Plant","Question","Resting","Swimming","Truck","Umbrella","Violin"]
name+=["Wind","Xenon","Yellow","Zebra"]

#List of animals
domesticAnimals=["Cat","Dog","Cow","Sheep","Goat","Pig"]
wildAnimals=["Lion","Tiger","Shark","Crocodile","Fox"]

#List of days of the week
daysOfTheWeek=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]


#functions
def talkingNumbers():
    engine.say("list of numbers until 10")
    for i in range(10):
        engine.say(str(i+1))
        engine.runAndWait()
        time.sleep(1)


def talkingLetters():
    engine.say("list of alphabets and examples")
    for i,j in zip(Letters,name):
        engine.say(i+" for "+j)
        engine.runAndWait()
        time.sleep(1)

def talkingDomAnimals():
    engine.say("list of Domestic animals")
    for i in domesticAnimals:
        engine.say(i)
        engine.runAndWait()
        time.sleep(1)
def talkingWildAnimals():
    engine.say("list of wild animals")
    for i in wildAnimals:
        engine.say(i)
        engine.runAndWait()
        time.sleep(1)

def talkingAddition():
    engine.say("list of numbers until 10 with their sums")
    for i in range(10):
        num=(i+1)+(i+1)
        engine.say(str(i+1)+"plus"+str(i+1)+"is "+str(num))
        engine.runAndWait()
        time.sleep(1)

def days():
    engine.say("Days of the week")
    for days in daysOfTheWeek:
        engine.say(days)
        engine.runAndWait()
        time.sleep(1)

def dispalytime():
        current = tm.strftime('%H:%M:%S:%p')
        labeltime["text"] = current
        topFrame.after(200, dispalytime)


#Labels and buttons
labeltime = Label(topFrame, bg="light blue", height=2, padx=20, fg="Black")
labeltime.pack(side="right")

labelWelcome=Label(topFrame,text="All You Can Learn 4 Kidz this is the copy by the way ",bg="light blue",fg="black",)
labelWelcome.pack(side="left")

buttonText=Button(thirdFrame,bd=0,text="Read out alphabets with name examples",command=talkingLetters,bg="Yellow",fg="Black",height=5)
buttonText.pack()

buttonNumbers=Button(sixthFrame,bd=0,bg="dark orange",fg="Black",text="Read out Numbers",command=talkingNumbers,height=5)
buttonNumbers.pack()

buttonDomAnimals=Button(fifthFrame,bd=0,bg="cyan",fg="Black",text="Read out Domestic Animals",command=talkingDomAnimals,height=5)
buttonDomAnimals.pack()

buttonWildAnimals=Button(fourthFrame,bd=0,bg="red",fg="Black",text="Read out Wild Animals",command=talkingWildAnimals,height=5)
buttonWildAnimals.pack()

buttonAddtion=Button(seventhFrame,bd=0,bg="Forest green",fg="black",height=5,text="Read out The Addition Of The First Ten Numbers",command=talkingAddition)
buttonAddtion.pack()

buttonDays=Button(eightFrame,bd=0,bg="violet red",fg="black",height=5,text="Read out Days Of The Week",command=days)
buttonDays.pack()

buttonQuiz=Button(root,bd=0,text="Take Quiz",font=2)
buttonQuiz.pack()

engine.say("Welcome to the all you can learn app for kids")
engine.runAndWait()


bottomFrame=Frame(root,bg="light blue")
bottomFrame.pack(side="bottom",fill="x")

Label(bottomFrame,text="Stay Safe And Santize",bg="light blue",fg="black",height=2).pack()
dispalytime()


root.mainloop()