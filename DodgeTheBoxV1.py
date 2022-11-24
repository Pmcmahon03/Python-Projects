import pygame as pg
import sys, random, time

#Variables
pg.init()
rgb = (0,0,150)
pc = (250,0,0) #player colour
ps = 0 #player speed
os = 4 #obstacle speed

class Game():
    def __init__(self,w,h,pg,rgb,pc,ps,os):
        self.h = h
        self.w = w
        self.pg = pg
        self.rgb = rgb
        self.pc = pc
        self.ps = ps
        self.os = os
        self.counter = 0
        self.pos_x = random.choice(range(0,self.w))
        self.pos_y = random.choice(range(0,self.h))
        self.screen = pg.display.set_mode((self.w,self.h))
        self.circle = pg.Rect(self.w/2 - 15,self.h-35,30,30)
        self.square = pg.Rect(self.pos_x,self.pos_y,40,40)
        self.square_2 = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,self.h)),40,40)
        self.square_3 = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,self.h)),40,40)
        self.square_4 = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,self.h)),40,40)
        self.square_5 = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,self.h)),40,40)
        self.clock = pg.time.Clock()
       
    def Game_loop(self):
        while True:
            self.game_clock()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        self.ps += 7
                    if event.key == pg.K_LEFT:
                        self.ps -= 7
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT:
                        self.ps -= 7
                    if event.key == pg.K_LEFT:
                        self.ps += 7
                       
                     
            self.change_background()            
            self.load_player()
            #self.obstacle_gen()
            self.obstacle()
           
            if self.counter >= 120:
                self.obstacle_2()
               
            if self.counter >= 300:
                self.obstacle_3()
               
            if self.counter >= 600:
                self.obstacle_4()
               
            if self.counter >= 21600:
                self.obstacle_5()
               
            if self.counter >= 600:
                self.speed_up()
               
            self.refresh_screen()

   
    def change_background(self):
        self.screen.fill(self.rgb)
        #self.refresh_screen()
        pass
   
    def game_clock(self):
        self.clock.tick(60)
        pass
   
    def refresh_screen(self):
        pg.display.flip()
        pass
   
    def load_player(self):
        pg.draw.ellipse(self.screen,self.pc,self.circle)
        self.player_animation()
        pass
       
    def player_animation(self):
        self.circle.x += self.ps
        if self.circle.left <= 0:
            self.circle.left = 0
        if self.circle.right >= self.w:
            self.circle.right = self.w
        pass
   
    def speed_up(self):
        self.os += 0.001
        pass
   
    def obstacle(self):
        pg.draw.rect(self.screen,self.pc,self.square)
        #pg.draw.rect(self.screen,self.pc,self.square_2)
       
        #self.obstacle_gen()
       
        if self.square.colliderect(self.circle):
            pg.quit()
            sys.exit()
       
        if self.square.left < 0:
            self.square.left = 0
        if self.square.right > self.w:
            self.square.right = self.w
        if self.square.top <= 0:
            self.square.top = 0
        if self.square.bottom >= self.h:
            self.square.bottom = 0
            self.square = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,100)),40,40)
           
        self.square.y += self.os
       
        self.counter += 1
        pass
   
    def obstacle_2(self):
        pg.draw.rect(self.screen,self.pc,self.square_2)
       
        if self.square_2.colliderect(self.circle):
            pg.quit()
            sys.exit()
       
        if self.square_2.left < 0:
            self.square_2.left = 0
        if self.square_2.right > self.w:
            self.square_2.right = self.w
        if self.square_2.top <= 0:
            self.square_2.top = 0
        if self.square_2.bottom >= self.h:
            self.square_2.bottom = 0
            self.square_2 = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,100)),40,40)
           
        self.square_2.y += self.os
        pass
       
    def obstacle_3(self):
        pg.draw.rect(self.screen,self.pc,self.square_3)
       
        if self.square_3.colliderect(self.circle):
            pg.quit()
            sys.exit()
       
        if self.square_3.left < 0:
            self.square_3.left = 0
        if self.square_3.right > self.w:
            self.square_3.right = self.w
        if self.square_3.top <= 0:
            self.square_3.top = 0
        if self.square_3.bottom >= self.h:
            self.square_3.bottom = 0
            self.square_3 = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,100)),40,40)
           
        self.square_3.y += self.os
        pass
       
    def obstacle_4(self):
        pg.draw.rect(self.screen,self.pc,self.square_4)
       
        if self.square_4.colliderect(self.circle):
            pg.quit()
            sys.exit()
       
        if self.square_4.left < 0:
            self.square_4.left = 0
        if self.square_4.right > self.w:
            self.square_4.right = self.w
        if self.square_4.top <= 0:
            self.square_4.top = 0
        if self.square_4.bottom >= self.h:
            self.square_4.bottom = 0
            self.square_4 = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,100)),40,40)
           
        self.square_4.y += self.os
        pass
   
    def obstacle_5(self):
        pg.draw.rect(self.screen,self.pc,self.square_5)
       
        if self.square_5.colliderect(self.circle):
            pg.quit()
            sys.exit()
       
        if self.square_5.left < 0:
            self.square_5.left = 0
        if self.square_5.right > self.w:
            self.square_5.right = self.w
        if self.square_5.top <= 0:
            self.square_5.top = 0
        if self.square_5.bottom >= self.h:
            self.square_5.bottom = 0
            self.square_5 = pg.Rect(random.choice(range(0,self.w)),random.choice(range(0,100)),40,40)
           
        self.square_5.y += self.os
        pass
       
           
#    def obstacle_gen(self):
#        
#        obj_list = []
#        
#        while self.counter < 10:
#            for i in range(0,1):
#                self.pos_x = random.choice(range(0,self.w))
#                self.pos_y = random.choice(range(0,self.h))
#
#            self.obj = self.square = pg.Rect(self.pos_x,self.pos_y,40,40)
#            obj_list.append(self.obj)
#            #time.sleep(2)
#            self.counter += 1
#            
#        for i in obj_list:
#            print(i)
#            pg.draw.rect(self.screen,self.pc,i)
#            
#        pass

game = Game(550,600,pg,rgb,pc,ps,os) #calling object|originalw=550 originalh=400
game.Game_loop() #calling game loop