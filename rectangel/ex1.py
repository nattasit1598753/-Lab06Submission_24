import sys 
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        
    def draw(self,screen):
        pg.draw.rect(screen,self.c,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
        self.c = (255, 0, 0)  

    def isMouseOn(self):
        if pg.mouse.get_pos()[0] > self.x and pg.mouse.get_pos()[0] < self.x + self.w and pg.mouse.get_pos()[1] > self.y and pg.mouse.get_pos()[1] < self.y + self.h:
            self.c = (128, 128, 128)  
            return True
        else:
            self.c = (255, 0, 0)  
            return False
        
    def isMousePressed(self):
        if pg.mouse.get_pos()[0] > self.x and pg.mouse.get_pos()[0] < self.x + self.w and pg.mouse.get_pos()[1] > self.y and pg.mouse.get_pos()[1] < self.y + self.h and pg.mouse.get_pressed()[0] == True:
            self.c = (200, 0, 200) 
            return True
        else:
            self.c = (255, 0, 0) 
            return False
        
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา


while(run):
    screen.fill((255, 255, 255))  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if btn.isMousePressed():
        btn.draw(screen)
    elif btn.isMouseOn():
        btn.draw(screen)
    
    else:
        btn.c = (255, 0, 0) 
        btn.draw(screen)

    

    pg.display.update()

print("Exiting program")
pg.quit()
sys.exit()
