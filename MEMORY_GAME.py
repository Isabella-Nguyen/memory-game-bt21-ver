##################################################### MEMORY GAME - HOUSE OF CARDS #################################################################
################################################### SUMMATIVE GAME BY ISABELLA NGUYEN ##############################################################
########################################################### ICS3U | SPRING 2020 ####################################################################


################################# START CODE #################################
import pygame
import time
from sys import exit
import random
pygame.init()
display=pygame.display.set_mode((1000,650))
pygame.display.set_caption('HOUSE OF CARDS')

#Colours
white=(255,255,255)
black=(0,0,0)
purple=	(147,112,219)
blue=(176,196,222)
darkblue=(119,136,153)

#Fonts
subfont=pygame.font.SysFont("inkfree",20)
subtitlefont=pygame.font.SysFont("britannic",65)
titlefont = pygame.font.SysFont("britannic", 72)
buttonfont = pygame.font.SysFont("britannic", 40)
nextfont = pygame.font.SysFont("britannic",30)
words = pygame.font.SysFont("inkfree",35)
smallfont = pygame.font.SysFont("inkfree",27)
questfont = pygame.font.SysFont("inkfree",40)

#While/if variables
running=True
playing=True
reading_instructions=True
gaming=True
PickingCard1=True
finished=False
started=False
settings=False

#Coordinate tuples for drawing all 15 cards and for detecting mouse clicks and motion
minx=(195,325,455,585,715,195,325,455,585,715,195,325,455,585,715)
miny=(170,170,170,170,170,320,320,320,320,320,470,470,470,470,470)
maxx=(285,415,545,675,805,285,415,545,675,805,285,415,545,675,805)
maxy=(300,300,300,300,300,450,450,450,450,450,600,600,600,600,600)

#Tuples for the settings coordinates and words
snx= (415,440,437,417) #n=min coordinate #x=max coordinate
sxx= (588,558,563,584)
sny= (220,280,340,400)
sxy= (250,310,375,430)
swords= ("- Restart -","- Quit -","- Help -","- Cancel -")
scoord= ((415,215),(440,275),(437,335),(417,395))
erase= ((414,215,200,50),(439,275,200,50),(436,335,200,50),(416,395,200,50))

#Lists for keeping track of different matches and cards picked
CardsList=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7]
MatchedList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
CorrectList=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Picked=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Variables for matches
card=-1 #value of card
pick=-1 #which card on the board
card1=-1 
pick1=-1
card2=-1
pick2=-1

#Variable for moves
smoves=""
moves=0

#Image Tuple for cards
ImageTuple=('RJ_card.jpg','chimmy_card.jpg','cooky_card.jpg','koya_card.jpg','shooky_card.jpg','mang_card.jpg','tata_card.jpg','bomb2.jpg')

################## DEFINITIONS #######################################################

def titlepage ():
    display.fill(blue) #background

    rectangle=pygame.Rect(65,370,895,130) #WHITE RECTANGLE
    pygame.draw.rect(display,(white),rectangle)
    
    title = titlefont.render("House of Cards", True, (darkblue))#TITLE
    display.blit(title, (265, 405))

    TitleImage=('titlePhoto.png')#IMAGE
    image=pygame.image.load(TitleImage)
    display.blit(image,(5,10))

    PlayButton=pygame.Rect(415,530,170,80) #PLAY BUTTON RECTANGLE
    pygame.draw.rect(display,(darkblue),PlayButton)

    PLAY = buttonfont.render("PLAY", True, (black))#PLAY BUTTON TEXT
    display.blit(PLAY, (457, 550))
    
    pygame.display.update()

