import sys 
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def drawred(self,screen):
        pg.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))


class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        if pg.mouse.get_pos()[0] > btn.x and pg.mouse.get_pos()[0] < btn.x + btn.w and pg.mouse.get_pos()[1] > btn.y and pg.mouse.get_pos()[1] < btn.y + btn.h:
            return True
        # pass
    def isMousePressed(self):
        if pg.mouse.get_pressed()[0] == 1:
            return True


pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(350,190,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

w_pressed = False
a_pressed = False
s_pressed = False
d_pressed = False

while(run):
    screen.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            w_pressed = True
        if event.type == pg.KEYUP and event.key == pg.K_w:
            w_pressed = False
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            a_pressed = True
        if event.type == pg.KEYUP and event.key == pg.K_a:
            a_pressed = False
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            s_pressed = True
        if event.type == pg.KEYUP and event.key == pg.K_s:
            s_pressed = False
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            d_pressed = True
        if event.type == pg.KEYUP and event.key == pg.K_d:
            d_pressed = False
   
    if w_pressed:
        btn.y -= 0.1
    if a_pressed:
        btn.x -= 0.1
    if s_pressed:
        btn.y += 0.1
    if d_pressed:
        btn.x += 0.1

   
    btn.drawred(screen)


    pg.display.update()

print("Exiting program")
pg.quit()
sys.exit()