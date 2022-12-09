'''
Project by Wafi Hassan
'''

import sys
from pygame import *
from math import *
from random import *
import random
import math
init()

#display setting
display_width = 1000
display_height = 700
gameDisplay = display.set_mode((display_width,display_height))
screen=display.set_mode((1000,700))

#defining colour for fonts
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)
blue = (0,0,255)

#initializing the clock
myclock=time.Clock()

#initializing variables
shipx = 350
shipy = 550
current_level=0
astroidY_change=0
astroidX=randint(0,800)
astroidY=randint(50,500)
aliencounter=0
enemy_y =0
enemy_x=0
gameover=False
textx = 8
texty = 40
score_value=0
livesr=1

asteroids=[]
alien=[]
alienbullets=[]
w=[0,3]##vertical speed of the enemy space ship bullet going downwards
v=[0,-5]#vertical speed of the space ship bullet going upwards
bullets=[]#empty list for bullets

#loading sounds
explosion_sound = mixer.Sound('./sounds/boom.wav')
bullet_sound = mixer.Sound('./sounds/shot1.wav')
bg_sound = mixer.Sound('./sounds/bgmusic1.ogg')


#setting volume
aaaaa=explosion_sound.set_volume(0.15)
bbbbb=bullet_sound.set_volume(0.15)
bbbbb=bg_sound.set_volume(0.05)

#defining font types and sizes
smallfont = font.SysFont("comicsansms", 25)
medfont = font.SysFont("comicsansms", 50)
largefont = font.SysFont("comicsansms", 85)
xlargefont = font.SysFont("Girassol", 100)



#loading images
bg_imgs = ['./image/bg_big.png',
	    './image/seamless_space.png',
	    './image/space3.jpg']

bg_1 = image.load(bg_imgs[0]).convert()
bg_2 = image.load(bg_imgs[1]).convert()
bg_3 = image.load(bg_imgs[2]).convert()
astroid=image.load("image/meteorBrown_med1.png").convert_alpha()
alienspaceship=image.load("image/ufo.png").convert_alpha()

#defining function to show score
def show_score(x,y):
    score = smallfont.render("Score : " + str(score_value), True, light_yellow)#rendering a font with colour and variable attributes
    screen.blit(score,(x,y))#blitting the score onto the screen
    
#defining function to show lives
def show_lives(x,y):
    lives = smallfont.render("Lives : " + str(livesr), True, green)
    screen.blit(lives,(x,y))
    
#defining function to show level
def show_level(x,y):
    level = smallfont.render("Level : " + str(current_level), True, blue)
    screen.blit(level,(x,y))
    
#defining text_object function to render text on surface
def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "xlarge":
        textSurface = xlargefont.render(text, True, color)

    return textSurface, textSurface.get_rect()#returns the text and gets the reactangular area of the surface

#defining function to text on button
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

#defining function to display message on screen   
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

#defining functions of buttons and their actions
def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = mouse.get_pos() #get the mouse cursor position
    click = mouse.get_pressed()#state of all the mouse buttons
    
    if x + width > cur[0] > x and y + height > cur[1] > y: # if mouse click inside x and y range
        draw.rect(gameDisplay, active_color, (x,y,width,height)) # highlight button if cursors pointed 
        if click[0] == 1 and action != None:#if left mouse button is clicked and an action is present.
            if action == "Quit":
                quit() # quit the game 
                
            if action == "Play":
                play() # go to the play function
            if action == "Controls":
                control_menu() # go to the control function
            if action == "Back":
                game_intro()
            if action =="Start":
                gameLoop() # # go to the gameLoop function
            
    else:
        draw.rect(gameDisplay, inactive_color, (x,y,width,height))#wont highlight button

    text_to_button(text,black,x,y,width,height)