def instructions():
    display.fill(blue)
    whiteback=pygame.Rect(50,50,900,550) #WHITE RECTANGLE BACKGROUND
    pygame.draw.rect(display,(white),whiteback)

    instructions=subtitlefont.render("INSTRUCTIONS: ", True, (black))#TITLE: INSTRUCTIONS
    display.blit(instructions,(70,70))

    #THE NEXT FEW LINES ARE WRITING THE INSTRUCTIONS
    text=subfont.render("Objective: Find all 7 pairs without picking the bomb!", True, (black))
    display.blit(text,(70,150))
    text=subfont.render("Pick two cards by clicking on them. If they are not a match, the cards you chose will be", True, (black))
    display.blit(text,(70,200))
    text=subfont.render("flipped over again. You will keep picking pairs until all matches are found.", True, (black))
    display.blit(text,(70,230))
    text=subfont.render("BUT! BE CAREFUL!!! There is one card that is a bomb. If you choose that card,", True, (black))
    display.blit(text,(70,280))
    text=subfont.render("ALL the cards will be flipped over again and you will have to restart!", True, (black))
    display.blit(text,(70,310))
    text=subfont.render("Avoid the bomb! GOOD LUCK!!!", True, (black))
    display.blit(text,(70,360))

    nextbutton=pygame.Rect(70,420,110,50) #NEXT BUTTON RECTANGLE
    pygame.draw.rect(display,(blue),nextbutton)

    instructionsImage=('instructionspic.jpg')#IMAGE
    image=pygame.image.load(instructionsImage)
    display.blit(image,(210,405))

def game_page():
    display.fill(blue)

    whiteback=pygame.Rect(165,140,670,490) #WHITE RECTANGLE BACKGROUND
    pygame.draw.rect(display,(white),whiteback)

    for i in range(15): #Draw 15 cards using the tuples
        rectangle=pygame.Rect(minx[i],miny[i],90,130)
        pygame.draw.rect(display,(purple),rectangle)

    title=subtitlefont.render("House of Cards", True, (black)) #WRITE "HOUSE OF CARDS"
    display.blit(title, (270, 15))

    MOVES=subfont.render("Moves:", True, (black)) #WRITE "Moves:"
    display.blit(MOVES, (820, 75))

    settingslogo=pygame.image.load('settingsicon_.png') #IMPORT SETTINGS LOGO
    display.blit(settingslogo,(15,15))

    #PICTURES ON THE SIDES
    Mang=('Mang.png')
    image=pygame.image.load(Mang)
    display.blit(image,(85,230))

    Chimmy=('Chimmy.png')
    image=pygame.image.load(Chimmy)
    display.blit(image,(650,60))

    Shooky=('Shooky.png')
    image=pygame.image.load(Shooky)
    display.blit(image,(890,385))

    TaTa=('tata.png')
    image=pygame.image.load(TaTa)
    display.blit(image,(15,440))

    Koya=('Koya.png')
    image=pygame.image.load(Koya)
    display.blit(image,(145,25))

    RJ=('RJ.png')
    image=pygame.image.load(RJ)
    display.blit(image,(825,200))

    Cooky=('Cooky.png')
    image=pygame.image.load(Cooky)
    display.blit(image,(870,460))

def bomb():
    rectangle=pygame.Rect(300,85,350,55)
    pygame.draw.rect(display,(blue),rectangle)
    BOMB=smallfont.render("YOU GOT THE BOMB!", True, (black)) #WRITE "YOU GOT THE BOMB!"
    display.blit(BOMB, (335, 90))
    pygame.display.update()
    
    time.sleep(0.8)#delay 0.8 seconds before redrawing all the cards
    for i in range(15): #REDRAW ALL CARDS
        rectangle=pygame.Rect(minx[i],miny[i],90,130)
        pygame.draw.rect(display,(purple),rectangle)
        pygame.display.update()
        MatchedList[i]=0 #RESET MATCHES

    rectangle=pygame.Rect(300,85,350,55) 
    pygame.draw.rect(display,(blue),rectangle)
    Pickacard=words.render("Pick a card", True, (black)) #WRITE "pick a card"
    display.blit(Pickacard, (390, 85))
    pygame.display.update()

