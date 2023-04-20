class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
        
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(255,25,255),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        (x,y) = pg.mouse.get_pos()
        if(self.x<=x<=self.w+self.x and self.y<=y<=self.h+self.y and pg.mouse.get_pressed()[0]==1):
            return 1
        pass
        
import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(400,350,100,70)

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(250, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(250, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(250, 300, 140, 32) # สร้าง InputBox3
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
font1 = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
text1 = font.render('Firstname', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect1 = text1.get_rect() # text size
textRect1.center = (350, 80)
text2 = font.render('Lastname', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (350, 180)
text3 = font.render('Age', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (350, 280)
text4 = font.render('SUMIT', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect4 = text4.get_rect() # text size
textRect4.center = (450, 390)
text5 = font1.render('Hello' + str(input_box1.text) +str(input_box2.text)+'! You are' +str(input_box3.text) +'years old.', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect5 = text5.get_rect() # text size
textRect5.center = (win_x//2, 450)

m=0
posx=0
posy=0
while run:
    screen.fill((0,255, 255))
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    if btn.isMouseOn()==1:
        text5 = font1.render('Hello ' + str(input_box1.text) +' '+str(input_box2.text)+' ! You are ' +str(int(input_box3.text)) +' years old.', True, (200,0,0))
        textRect5 = text5.get_rect() # text size
        textRect5.center = (win_x//2, 450)
        m=1
    else:
        btn.draw(screen)
    if m == 1:
        screen.blit(text5, textRect5)
        
    pg.draw.circle(screen,(200,0,255),(posx,posy),20)
    pg.draw.circle(screen,(255,0,0),(posy,posx),30)
    pg.draw.rect(screen,(0,255,0),(0,0,20,480))
    pg.draw.rect(screen,(0,255,0),(0,0,800,20))
    pg.draw.rect(screen,(0,255,0),(780,0,20,480))
    pg.draw.rect(screen,(0,255,0),(0,460,800,20))
    posx+=0.3
    posy+=0.1
    if(posx>=win_x):posx=0
    if(posy>=win_y):posy=0
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    screen.blit(text4, textRect4)
    pg.time.delay(1)
    pg.display.update()