#game start with calling this function
def game_intro():
    menu_1 = image.load('./image/menubackground.jpg')#making the background under variable menu_1
    gameDisplay.blit(menu_1,(0,0))#assigning the game display under the menu_1 background

    intro = True

    while intro:#while loop, will continue running until intro=False
        for evt in event.get():
                if evt.type == QUIT:
                    quit()
                       

        message_to_screen("Space Heroes!",green,-210,size="xlarge")#printing message onto pygame screen 
        message_to_screen("The objective is to shoot and destroy",white,-30)
        message_to_screen("the enemy ships before they destroy you.",white,10)
        message_to_screen("Defeat all of them to advance to next level!.",white,50)
        message_to_screen("By Wafi Hassan",blue, 110)

        button("Play", 230,500,100,50, green, light_green, action="Play")#Using the button function on the main menu for navigation.
        button("Controls", 430,500,100,50, yellow, light_yellow, action="Controls")
        button("Quit", 630,500,100,50, red, light_red, action ="Quit")

        display.update()#update the contents of the entire display

        myclock.tick(15) # tick after 15 nanoseconds


#this function will display game control rules
def control_menu():
    menu_1 = image.load('./image/menubackground.jpg')
    gameDisplay.blit(menu_1,(0,0))

    intro = True#assigning intro as true

    while intro:#will continue running until intro is defined as False
        for evt in event.get():
                #print(event)
                if evt.type == QUIT:
                    quit()
                    
 
        message_to_screen("Controls",blue,-210,size="large")
        message_to_screen("SPACE    -    SHOOT",white,-30)
        message_to_screen("[R] and [L] arrow keys   -  Left and Right movement",white,10)

        button("Back", 550,500,100,50, red, light_red, action ="Back")#button displaying "Back" and assigned the action "back"

        display.update()

        myclock.tick(15)

# this function will initialize all variables after game over and giving player an option to start play again.
def game_over():
    global alien#the reason we global all the variables is because to change a value to a variable throughout the whole code, you must use global. Other wise I would be starting the game with 0 lives etc.
    global alienbullets
    global livesr
    global score_value
    global shipx
    global shipy
    global current_level
    global aliencounter
    global asteroids
    global bullets
    
    #creating empty lists for everything in the game so that all the progress can be reset.
    bullets=[]
    asteroids=[]
    aliencounter=0
    alien=[]
    alienbullets=[]
    livesr=1
    score_value=0
    current_level=1
    
    bg_sound.stop()#stops the background sound
    menu_1 = image.load('./image/gameover.jpg').convert_alpha()#loading the gameover image
    gameDisplay.blit(menu_1,(0,0))

    gameover = True

    while gameover:
        for evt in event.get():
            if evt.type == QUIT:
                gameover=False
                quit()
                

        button("QUIT", 550,500,100,50, red, light_red, action ="Quit")
        button("RESTART", 310,500,115,50, red, light_red, action ="Start")

        display.update()

        myclock.tick(15)#runs at 15fps

        
        
# this function will take you to the play screen with the introduction to the story and to start the game
def play():
    screen=display.set_mode((display_width,display_height))
    running=True
    y=0 #initializing
    while running:
        for evt in event.get():
            #print(event)
                if evt.type == QUIT:
                    quit()
                    
                    
                if evt.type == KEYDOWN:
                    if evt.key == K_e: # if "E" button pressed the game will start
                          gameLoop()

        rel_y = y % bg_3.get_rect().width#making sure the background fits onto the screen by findingthe width remaining.
        screen.blit(bg_3,(0,rel_y - bg_3.get_rect().width))#blitting the rest of the width back on the background as it moves down the screen.
        if rel_y < 600: # if the background goes off the screen
            screen.blit(bg_3,(0,rel_y)) 
        y +=1 # moving background image downwards

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

        myclock.tick(120)#120fps
     
    quit()

# this function will randomly generating five asteroids(used in lvl3)
def enemy_generate(): 
    for i in range(5):#continuous for loop that will run 5 times
        asteroids.append((randint(50 ,800),randint(0,100)))#appending 5 random coordinates of the asteroids into the empty list "asteroids"
        