def winning_screen():
    display.fill(blue)
    whiteback=pygame.Rect(50,50,900,550) #WHITE RECTANGLE BACKGROUND
    pygame.draw.rect(display,(white),whiteback)

    win=subtitlefont.render("CONGRATULATIONS!", True, (black)) #WRITE "CONGRATULATIONS"
    display.blit(win, (210, 70))

    image=pygame.image.load('closing_pic.jpg') #OUTPUT IMAGE
    display.blit(image,(80,140))
    
    againButton=pygame.Rect(665,290,150,70) #PLAY AGAIN BUTTON RECTANGLE
    pygame.draw.rect(display,(blue),againButton)

    again = nextfont.render("Play again", True, (black))#PLAY AGAIN BUTTON TEXT
    display.blit(again, (673, 310))

    noButton=pygame.Rect(665,390,150,70) #QUIT BUTTON RECTANGLE
    pygame.draw.rect(display,(blue),noButton)

    quitt = buttonfont.render("Quit", True, (black))#QUIT BUTTON TEXT
    display.blit(quitt, (704, 403))

    MOVES=buttonfont.render("Moves:", True, (black)) #WRITE "Moves: "
    display.blit(MOVES, (647, 220))

    nummoves=buttonfont.render(smoves,True,(black))
    display.blit(nummoves, (772, 220)) #WRITE THE MOVES

def settings_page():
    backrect = pygame.Surface((1000,650)) #DRAW A WHITE RECTANGLE THAT IS SLIGHTLY TRANSPARENT BEHIND THE SETTINGS MENU
    backrect.set_alpha(170)
    backrect.fill((white))
    display.blit(backrect, (0,0))
    
    settingsrect=pygame.Rect(325,100,350,450) #SETTINGS RECTANGLE
    pygame.draw.rect(display,(blue),settingsrect)
    settingsrectb=pygame.Rect(325,100,350,450) #SETTINGS RECTANGLE BORDER
    pygame.draw.rect(display,(black),settingsrectb,width=7)

    for i in range(4):
        restart=buttonfont.render(swords[i],True,(black)) #WRITE THE SETTINGS OPTIONS USING THE TUPLES
        display.blit(restart,scoord[i])

    settingsT=subtitlefont.render("Settings", True, (black)) #SETTINGS TEXT
    display.blit(settingsT, (385,125))

    settingspic=('settings_pic.png') #IMAGE
    image=pygame.image.load(settingspic)
    display.blit(image,(515,448))
    
    pygame.display.update()


####################### END OF DEFINITIONS ####################################################################

####################### GAME CODE #############################################################################

################ TITLE PAGE ######################
titlepage()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #QUIT
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION: #DRAW A BORDER OVER PLAY BUTTON WHEN MOUSE IS ON THE BUTTON
            pos = pygame.mouse.get_pos()
            mousex=pos[0]
            mousey=pos[1]
            if mousex>=415 and mousex<=585 and mousey>=530 and mousey<=610: #WHEN MOUSE IS HOVERING ON BUTTON
                PlayOutline=pygame.Rect(415,530,170,80)
                pygame.draw.rect(display,(black),PlayOutline,width=3)
                pygame.display.update()
            else: #WHEN MOUSE IS NOT ON BUTTON
                noPlayOutline=pygame.Rect(415,530,170,80)
                pygame.draw.rect(display,(darkblue),noPlayOutline,width=3)
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN: #WHEN PLAY BUTTON IS CLICKED RUN PLAY LOOP
            if mousex>=415 and mousex<=585 and mousey>=530 and mousey<=610:
                running=False

