class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        (x,y) = pg.mouse.get_pos()
        # print(x,y)
        if(self.x<=x<=self.w+self.x and self.y<=y<=self.h+self.y and pg.mouse.get_pressed()[0]==1):
            return 1
        elif(self.x<=x<=self.w+self.x and self.y<=y<=self.h+self.y):
            return 2
        pass

import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(340,200,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    
    screen.fill((255, 255, 255))
    if btn.isMouseOn()==1:
        pg.draw.rect(screen,(148,0,211),(btn.x,btn.y,btn.w,btn.h))
    elif btn.isMouseOn()==2:
        pg.draw.rect(screen,(211,211,211),(btn.x,btn.y,btn.w,btn.h))
    else:
        btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
