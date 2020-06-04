import sys
from pygame import *
from math import *
from random import *
import random
import math
init()

display_width = 1000
display_height = 700

shipx = 350
shipy = 550

asteroids=[]
astroidX=randint(0,800)
astroidY=randint(50,500)
astroidY_change=0

alien=[]
aliencounter=0
enemy_y =0
enemy_x=0

alienbullets=[]
w=[0,3]

gameDisplay = display.set_mode((display_width,display_height))

screen=display.set_mode((1000,700))



white = (255,255,255)
black = (0,0,0)


red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

blue = (0,0,255)

clock = time.Clock()

explosion_sound = mixer.Sound('./sounds/boom.wav')
bullet_sound = mixer.Sound('./sounds/shot1.wav')

bg_sound = mixer.Sound('./sounds/bgmusic1.ogg')

smallfont = font.SysFont("comicsansms", 25)
medfont = font.SysFont("comicsansms", 50)
largefont = font.SysFont("comicsansms", 85)
xlargefont = font.SysFont("Girassol", 100)

textx = 10
texty = 10


bg_imgs = ['./image/bg_big.png',
	    './image/seamless_space.png',
	    './image/space3.jpg']
bg_move_dis = 0
bg_1 = image.load(bg_imgs[0]).convert()
bg_2 = image.load(bg_imgs[1]).convert()
bg_3 = image.load(bg_imgs[2]).convert()

Score_1 = 200
Score_2 = 200
	
if (Score_1 + Score_2) < 500:
    background = bg_1
elif (Score_1 + Score_2) < 1500:
    background = bg_2
else:
    background = bg_3



v=[0,-5]#horiz and vertical speed of the bullet
#print(ets)


bullets=[]#empty list for bullets

astroid=image.load("image/meteorBrown_med1.png").convert_alpha()

alienspaceship=image.load("image/ufo.png").convert_alpha()

def show_score(x,y):
    score = smallfont.render("Score : " + str(score_value), True, light_yellow)
    screen.blit(score,(x,y))
def show_lives(x,y):
    lives = smallfont.render("Lives : " + str(livesr), True, light_yellow)
    screen.blit(lives,(x,y))                    

def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "xlarge":
        textSurface = xlargefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
   
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = mouse.get_pos()
    click = mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "Quit":
                quit()
                
            if action == "Play":
                play()
            if action == "Controls":
                control_menu()
            if action == "Back":
                quit()
            
    else:
        draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

def game_intro():
    menu_1 = image.load('./image/menubackground.jpg')
    gameDisplay.blit(menu_1,(0,0))

    intro = True

    while intro:
        for evt in event.get():
                #print(event)
                if evt.type == QUIT:
                    quit()
                    

                if evt.type == KEYDOWN:
                    if evt.key == K_c:
                        intro = False
                    elif evt.key == K_q:
                        
                        quit()
                        


        message_to_screen("Space Heroes!",green,-210,size="xlarge")
        message_to_screen("The objective is to shoot and destroy",white,-30)
        message_to_screen("the enemy ships before they destroy you.",white,10)
        message_to_screen("Defeat all of them to advance to next level!.",white,50)
        message_to_screen("By Wafi Hassan",blue, 110)

        button("Play", 230,500,100,50, green, light_green, action="Play")
        button("Controls", 430,500,100,50, yellow, light_yellow, action="Controls")
        button("Quit", 630,500,100,50, red, light_red, action ="Quit")

        display.update()

        clock.tick(15)



def control_menu():
    menu_1 = image.load('./image/menubackground.jpg')
    gameDisplay.blit(menu_1,(0,0))

    intro = True

    while intro:
        for evt in event.get():
                #print(event)
                if evt.type == QUIT:
                    quit()
                    

                if evt.type == KEYDOWN:
                    if evt.key == K_c:
                        intro = False
                    elif evt.key == K_q:
                        
                        quit()
 
        message_to_screen("Controls",blue,-210,size="large")
        message_to_screen("SPACE    -    SHOOT",white,-30)
        message_to_screen("W-A-S-D   -  up, down, left, right movement",white,10)

        button("Back", 550,500,100,50, red, light_red, action ="Back")

        display.update()

        clock.tick(15)

def game_over():
    bg_sound.stop()
    menu_1 = image.load('./image/gameover.jpg').convert()
    gameDisplay.blit(menu_1,(0,0))

    gameover = True

    while gameover:
        for evt in event.get():
                if evt.type == QUIT:
                    quit()

        button("QUIT", 550,500,100,50, red, light_red, action ="Quit")
        button("MENU", 310,500,100,50, red, light_red, action ="Back")

        display.update()

        clock.tick(15)

def play():
    display_width = 1000
    display_height = 700
    screen=display.set_mode((display_width,display_height))
    running=True
    y=0
    while running:
        for evt in event.get():
            #print(event)
                if evt.type == QUIT:
                    quit()
                    exit()
                    
                if evt.type == KEYDOWN:
                    if evt.key == K_e:
                          gameLoop()

        rel_y = y % bg_3.get_rect().width
        screen.blit(bg_3,(0,rel_y - bg_3.get_rect().width))
        if rel_y < 600:
            screen.blit(bg_3,(0,rel_y))
        y +=1

        message_to_screen("Attention, Fighter! ",blue,-300,size="medium")
        message_to_screen("You have been summoned by our government to protect our planet Kiblar.",white,-210)
        message_to_screen("We are being attacked by incoming enemies from the planet Noxus.",white,-170)
        message_to_screen("You are our only defender left, protect us at all costs!",white,-130)
        message_to_screen("Intelligence reports that there are 2 waves of enemies.",white,-90)
        message_to_screen("After you eliminate them all, they will send their mothership Dengrau.",white,-50)
        message_to_screen("Killing Dengrau will save our existence on galaxy 1029 from the rival planet Noxus.",white,-10)
        message_to_screen("ARE YOU READY TO TAKE THIS CHALLENGE?!",white,130)
        message_to_screen("CLICK [E] TO START!",red,190)

        
        display.update()

        myclock.tick(120)
     
    quit()