############## INSTRUCTIONS ####################
while playing:
    instructions()
    
    if started==False: #CHECK WHETHER USER ALREADY STARTED THE GAME
        START=nextfont.render("START",True,(black))#START BUTTON TEXT
        display.blit(START,(85,430))
    elif started==True:
        BACK=nextfont.render("BACK",True,(black))#BACK BUTTON TEXT
        display.blit(BACK,(90,430))
    
    while reading_instructions: #START INSTRUCTIONS LOOP
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #QUIT
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION: #DRAW A BORDER OVER NEXT BUTTON WHEN MOUSE IS ON THE BUTTON
                pos = pygame.mouse.get_pos()
                mousex=pos[0]
                mousey=pos[1]
                if mousex>=70 and mousex<=180 and mousey>=420 and mousey<=470: #WHEN MOUSE IS HOVERING ON THE BUTTON
                    NextOutline=pygame.Rect(70,420,110,50)
                    pygame.draw.rect(display,(black),NextOutline,width=3)
                else: #WHEN MOUSE IS NOT ON BUTTON
                    noNextOutline=pygame.Rect(70,420,110,50)
                    pygame.draw.rect(display,(blue),noNextOutline,width=3)
            elif event.type == pygame.MOUSEBUTTONDOWN: #WHEN PLAY BUTTON IS CLICKED RUN PLAY LOOP
                if mousex>=70 and mousex<=180 and mousey>=420 and mousey<=470:
                    reading_instructions=False
                    gaming=True
   
