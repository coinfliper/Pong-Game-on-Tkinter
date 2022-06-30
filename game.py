from tkinter import *
import random
import time

class Ball:

    def __init__(self,canvas,paddle,color):
        self.score = 0
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,51,51,fill=color)
        self.canvas.move(self.id,669,376)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -6
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score = self.score + 1
                return True
        return [False,self.score]

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 8
        if self.hit_paddle(pos) == True:
            self.y = -8
        if pos[0] <= 0:
            self.x = 8
        if pos[2] >= self.canvas_width:
            self.x = -8
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        
    def my_score(self):
        if self.hit_bottom == True:
            print('Your score:',self.score)
        return self.score

class Paddle:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,273,27,fill=color)
        self.canvas.move(self.id,546,590)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -11

    def turn_right(self,evt):
        self.x = 11

tk=Tk()
tk.title('PONG')
tk.attributes('-fullscreen', True)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=1366,height=768,bd=0,bg="#e3c42b")
canvas.pack()
tk.update()

paddle = Paddle(canvas,"red")
ball = Ball(canvas,paddle,"blue")

while 1:
    if ball.hit_bottom == False:
        paddle.draw()
        ball.draw()
    elif ball.hit_bottom == True:
        time.sleep(0.9)
        ball.my_score()
        tk.destroy()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.0001)
   
    