##def enemy_generate(): 
##
##    for i in range(5):
##        asteroids.append((randint(50 ,800),randint(0,100)))
##        


def drawScene(screen,sx,sy,bull,alienbull,alien,asteroids):
    
    lee=image.load("image/laserRed16.png").convert_alpha()
    bt=image.load("image/missile.png").convert_alpha()

    spaceship=image.load("image/ship.png").convert_alpha()
    screen.blit(spaceship,[sx,sy])  
    
    for b in bull:
        screen.blit(bt,(b[0],b[1]))#drawing the bullets
        
   
    for en in alien:  

        screen.blit(alienspaceship,(en[0],en[1]))


    for a in asteroids:
        screen.blit(astroid,(a[0] ,(a[1] + astroidY_change)))

    
    for eb in alienbull:
       
        screen.blit(lee,(eb[0],eb[1]))#drawing the bullets       


    display.update()
   

score_value=0
lives=3
def checkHits(bull,targ):
    global score_value 
    for b in bull:# go through each bullet
##        for a in astero:
##            aliendistance = math.sqrt((math.pow(b[0]-a[0],2)) + (math.pow(b[1]-a[1],2)))
##            if aliendistance < 50:
##                asteroids.remove(a)
##                bull.remove(b)
##                explosion_sound.play()
##                score_value+=1
##                break
        for t in targ: #go through each target
            distance = math.sqrt((math.pow(b[0]-t[0],2)) + (math.pow(b[1]-t[1],2)))
            if distance < 30:
                targ.remove(t)#removes the target
                bull.remove(b)#removes the bullet
                explosion_sound.play()
                score_value += 1
                if score_value==10:
                    next_level()
                break


livesr=3
def checkalienbullets(alienbull):
    global livesr
    global score_value
    for a in alienbull:
        alienbdistance=math.sqrt((math.pow(a[0]-shipx,2)) + (math.pow(a[1]-shipy,2)))
        if alienbdistance<40:
            livesr-=3
            print(livesr)
            if livesr<=0:
                game_over()
                


def moveBullets(bull):
    for b in bull:
        b[0]+=b[2]
        b[1]+=b[3]
        if b[1]>700:#off-screen
            bull.remove(b)

def move_alien_bull(ebull):
    for e in ebull:
        e[0]+=e[2]
        e[1]+=e[3]
        if e[1]>700:#off-screen
            ebull.remove(e)

def next_level():
    if random.randrange(0,6*40) == 1:
        aliencounter+=1
        x= randint(50,700)
        y= randint(0,100)
        alien.append([x,y])
        alienbullets.append([x,y,w[0],w[1]])

            
myclock=time.Clock()
##y=0

##enemy_generate() 

def gameLoop():
    livesr=3
    bg_sound.play(-1)
    rapidbullet=20
    y=0
    score=0
    ship_x =0
    ship_y=0 
    global shipx
    global shipy
    global aliencounter
    global astroidY 
    global astroidY_change
    global enemy_y
    global alien
##    global livesr
    direction= None
    running=True
    function=True
    

    while running:
        astroidY_change += .5
        #enemy_y += 0
        #global alienbullets
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                quit()
            if evt.type==KEYDOWN:
                if evt.key == K_LEFT:
                    ship_x = -2.5
                if evt.key == K_RIGHT:
                    ship_x = 2.5
##                if evt.key == K_UP: 
##                    ship_y = -2
##                if evt.key == K_DOWN: 
##                    ship_y = 2
            if evt.type==KEYUP:
                if evt.key == K_LEFT or evt.key == K_RIGHT: 
                    ship_x = 0
##                    ship_y = 0

        shipx += ship_x
##        shipy += ship_y 
        
        if shipx <= 0: 
            shipx = 0
        elif shipx >= 900:
            shipx = 900

##        if shipy <= 0: 
##            shipy = 0
##        elif shipy >= 650:
##            shipy = 650
            


        # astroid Movement
        astroidY += astroidY_change
        
        if astroidY_change >=650: 
           astroidY_change =0    

        
        if rapidbullet<20:
            rapidbullet+=1
        
        keys=key.get_pressed()       
        if keys[32] and rapidbullet==20:#32 is the space key
            bullet_sound.play()
 
            bullets.append([shipx,shipy,v[0],v[1]]) 
            rapidbullet=0
        
        while function:
            if random.randrange(0,6*40) == 1:
                aliencounter+=1
                x= randint(50,700)
                y= randint(0,100)
                alien.append([x,y])
                alienbullets.append([x,y,w[0],w[1]])
            if aliencounter==10:
                function=False



        rel_y = y % bg_3.get_rect().width
        screen.blit(bg_3,(0,rel_y - bg_3.get_rect().width))
        if rel_y < 700:
            screen.blit(bg_3,(0,rel_y))
        y +=1

        if enemy_y >= 600: 
           enemy_y = 0
           
        show_score(textx,texty)
        show_lives(10,40)
        moveBullets(bullets)
        move_alien_bull(alienbullets)
        checkHits(bullets,alien)
        checkalienbullets(alienbullets)
        drawScene(screen,shipx,shipy,bullets,alienbullets,alien,asteroids) 

        display.update()
        myclock.tick(120)
         
    quit()

game_intro()