############## GAME PAGE ######################
    game_page()

    if started==True: #USER ALREADY STARTED THE GAME
        for i in range(15):
            if MatchedList[i]==1 or Picked[i]==1: #DRAW CARDS ALREADY FLIPPED OVER
                cardImage=pygame.image.load(ImageTuple[CardsList[i]]) #DRAW CARD WITH CORRECT IMAGE
                cardImage=pygame.transform.scale(cardImage,(90,130))
                display.blit(cardImage,(minx[i],miny[i]))
                
        nummoves=subfont.render(smoves,True,(black))
        display.blit(nummoves, (890, 75)) #WRITE THE MOVES

        if PickingCard1==True: #ACCORDING TO WHETHER THE USER IS IN THE MIDDLE OF PICKING THEIR FIRST OR SECOND CARD OF THE MATCH, WRITE THE CORRECT WORDS ON SCREEN
            Pickacard=words.render("Pick a card", True, (black)) #WRITE "Pick a card"
            display.blit(Pickacard, (385, 85))
        elif PickingCard1==False:
            Pickacard=words.render("Pick another card", True, (black)) #WRITE "pick another card"
            display.blit(Pickacard, (350, 85))
        
    elif started==False: #USER IS JUST STARTING THE GAME
        smoves=str(moves)
        nummoves=subfont.render(smoves,True,(black)) #WRITE THE NUMBER OF MOVES (WHICH IS 0 AT THE BEGINNING)
        display.blit(nummoves, (890, 75))
        
        Pickacard=words.render("Pick a card", True, (black)) #WRITE "Pick a card"
        display.blit(Pickacard, (385, 85))
        
        random.shuffle(CardsList) #Shuffle cards list to make the game random
        for i in range(15): #SET BOMB TO 0 IN CORRECT LIST BECAUSE IN ORDER TO WIN YOU CAN'T HAVE THE BOMB CARD FLIPPED
            if CardsList[i]==7:
                CorrectList[i]=0

    for i in range(15):
        nocardOutline=pygame.Rect(minx[i],miny[i],90,130) #DRAW THE PURPLE OUTLINE SO THAT WHEN THE MOUSE MOVES A PURPLE OUTLINE DOESN'T RANDOMLY APPEAR
        pygame.draw.rect(display,(purple),nocardOutline,width=3)
    
    pygame.display.update()    
    started=True #STATE THAT THE GAME HAS STARTED
    
    while gaming: #START GAME PAGE LOOP
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #QUIT
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                mousex=pos[0]
                mousey=pos[1]
                for i in range(15):
                    if mousex>=minx[i] and mousex<=maxx[i] and mousey>=miny[i] and mousey<=maxy[i]: #WHEN MOUSE IS HOVERING OVER A CARD
                        cardOutline=pygame.Rect(minx[i],miny[i],90,130) #DRAW BLACK OUTLINE
                        pygame.draw.rect(display,(black),cardOutline,width=3)
                        pygame.display.update()
                    else: #WHEN MOUSE IS NOT ON A CARD
                        nocardOutline=pygame.Rect(minx[i],miny[i],90,130) #COVER BLACK OUTLINE
                        pygame.draw.rect(display,(purple),nocardOutline,width=3)
                        pygame.display.update()
                if mousex>=19 and mousex<=61 and mousey>=19 and mousey<=61: #WHEN MOUSE IS HOVERING ON SETTINGS ICON
                    settingslogo=pygame.image.load('settingsicon2_.png') #IMPORT GRAY SETTINGS LOGO
                    display.blit(settingslogo,(15,15))
                    pygame.display.update()
                else:
                    settingslogo=pygame.image.load('settingsicon_.png') #IMPORT BLACK SETTINGS LOGO
                    display.blit(settingslogo,(15,15))
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONDOWN: #### DETERMINING THE CARD ####
                for i in range(15):
                    if mousex>=minx[i] and mousex<=maxx[i] and mousey>=miny[i] and mousey<=maxy[i] and MatchedList[i]==0 and Picked[i]==0: #WHEN A CARD IS CLICKED THAT HAS NOT ALREADY BEEN MATCHED OR PICKED
                        pick=i #REMEMBER WHAT CARD WAS CLICKED
                        card=CardsList[i] #REMEMBER WHAT THE VALUE OF THE CARD IS

                        Picked[i]=1 #RECORD WHAT CARD WAS JUST PICKED SO THAT THE USER CANNOT PICK THAT CARD AGAIN
                        
                        cardImage=pygame.image.load(ImageTuple[card]) #DRAW CARD WITH CORRECT IMAGE
                        cardImage=pygame.transform.scale(cardImage,(90,130))
                        display.blit(cardImage,(minx[pick],miny[pick]))
                        pygame.display.update()

                        if PickingCard1==True: #PICKING THE FIRST CARD
                            card1=card
                            pick1=pick
                            PickingCard1=False
                            
                            if card1==7: ##### BOMB ######
                                moves+=1 #ADD ONE MOVE
                                smoves=str(moves) #CONVERT INT TO STRING TO DISPLAY IT
                                nummoves=subfont.render(smoves,True,(black))
                                rectangle=pygame.Rect(889,74,50,30) #ERASE THE OTHER MOVES
                                pygame.draw.rect(display,(blue),rectangle) 
                                display.blit(nummoves, (890, 75)) #WRITE THE MOVES
                                pygame.display.update()
                                
                                bomb()
                                PickingCard1=True
                                for i in range(15): #RESET PICKED CARDS
                                     Picked[i]=0
                                
                            else:
                                rectangle=pygame.Rect(300,85,350,55) #ERASE THE OTHER WORDS
                                pygame.draw.rect(display,(blue),rectangle)
                                Pickacard=words.render("Pick another card", True, (black)) #WRITE "pick another card"
                                display.blit(Pickacard, (350, 85))
                                pygame.display.update()
                        
                        elif PickingCard1==False: #PICKING THE SECOND CARD
                            card2=card
                            pick2=pick
                            
                            moves+=1 #ADD ONE MOVE
                            smoves=str(moves) #CONVERT INT TO STRING TO DISPLAY IT
                            nummoves=subfont.render(smoves,True,(black))
                            rectangle=pygame.Rect(889,74,50,30) #ERASE THE OTHER MOVES
                            pygame.draw.rect(display,(blue),rectangle) 
                            display.blit(nummoves, (890, 75)) #WRITE THE MOVES
                            
                            PickingCard1=True
                            if card1==card2: #CHECK IF USER GOT A MATCH
                                MatchedList[pick1]=1 #RECORD THE MATCHES
                                MatchedList[pick2]=1
                                if MatchedList==CorrectList: #IF THE USER WON
                                    rectangle=pygame.Rect(300,85,350,55) #ERASE THE WORDS AT THE TOP
                                    pygame.draw.rect(display,(blue),rectangle)
                                    
                                    bombimage=pygame.image.load(ImageTuple[7])
                                    bombimage=pygame.transform.scale(bombimage,(90,130)) #BOMB IMAGE
                                    bombloca=CardsList.index(7) #FIND WHICH CARD IS THE BOMB
                                    display.blit(bombimage,(minx[bombloca],miny[bombloca])) #OUTPUT THE IMAGE ON THE CORRECT CARD
                                    time.sleep(0.3) #SLIGHT DELAY TO MAKE IT LOOK SMOOTHER
                                    pygame.display.update()
                                    time.sleep(0.8) #DELAY

                                    for i in range (15):
                                        rectangle=pygame.Rect(minx[i],miny[i],90,130)
                                        pygame.draw.rect(display,(purple),rectangle)
                                    pygame.display.update()
                                    time.sleep(0.8)
                                    
                                    winn=titlefont.render("YOU WIN!!!", True, (black)) #WRITE "YOU WIN!!!"
                                    display.blit(winn, (320, 320))
                                    pygame.display.update()
                                    time.sleep(1) #DELAY
                                    
                                    gaming=False #GET OUT OF THE GAMING LOOP AND SHOW THE WINNING PAGE
                                    finished=True 
                                else: #IF THE USER DID NOT WIN BUT STILL GOT A MATCH
                                    rectangle=pygame.Rect(300,85,350,55)
                                    pygame.draw.rect(display,(blue),rectangle)
                                    congrats=smallfont.render("Congrats! You got a match!", True, (black)) #WRITE "Congrats! You got a match!"
                                    display.blit(congrats, (315, 90))
                                    pygame.display.update()
                                    
                                    time.sleep(0.8) #DELAY
                                    
                                    rectangle=pygame.Rect(300,85,350,55)
                                    pygame.draw.rect(display,(blue),rectangle)
                                    Pickacard=words.render("Pick a card", True, (black)) #WRITE "pick a card"
                                    display.blit(Pickacard, (390, 85))
                                    pygame.display.update()
                                
                            elif card2==7: ###### BOMB ######
                                bomb()
                                PickingCard1=True
                                for i in range(15): #RESET PICKED CARDS
                                    Picked[i]=0
                                    
                            else:
                                rectangle=pygame.Rect(300,85,350,55)
                                pygame.draw.rect(display,(blue),rectangle)
                                congrats=words.render("Try again", True, (black)) #WRITE "try again"
                                display.blit(congrats, (390, 85))
                                pygame.display.update()
                                
                                time.sleep(0.8) #DELAY
                                
                                rectangle=pygame.Rect(minx[pick1],miny[pick1],90,130) #REDRAW CARDS CHOSEN
                                pygame.draw.rect(display,(purple),rectangle)
                                rectangle=pygame.Rect(minx[pick2],miny[pick2],90,130)
                                pygame.draw.rect(display,(purple),rectangle)
                                
                                rectangle=pygame.Rect(300,85,350,55)
                                pygame.draw.rect(display,(blue),rectangle)
                                Pickacard=words.render("Pick a card", True, (black)) #WRITE "pick a card"
                                display.blit(Pickacard, (390, 85))
                                pygame.display.update()
                                for i in range(15): #RESET PICKED CARDS
                                    Picked[i]=0
                    elif mousex>=15 and mousex<=65 and mousey>=15 and mousey<=65: #IF THE SETTINGS BUTTON IS CLICKED
                        settings=True
                        gaming=False

