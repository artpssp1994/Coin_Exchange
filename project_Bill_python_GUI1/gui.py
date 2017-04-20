from Tkinter import *
import time

#----------------------------------------------------------------------

class MainWindow():

    #----------------

    def __init__(self, main):

        # amount of coins
        self.amountOfOneBaht = 0
        self.amountOfFiveBaht = 0
        self.amountOfTenBaht = 0
        
        # canvas for image
        self.canvas = Canvas(main, width=800, height=480,bg="#C6E2FF")
        self.canvas.grid(row=0, column=0)

        # add images
        self.imageIncreaseOne = PhotoImage(file = "button/bt_arrow/bt_increase.png")
        self.imageDecreaseOne = PhotoImage(file = "button/bt_arrow/bt_decrease.png")
        self.imageIncreaseFive = PhotoImage(file = "button/bt_arrow/bt_increase.png")
        self.imageDecreaseFive = PhotoImage(file = "button/bt_arrow/bt_decrease.png")
        self.imageIncreaseTen = PhotoImage(file = "button/bt_arrow/bt_increase.png")
        self.imageDecreaseTen = PhotoImage(file = "button/bt_arrow/bt_decrease.png")
        self.imageApprove = PhotoImage(file = "button/bt_approve/bt_approve.png")
        self.imageReset = PhotoImage(file = "button/bt_reset/bt_reset.png")
        self.imageOneBaht = PhotoImage(file = "coins/onebaht.png")
        self.imageFiveBaht = PhotoImage(file = "coins/fivebaht.png")
        self.imageTenBaht = PhotoImage(file = "coins/tenbaht.png")
        self.imageCanvas01 = PhotoImage(file = "canvas/canvas01.png")
        self.imageCanvas02 = PhotoImage(file = "canvas/canvas02.png")

        # set location images on canvas
        self.objectIncreaseOne = self.canvas.create_image(500, 30, anchor=NW, image=self.imageIncreaseOne)
        self.objectDecreaseOne = self.canvas.create_image(500, 95, anchor=NW, image=self.imageDecreaseOne)
        self.objectIncreaseFive = self.canvas.create_image(500, 170, anchor=NW, image=self.imageIncreaseFive)
        self.objectDecreaseFive = self.canvas.create_image(500, 235, anchor=NW, image=self.imageDecreaseFive)
        self.objectIncreaseTen = self.canvas.create_image(500, 310, anchor=NW, image=self.imageIncreaseTen)
        self.objectDecreaseTen = self.canvas.create_image(500, 375, anchor=NW, image=self.imageDecreaseTen)
        
        self.objectApprove = self.canvas.create_image(600, 400, anchor=NW, image=self.imageApprove)
        self.objectReset = self.canvas.create_image(600, 315, anchor=NW, image=self.imageReset)
        
        self.objectOneBaht = self.canvas.create_image(270, 40, anchor=NW, image=self.imageOneBaht)
        self.objectFiveBaht = self.canvas.create_image(270, 180, anchor=NW, image=self.imageFiveBaht)
        self.objectTenBaht = self.canvas.create_image(270, 320, anchor=NW, image=self.imageTenBaht)

        self.objectCanvas01 = self.canvas.create_image(375, 40, anchor=NW, image=self.imageCanvas01)
        self.objectCanvas02 = self.canvas.create_image(375, 180, anchor=NW, image=self.imageCanvas01)
        self.objectCanvas03 = self.canvas.create_image(375, 320, anchor=NW, image=self.imageCanvas01)
        self.objectCanvas04 = self.canvas.create_image(5, 8, anchor=NW, image=self.imageCanvas02)

        # event on click       
        self.buttonIncreaseOne = self.canvas.tag_bind(self.objectIncreaseOne, '<Button-1>', self.increaseOne)
        self.buttonDecreaseOne = self.canvas.tag_bind(self.objectDecreaseOne, '<Button-1>', self.decreaseOne)
        self.buttonIncreaseFive = self.canvas.tag_bind(self.objectIncreaseFive, '<Button-1>', self.increaseFive)
        self.buttonDecreaseFive = self.canvas.tag_bind(self.objectDecreaseFive, '<Button-1>', self.decreaseFive)
        self.buttonIncreaseTen = self.canvas.tag_bind(self.objectIncreaseTen, '<Button-1>', self.increaseTen)
        self.buttonDecreaseTen = self.canvas.tag_bind(self.objectDecreaseTen, '<Button-1>', self.decreaseTen)
        self.buttonApprove = self.canvas.tag_bind(self.objectApprove, '<Button-1>', self.approve)
        self.buttonReset = self.canvas.tag_bind(self.objectReset, '<Button-1>', self.reset)
        self.canvas.pack()

    #----------------------------------------------
    # increase one baht
    
    def increaseOne(self, event):

        self.amountOfOneBaht += 5
        print("amount of one baht :",self.amountOfOneBaht)

    def decreaseOne(self, event):

        if (self.amountOfOneBaht > 0):
            self.amountOfOneBaht -= 5
        print("amount of one baht :",self.amountOfOneBaht)

    #----------------
    # increase five baht

    def increaseFive(self, event):

        self.amountOfFiveBaht += 1
        print("amount of five baht :",self.amountOfFiveBaht)

    def decreaseFive(self, event):

        if (self.amountOfFiveBaht > 0):
            self.amountOfFiveBaht -= 1
        print("amount of five baht :",self.amountOfFiveBaht)

    #----------------
    # increase ten baht

    def increaseTen(self, event):

        self.amountOfTenBaht += 1
        print("amount of ten baht :",self.amountOfTenBaht)

    def decreaseTen(self, event):

        if (self.amountOfTenBaht > 0):
            self.amountOfTenBaht -= 1
        print("amount of ten baht :",self.amountOfTenBaht)

    #----------------------------------------------
    # approve button
    
    def approve(self, event):
        print("Approveeeeeeee!!")

    #----------------
    # reset button

    def reset(self, event):
        self.amountOfOneBaht = 0
        self.amountOfFiveBaht = 0
        self.amountOfTenBaht = 0
        print("amount of one baht :",self.amountOfOneBaht)
        print("amount of five baht :",self.amountOfFiveBaht)
        print("amount of ten baht :",self.amountOfTenBaht)

#----------------------------------------------------------------------

root = Tk()
MainWindow(root)
root.mainloop()
