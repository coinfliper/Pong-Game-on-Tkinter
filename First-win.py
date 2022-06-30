from tkinter import *
import random
import time


root = Tk()
root.title("PONG")
root.attributes('-fullscreen', True)
root["bg"] = "#e3c42b"

#to start game, update the address of the folder with the First-win files.py and game.py

def start_game():
    exec(open('D:\\Desktop\\PONG\\game.py').read())

def quit_game():
    root.destroy()

btn1 = Button(text = "Играть" , padx = "20" , pady = "8" ,
             bg = "#e3c42b" , fg = "black" , activebackground = "#e6d651" ,
             activeforeground = "black", bd = "6" , relief = "solid"  ,
             font = "Arial 40" , command = start_game)
btn1.place(relx =.5 , rely =.4 , anchor = "c" , height = 100 ,
          width = 300 , bordermode = OUTSIDE )

#after clicking the "Play" button, in order for the stream to be transferred to the game file window, you need to click on the screen

#your score will be displayed in the console

btn2 = Button(text = "Выйти" , padx = "20" , pady = "8" ,
             bg = "#e3c42b" , fg = "black" , activebackground = "#e6d651" ,
             activeforeground = "black", bd = "6" , relief = "solid"  ,
             font = "Arial 40" , command = quit_game)
btn2.place(relx =.5 , rely =.6 , anchor = "c" , height = 100 ,
          width = 300 , bordermode = OUTSIDE )

root.mainloop()