############## SETTINGS #######################
    settings_page()
    while settings: #SETTINGS LOOP
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #QUIT
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                mousex=pos[0]
                mousey=pos[1]
                for i in range(4):
                    if mousex>=snx[i] and mousex<=sxx[i] and mousey>=sny[i] and mousey<=sxy[i]: #IF THE MOUSE IS HOVERING ON ONE OF THE WORDS
                        rectangle=pygame.Rect(erase[i]) #ERASE THE OTHER WORDS
                        pygame.draw.rect(display,(blue),rectangle)
                        restart=buttonfont.render(swords[i],True,(purple)) #WRITE THE CORRECT WORD IN PURPLE
                        display.blit(restart,scoord[i])
                    else: #THE MOUSE IS NOT ON ANY OF THE WORDS
                        rectangle=pygame.Rect(erase[i]) #ERASE THE OTHER WORDS
                        pygame.draw.rect(display,(blue),rectangle)
                        restart=buttonfont.render(swords[i],True,(black)) #WRITE THE CORRECT WORD IN BLACK
                        display.blit(restart,scoord[i])
            elif event.type==pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if mousex>=snx[i] and mousex<=sxx[i] and mousey>=sny[i] and mousey<=sxy[i]: #IF ONE OF THE WORDS ARE CLICKED
                        if i==0: #RESTART
                            MatchedList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #INITIALIZE EVERYTHING
                            CorrectList=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                            Picked=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                            card=-1
                            pick=-1
                            card1=-1
                            pick1=-1
                            card2=-1
                            pick2=-1
                            moves=0
                            PickingCard1=True
                            started=False
                            gaming=False
                            settings=False
                            reading_instructions=True
                        elif i==1: #QUIT
                            pygame.quit()
                            exit()
                        elif i==2: #HELP/INSTRUCTIONS
                            settings=False
                            reading_instructions=True
                        elif i==3: #CANCEL/ GO BACK TO GAME
                            settings=False
                            gaming=True


