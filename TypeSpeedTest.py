
from tkinter import *
import time
import threading


class TypeSpeedTest:
    def __init__(self):
        ##################################################### ROOT METHOD
        self.root = Tk()
        self.root.title("Speed Typing Test")
        self.root.geometry("1000x600")
        self.root.configure(bg="#8ec5d1")
        self.root.resizable(False,False)

        ##################################################### FRAME METHOD
        self.frame1 = Frame(self.root,width=650,height=300, bg="#8ec5d1")
        self.frame1.place(x=0,y=0)
        self.frame2 = Frame(self.root,width=650,height=300,bg="#95dde6")
        self.frame2.place(x=0,y=300)        
        self.frame3 = Frame(self.root,width=350,height=600, bg="#8eb8d1")
        self.frame3.place(x=650,y=0)

        ##################################################### PANE ONE
        self.testLabel = Label(self.root, text="Speed Typing Test", font=("arial",24,"bold italic"), bg="#8ec5d1")
        self.testLabel.place(x=20,y=20)
        
        self.sampleText = Label(self.root, text="Sample Text:", font=("arial",20), bg="#8ec5d1")
        self.sampleText.place(x=40,y=100)

        self.sampleLabel = Label(self.root, text="Good code is simple code.", font=("arial",20,"bold"),bg="white")
        self.sampleLabel.place(x=50,y=150)

        ##################################################### PANE TWO
        self.entryLabel = Label(self.root,text="Entry Field:",font=("arial", 20), bg="#95dde6")
        self.entryLabel.place(x=40,y=330)

        self.inputEntry = Entry(self.root,font=("arial", 20),bd=5, width=23)
        self.inputEntry.place(x=50,y=380)
        self.inputEntry.bind("<KeyPress>", self.startGame)
        self.inputEntry.focus_set()
      
        ##################################################### PANE THREE
        self.instrucLabel = Label(self.root, text="Start typing the sample\n text to begin test.",  font=("arial",18), bg="#8eb8d1")
        self.instrucLabel.place(x=685, y=20)

        self.timeLabel = Label(self.root, text="Time:", font=("arial",18,"bold"), bg="#8eb8d1")
        self.timeLabel.place(x=670,y=100)

        self.timeLabelCount = Label(self.root, text= "00:0" + str(secCount), font=("arial", 18,), bg="#8eb8d1")
        self.timeLabelCount.place(x=670,y=150)  

        self.speedLabel = Label(self.root, text="Speed:", font=("arial",18,"bold"), bg="#8eb8d1")
        self.speedLabel.place(x=670,y=210)

        self.speedLabelCount = Label(self.root, text="0.00 WPM", font=("arial",18,), bg="#8eb8d1")
        self.speedLabelCount.place(x=670,y=260)      

        self.wordCountLabel = Label(self.root, text="Word Count:", font=("arial",18,"bold"), bg="#8eb8d1")
        self.wordCountLabel.place(x=670,y=320) 

        self.wordCount = Label(self.root, text= "0 Words", font=("arial",18), bg="#8eb8d1")
        self.wordCount.place(x=670,y=370) 

        self.resetButton = Button(self.root, text="Try Again", command=self.reset)
        self.resetButton.place(x=800,y=450)  

        ##################################################### CLASS VARIABLE DECLARATIONS          

        self.counter = 0
        self.running = False

        ##################################################### CALL MAIN LOOP
        self.root.mainloop()

    ##################################################### TIME METHOD
    def time(self, *args):
        global secCount
        if self.inputEntry.get() == self.sampleLabel.cget("text"):
            self.timeLabelCount.config(text="Finished in " + str(secCount) + " Seconds",font=("arial",18),fg="green")
        elif(secCount<9):
            secCount = secCount + 1
            self.timeLabelCount.config(text="00:0" + str(secCount))
            self.timeLabelCount.after(1000,self.time)
        elif(secCount<59):
            secCount = secCount + 1
            self.timeLabelCount.config(text="00:" + str(secCount))
            self.timeLabelCount.after(1000,self.time)

    ##################################################### START GAME METHOD
    def startGame(self, *args):
        if(secCount == 0):
            self.time()
        if not self.running:
            self.running = True
            t = threading.Thread(target=self.timeThread)
            t.start()
        else:
            self.inputEntry.config(fg="black")
        if self.inputEntry.get() == self.sampleLabel.cget("text")[:-1]:
            self.running = False
            self.inputEntry.config(fg="green")

    ##################################################### THREADING METHOD
    def timeThread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            CPS = len(self.inputEntry.get()) / self.counter
            CPM = CPS * 60
            WPM = CPM / 5
            worCount = len(self.inputEntry.get()) / 5
            self.speedLabelCount.config(text="Calculating...", font=("arial",15))
            self.wordCount.config(text=f"{worCount}  Words")
            if self.inputEntry.get() == self.sampleLabel.cget("text"):
                self.wordCount.config(text=f"{worCount}  Words",fg="green")
            if self.inputEntry.get() == self.sampleLabel.cget("text"):
                self.speedLabelCount.config(text=f"{WPM:.2f} WPM", font=("arial",18),fg="green")

    ##################################################### RESET BUTTON METHOD
    def reset(self):
        self.running = False
        self.counter = 0
        global secCount
        secCount = 0
        self.speedLabelCount.config(text="0.00 WPM", fg="black")
        self.wordCount.config(text="0 Words", fg="black")
        self.timeLabelCount.config(text="00:0" + str(secCount), fg="black")
        self.inputEntry.delete(0,END)

##################################################### GLOBAL VARIABLE DECLARATION
secCount=0

##################################################### INITIATE TYPE SPEED TEST CLASS
TypeSpeedTest()