#this function will draw aliens, asteroids, bullet and alien bullets on screen
def drawScene(screen,sx,sy,bull,alienbull,alien,asteroids):
    
    at=image.load("image/laserRed16.png").convert_alpha()
    bt=image.load("image/missile.png").convert_alpha()
    spaceship=image.load("image/ship.png").convert_alpha()
    screen.blit(spaceship,[sx,sy])  
    
    for b in bull:#for loop that runs under values "b" and takes values out of "bull"
        screen.blit(bt,(b[0],b[1]))#drawing the bullets
        
   
    for en in alien:  

        screen.blit(alienspaceship,(en[0],en[1]))#drawing the aliens


    for a in asteroids:  
        astroid=image.load("image/meteorBrown_med1.png").convert_alpha()
        screen.blit(astroid,(a[0],(a[1]+astroidY_change))) ##drawing the astreroids and moving downwards

    
    for eb in alienbull:
       
        screen.blit(at,(eb[0],eb[1]))#drawing the aliens bullets       


    display.update()
   
##score_value=0

#this function will check whether any bullet hit any object 
def checkHits(bull,targ,astero):
    global score_value #global score value since we are changing the score based on if bullet hits target, we want the score value to change globally
    for b in bull:# go through each bullet
        for a in astero:
            astrod = math.sqrt((math.pow(b[0]-a[0],2)) + (math.pow(b[1]-a[1],2)))#distance formula applied through the distance between the bullet and asteroid.
            if astrod < 50: # if distance less than 50
                asteroids.remove(a)# remove asteroid if hits
                bull.remove(b)#remove bullet if hits
                explosion_sound.play() # explosion sound when it hits
                score_value+=1 # updating score
                break
        for t in targ: #go through each target
            distance = math.sqrt((math.pow(b[0]-t[0],2)) + (math.pow(b[1]-t[1],2)))
            if distance < 30:
                targ.remove(t)#removes the target
                bull.remove(b)#removes the bullet
                explosion_sound.play()
                score_value += 1
                if score_value==10:# condition to change level
                    level_2()
                elif score_value==30:# condition to change level
                    level_3()
                elif score_value==60:# condition to finish game
                    gamefinish()
                break #breaks out of this loop to continue rechecking if bullet hits targets

#this function will check whether any alien bullets hit space ship
def checkalienbullets(alienbull):
    global livesr
    global score_value
    for a in alienbull:
        alienbdistance=math.sqrt((math.pow(a[0]-shipx,2)) + (math.pow(a[1]-shipy,2)))
        if alienbdistance<40: # if it hits
            livesr-=1 # decrease live
            print(livesr)
            if livesr==0: # if no more live then game over
                game_over()
                
                

#this function will define movement of space ship bullet
def moveBullets(bull):
    for b in bull:
        b[0]+=b[2]
        b[1]+=b[3]
        if b[1]>700:#off-screen
            bull.remove(b)

#this function will define movement of space alien bullet
def move_alien_bull(ebull):
    for e in ebull:
        e[0]+=e[2]
        e[1]+=e[3]
        if e[1]>700:#off-screen
            ebull.remove(e)

