import sys 
import pygame as pg

class Textbox:
    def __init__(self,x,y,text=""):
        self.x = x
        self.y = y
        self.text = text
        
    def draw(self,Screen):
        self.surface = FONT.render(self.text,True,(0,0,0))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (self.x,self.y)
        Screen.blit(self.surface,self.rect)

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
                    print(list_text)
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
    def drawgreen(self,screen):
        pg.draw.rect(screen,(0,255,0),(self.x,self.y,self.w,self.h))


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
        
    def isClicked(self):
        if self.isMouseOn() and pg.mouse.get_pressed()[0]:
            return True
        else:
            return False
        
#---------------------------------------------------------------------------------------------------        

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button((win_x // 2)-100 , 300 ,200,50) # สร้าง Object จากคลาส Button ขึ้นมา
# output = "321"

COLOR_INACTIVE = pg.Color(0,0,0) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(255,0,0)     # ^^^
FONT = pg.font.Font(None, 32)
input_box1 = InputBox(150, 80, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(150, 140, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(150, 200, 140, 32) # สร้าง InputBox3
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

font = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
list_text = ["", "", ""]
form_name = Textbox(280,40,"Personal information form")
name = Textbox(20,90,"Name")
surname = Textbox(20,150,"Surname")
age = Textbox(20,210,"Age")
answer = Textbox(50,400,"")
submit = Textbox(360,315, "Submit")
all_text = [form_name, name, surname, age, answer, submit]
age_error = Textbox(50,430, "Age must be number")
information_error = Textbox(50,400, "Please complete all fields.")

while run:
    screen.fill((255, 255, 255))
    btn.drawgreen(screen)

    for text in all_text:
        text.draw(screen)
    
    for box in input_boxes: 
        box.update() 
        box.draw(screen)
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    
    if len(input_box3.text) != 0: 
        if input_box3.text.isdigit() == False:
            age_error.draw(screen)

    if btn.isClicked() == True:
        if input_box1.text != "" and input_box2.text != "" and input_box3.text != "":
            list_text[0] = input_box1.text
            list_text[1] = input_box2.text
            list_text[2] = input_box3.text
            output = str("Hello " + list_text[0] + " " + list_text[1] + "! " + "You are " + list_text[2] + " years old.")
            answer.text = output
        else:
            information_error.draw(screen)
        
    pg.time.delay(1)
    pg.display.update()