################# WINNING PAGE ######################
    winning_screen()
    while finished:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #QUIT
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if mousex>=665 and mousex<=815 and mousey>=390 and mousey<=460: #QUIT BY QUIT BUTTON
                    pygame.quit()
                    exit()
                elif mousex>=665 and mousex<=815 and mousey>=290 and mousey<=360: #PLAY AGAIN/RETURN TO INSTRUCTIONS PAGE
                    MatchedList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #INITIALIZE EVERYTHING
                    CorrectList=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                    Picked=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    card=-1
                    pick=-1
                    card1=-1
                    pick1=-1
                    card2=-1
                    pick2=-1
                    moves=0
                    PickingCard1=True
                    started=False
                    finished=False
                    reading_instructions=True #GO BACK TO INSTRUCTIONS
            elif event.type == pygame.MOUSEMOTION: #DRAW A BORDER OVER PLAY BUTTON WHEN MOUSE IS ON THE BUTTON
                pos = pygame.mouse.get_pos()
                mousex=pos[0]
                mousey=pos[1]
                if mousex>=665 and mousex<=815 and mousey>=290 and mousey<=360: #WHEN MOUSE IS HOVERING ON PLAY AGAIN BUTTON
                    againOutline=pygame.Rect(665,290,150,70)
                    pygame.draw.rect(display,(black),againOutline,width=3)
                else: #WHEN MOUSE IS NOT ON BUTTON
                    noagainOutline=pygame.Rect(665,290,150,70)
                    pygame.draw.rect(display,(blue),noagainOutline,width=3)
                if mousex>=665 and mousex<=815 and mousey>=390 and mousey<=460: #WHEN MOUSE IS HOVERING ON QUIT BUTTON
                    QuitOutline=pygame.Rect(665,390,150,70)
                    pygame.draw.rect(display,(black),QuitOutline,width=3)
                else: #WHEN MOUSE IS NOT ON BUTTON
                    noQuitOutline=pygame.Rect(665,390,150,70)
                    pygame.draw.rect(display,(blue),noQuitOutline,width=3)

                    





                        