# this function will run once level 2 starts, its practically the same as level_3() and gameLoop()
def level_2():
    global asteroids
    global alien
    global aliencounter
    global alienbullets
    global shipx
    global shipy
    global current_level
    global livesr
    global score_value
    global enemy_y
    global astroidY 
    global astroidY_change
    global bullets

    asteriodY_change=0
    rapidbullet=40
    y=0
    alien=[]
    ship_x =0
    alienbullets=[]
    ship_y=0 
    current_level+=1
    livesr+=1
    direction= None
    running=True

    while running:
        astroidY_change += .5

        for evt in event.get():
            if evt.type==QUIT:
                running=False
                quit()
            if evt.type==KEYDOWN:
                if evt.key == K_LEFT:#if left key is clicked, then it will move 2.5 spaces to the left
                    ship_x = -2.5
                if evt.key == K_RIGHT:#if right key is clicked, then it will move 2.5 spaces to the right
                    ship_x = 2.5

            if evt.type==KEYUP:
                if evt.key == K_LEFT or evt.key == K_RIGHT: 
                    ship_x = 0


        shipx += ship_x#adding the value of 2.5 to where the ship is currently

        
        if shipx <= 0:# if ship goes out of screen 
            shipx = 0#it will not go further
        elif shipx >= 900:
            shipx = 900
           


        # astroid Movement
        astroidY += astroidY_change
        
        if astroidY_change >=650: #when it reaches the bottom of the screen it will reset
           astroidY_change =0    

        
        if rapidbullet<40:#if rapid bullet is less than 40, then it will add 1, imagine it kind of like reloading a weapon, once it reaches 40, then you can shoot
            rapidbullet+=1
        
        keys=key.get_pressed()       
        if keys[32] and rapidbullet==40:#32 is the space key
            bullet_sound.play()#playing bullet sound
 
            bullets.append([shipx,shipy,v[0],v[1]]) #
            rapidbullet=0#rapid bullet resets to zero as it starts "reloading"
        

        if random.randrange(0,6*20) == 1 and score_value<=30:#if a random number from 0 to 180 is equal to 1 and the score is less than 30, than it will continue adding more aliens, if score is 30, then it will move onto next level
            x= randint(50,700)#finding a random number between 50 and 700 and labelling it as x
            y= randint(0,100)#finding a random number between 0 and 100 and labelling it as y
            alien.append([x,y])#appending both values onto the empty alien list
            alienbullets.append([x,y,w[0],w[1]])#appending the alien bullets at the aliens coordinates with the speed listed in the list "w"




        rel_y = y % bg_3.get_rect().width#finding the amount of the background left after blitting it onto the screen
        screen.blit(bg_3,(0,rel_y - bg_3.get_rect().width))#pasting the rest of the width after it finishes its rotation for a smooth background transition
        if rel_y < 700:#if it goes out of screen
            screen.blit(bg_3,(0,rel_y))#blit the 3rd background onto the screen
        y +=1#add 1 to y, this will be the speed at which the background moves.

        if enemy_y >= 600: 
           enemy_y = 0
        #calling multiple functions on the gameLoop to help with checking if the bullet hit, generating the targets, and displaying the scene,stats.  
        show_score(textx,texty)
        show_lives(10,70)
        show_level(10,10)
        moveBullets(bullets)
        move_alien_bull(alienbullets)
        checkHits(bullets,alien,asteroids)
        checkalienbullets(alienbullets)
        drawScene(screen,shipx,shipy,bullets,alienbullets,alien,asteroids) 

        display.update()
        myclock.tick(120)#120 fps
         
    quit()#quits the gameLoop() once done the loop


def level_3():
    enemy_generate()#generate asteroids
    global alien
    global aliencounter
    global alienbullets
    global shipx
    global shipy
    global current_level
    global livesr
    global score_value
    global enemy_y
    global astroidY 
    global astroidY_change
    global bullets
    bullets=[]
    asteriodY_change=0
    rapidbullet=40
    y=0
    alien=[]
    alienbullets=[]
    ship_x =0
    ship_y=0 
    current_level+=1
    livesr=1
    direction= None
    running=True
    function=True
    while running:
        astroidY_change += .5
        
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                quit()
            if evt.type==KEYDOWN:
                if evt.key == K_LEFT:
                    ship_x = -2.5
                if evt.key == K_RIGHT:
                    ship_x = 2.5

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

        
        if rapidbullet<40:
            rapidbullet+=1
        
        keys=key.get_pressed()       
        if keys[32] and rapidbullet==40:#32 is the space key
            bullet_sound.play()
 
            bullets.append([shipx,shipy,v[0],v[1]]) 
            rapidbullet=0
        
        
        if random.randrange(0,6*15) == 1 and score_value<=60:
            aliencounter+=1
            x= randint(50,700)
            y= randint(0,100)
            alien.append([x,y])
            alienbullets.append([x,y,w[0],w[1]])




        rel_y = y % bg_3.get_rect().width
        screen.blit(bg_3,(0,rel_y - bg_3.get_rect().width))
        if rel_y < 700:
            screen.blit(bg_3,(0,rel_y))
        y +=1

        if enemy_y >= 600: 
           enemy_y = 0
           
        show_score(textx,texty)#calling function to show score
        show_lives(10,70)#calling function to show lives
        show_level(10,10)#calling function to show level
        moveBullets(bullets)#calling function to move bullet
        move_alien_bull(alienbullets)#calling function to move alien bullet
        checkHits(bullets,alien,asteroids)#calling function to check hits
        checkalienbullets(alienbullets)#calling function to check alien bullets
        drawScene(screen,shipx,shipy,bullets,alienbullets,alien,asteroids) #calling function to draw screen

        display.update()
        myclock.tick(120)
         
    quit()

