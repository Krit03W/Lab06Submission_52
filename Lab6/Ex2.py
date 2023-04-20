class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))
        
import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
key=''
while(run):
    screen.fill((255, 255, 255))
    
    if key == 'w':
        firstObject.y -= 0.3
        if event.type == pg.KEYUP and event.key == pg.K_w:
                key = ''
    if key == 'a':
        firstObject.x -= 0.3
        if event.type == pg.KEYUP and event.key == pg.K_a:
                key = ''
    if key == 's':
        firstObject.y += 0.3
        if event.type == pg.KEYUP and event.key == pg.K_s:
                key = ''
    if key == 'd':
        firstObject.x += 0.3
        if event.type == pg.KEYUP and event.key == pg.K_d:
                key = ''
    firstObject.draw(screen)          
    pg.display.update()   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN and event.key == pg.K_w: 
            key = 'w'
        if event.type == pg.KEYDOWN and event.key == pg.K_a: 
            key = 'a'
        if event.type == pg.KEYDOWN and event.key == pg.K_s: 
            key = 's'
        if event.type == pg.KEYDOWN and event.key == pg.K_d: 
            key = 'd'
            
     
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False