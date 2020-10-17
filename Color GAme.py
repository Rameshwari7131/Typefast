# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:16:40 2020

@author: RITESH JADHAV
"""

# import the modules  
import tkinter as tk 
import random 

  
# list of possible colour. 
colours = ['Red','Blue','Green','Black', 
           'Yellow','Orange','White','Purple','Brown'] 
score = 0
  
# the game time left, initially 30 seconds. 
timeleft = 60

def open_window():
    top = tk.Toplevel()
    top.title("top window")
    top.geometry("500x400")
    

  
# function that will start the game. 
def startGame(event): 
      
    if timeleft == 60: 
          
        # start the countdown timer. 
        countdown() 
          
    # run the function to 
    # choose the next colour. 
    nextColour() 
  
# Function to choose and 
# display the next colour. 
def nextColour(): 
  
    # use the globally declared 'score' 
    # and 'play' variables above. 
    global score 
    global timeleft 
  
    # if a game is currently in play 
    if timeleft > 0: 
  
        # make the text entry box active. 
        e.focus_set() 
  
        # if the colour typed is equal 
        # to the colour of the text 
        

        if e.get().lower() == colours[1].lower(): 
              
            score += 1
  
        # clear the text entry box. 
        e.delete(0, tk.END) 
          
        random.shuffle(colours) 
          
        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value 
        label.config(fg = str(colours[1]), text = str(colours[0])) 
          
        # update the score. 
        scoreLabel.config( text = "YOUR SCORE  IS : " + str(score)) 
        
        if (timeleft == 0):
            label.config(text = "TIME OUT"+ str(timeleft))
            label.pack()
  
  
# Countdown timer function  
def countdown(): 
  
    global timeleft 
  
    # if a game is in play 
    if timeleft > 0: 
  
        # decrement the timer. 
        timeleft -= 1
          
        # update the time left label 
        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 
                                 
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown) 
  # quit game

         

    
# Driver Code 
  
# create a GUI window 
root = tk.Tk() 
  
# set the title 
root.title("COLORGAME") 
  
# set the size 
root.geometry("500x400") 

#set window colour
root['background'] = '#856ff8'



# add an instructions label 
instructions = tk.Label(root, text = "Type in the colour "
                        "of the words, and not the word text!!", bg= '#856ff8',
                        font = ('Arial', 15)) 
instructions.pack()  

#label for space
label_2 = tk.Label(root,text = " ", bg= '#856ff8')
label_2.pack()
  
# add a score label 
scoreLabel = tk.Label(root, text = "Press  ENTER  to start", bg= '#856ff8',
                                      font = ('Arial', 13)) 
scoreLabel.pack() 

#label for space
label_3 = tk.Label(root,text = " ", bg= '#856ff8')
label_3.pack()
  
# add a time left label 
timeLabel = tk.Label(root, text = "Time left: " +
              str(timeleft), bg= '#856ff8', font = ('Helvetica', 12)) 
                
timeLabel.pack() 

# add a label for displaying the colours 
label = tk.Label(root, font = ('Helvetica', 60), bg= '#856ff8') 
label.pack() 

# add a text entry box for 
# typing in colours 
e = tk.Entry(root, width = 25) 
  
# run the 'startGame' function  
# when the enter key is pressed 

root.bind('<Return>', startGame) 
e.pack() 

#label for space
label_4 = tk.Label(root,text = " ", bg= '#856ff8')
label_4.pack()

# set focus on the entry box 
e.focus_set() 

# exit button
b1 = tk.Button(root, text = "Click Here to Exit",font = ('Helvetica', 10), bg= '#000000', fg = '#fff',command = root.destroy,width=12 )
b1.pack()



#label for space
label_4 = tk.Label(root,text = " ",bg= '#856ff8')
label_4.pack()



#label for space
label_5 = tk.Label(root,text = " ",bg= '#856ff8')
label_5.pack()

#SCORE LABLE

scoreLabel = tk.Label(root, text = " ****WEL-COME ****", bg= '#856ff8',
                                      font = ('Arial', 16)) 
scoreLabel.pack()

  
# start the GUI 
root.mainloop() 