#this function will run when a score of 60 is reached.
def gamefinish():
    global alien
    global alienbullets
    global livesr
    global score_value
    global shipx
    global shipy
    global current_level
    global aliencounter
    global asteroids
    global bullets
    


    bg_sound.stop()#stops the background music
    
    gameDisplay = display.set_mode((1000,700))
    over = image.load('./image/gamewon.jpg').convert_alpha()#pasting a game won screen on the display
    gameDisplay.blit(over,(0,0))

    gamewin = True

    while gamewin:
        for evt in event.get():
            if evt.type == QUIT:
                gamewin=False
                quit()
                

        button("QUIT", 550,500,100,50, red, light_red, action ="Quit")#buttons showing the options of either quitting or going back into mennu, actions are listed as "quit" or "back"
        button("MENU", 310,500,100,50, red, light_red, action ="Back")
        show_score(430,420)#shows your score at the position (430,420)

        display.update()

        myclock.tick(15)#15 fps


    

            

#this is the main game loop that runs for the 1st level
def gameLoop():
    
    gameover=False
    bg_sound.play(-1)#plays the music
    rapidbullet=40#bullet speed at 40
    global shipx
    global shipy
    global aliencounter
    global astroidY 
    global astroidY_change
    global enemy_y
    global alien
    global alienbullets
    global current_level
    global bullets
    global score_value
    global bullets
    bullets=[]
    livesr=1
    y=0
    alien=[]
    aliencounter=0
    alienbullets=[]
    score_value=0
    ship_x =0
    ship_y=0

    current_level=1
    direction= None
    running=True
    function=True
    

    while running:
        astroidY_change += .5
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                quit()
            if evt.type==KEYDOWN:
                if evt.key == K_LEFT:
                    ship_x = -2.5
                if evt.key == K_RIGHT:
                    ship_x = 2.5
            if evt.type==KEYUP:
                if evt.key == K_LEFT or evt.key == K_RIGHT: 
                    ship_x = 0

        shipx += ship_x
        
        if shipx <= 0: 
            shipx = 0
        elif shipx >= 900:
            shipx = 900



        # astroid Movement
        astroidY += astroidY_change
        
        if astroidY_change >=650: 
           astroidY_change =0 # initilizing astroid position if it reaches the outside of the screen   

        
        if rapidbullet<40:
            rapidbullet+=1
        
        keys=key.get_pressed()       
        if keys[32] and rapidbullet==40:#32 is the space key
            bullet_sound.play()#bullet sound is played
 
            bullets.append([shipx,shipy,v[0],v[1]]) 
            rapidbullet=0
        
        
        if random.randrange(0,6*30) == 1 and score_value<=10:
            aliencounter+=1
            x= randint(50,700)
            y= randint(0,100)
            alien.append([x,y])
            alienbullets.append([x,y,w[0],w[1]])



        rel_y = y % bg_3.get_rect().width
        screen.blit(bg_3,(0,rel_y - bg_3.get_rect().width))
        if rel_y < 700:
            screen.blit(bg_3,(0,rel_y))
        y +=1

        if enemy_y >= 600: 
           enemy_y = 0
           
        show_score(textx,texty)
        show_lives(10,70)
        show_level(10,10)
        moveBullets(bullets)
        move_alien_bull(alienbullets)
        checkHits(bullets,alien,asteroids)
        checkalienbullets(alienbullets)
        drawScene(screen,shipx,shipy,bullets,alienbullets,alien,asteroids) 

        display.update()
        myclock.tick(120)
         
    quit()

game_intro()#first function being called, this is the title menu













