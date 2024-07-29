# thu vien game
import pygame, sys, threading
import pygame_gui
from button import Button
from pyvidplayer import Video

pygame.init()
# tieu de va icon
pygame.display.set_caption("CARO SQR")
icon = pygame.image.load(r'assets/eww.jpg')
pygame.display.set_icon(icon)

# cua so game

#question_screen = pygame.display.set_mode((300,270))
screen = pygame.display.set_mode((1280,720))
WIDTH, HEIGHT = 1280, 720
#bg
bg=pygame.image.load(r'assets/mainmenu.png')
bg=pygame.transform.scale(bg,(1280,720))
win_bg=pygame.image.load('assets/winner_background3.png')
win_bg=pygame.transform.scale(win_bg,(1280,720))
question_bg = pygame.image.load(r'assets/exit_question.png')
banco=pygame.image.load(r'assets/tempboard.png')
#banco=pygame.transform.scale(banco,(1280,720))
cox=pygame.image.load(r'assets/x.png')
coo=pygame.image.load(r'assets/o.png')
xwin=pygame.image.load(r'assets/XWIN.png')
owin=pygame.image.load(r'assets/OWIN.png')
nenbanco=pygame.image.load(r'assets/background.png')
nenbanco=pygame.transform.scale(nenbanco,(1280,720))
settingbg=pygame.image.load(r'assets/settingbg.png')
settingbg=pygame.transform.scale(settingbg,(1280,720))
pt=pygame.image.load(r'assets/1151373.png')
pt=pygame.transform.scale(pt,(1280,720))
won = False
# fps
clock = pygame.time.Clock()
#music 
nhac = pygame.mixer.Sound('music/game.wav')
#nhac.play(loops = -1)

time_skip= 600

#text input

manager1 = pygame_gui.UIManager((1280, 720))
manager2 = pygame_gui.UIManager((1280, 720))
name_1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((500, 400), (300, 50)), manager=manager1,
                                               object_id='#main_text_entry')

name_2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((500, 400), (300, 50)), manager=manager2,
                                               object_id='#main_text_entry')



# Loading BG
LOADING_BG = pygame.image.load("assets/Loading Bar Background.png")
#LOADING_BG=pygame.transform.scale(LOADING_BG,(771,100))
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))
# Loading Bar and variables
loading_bar = pygame.image.load("assets/Loading Bar.png")
#loading_bar=pygame.transform.scale(loading_bar,(5,40))
loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8
# Work
WORK = 10000000

ok_play = True
ok_about = True
ok_setting =True
wide = 54
time_win=0
def intro():
    global time_skip
    vid = Video("music/intro vcl wtf.mp4")
    vid.set_size((1280,720))
    while True:
        vid.draw(screen, (0,0))
        SKIP_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(70, 40), 
                            text_input="SKIP", font=get_font(30), base_color="White", hovering_color="red")

        PLAY_BACK.changeColor(SKIP_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_question()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(SKIP_MOUSE_POS):
                    vid.close()
                    nhac.play(loops = -1)
                    main()    
        time_skip -= 1
        if time_skip <=0:
            
            vid.close()
            nhac.play(loops = -1)
            main() 
        clock.tick(60)
        pygame.display.update()
     

def doWork():
	# Do some math WORK amount times
	global loading_finished, loading_progress

	for i in range(WORK):
		math_equation = 523687 / 789456 * 89456
		loading_progress = i 
	loading_finished = True
# Finished text
FONT = pygame.font.SysFont("Roboto", 100)
finished = FONT.render("Done!", True, "white")
finished_rect = finished.get_rect(center=(640, 360))

ham =0
board = [[0,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]]

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/NeonTubes2.otf", size)
# Thread
#threading.Thread(target=doWork).start()

def ld():
    global ham
    global loading_finished
    threading.Thread(target=doWork).start()
    while True:
        global loading_bar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_question()

        screen.fill("#0d0e2e")
        if not loading_finished:
            loading_bar_width = loading_progress / WORK * 720
            loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
            loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
            screen.blit(LOADING_BG, LOADING_BG_RECT)
            screen.blit(loading_bar, loading_bar_rect)
        else:
            if(ham == 1):
                play()
            else:
                if ham == 2:
                    about()
                elif ham==3:
                    setting()     
        pygame.display.update()
        clock.tick(120)



def AI():
    while True:
        screen.blit(bg, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="cyan", hovering_color="hotpink")
        comingsoon = Button(image=None, pos=(640, 400), 
                                    text_input="COMING SOON", font=get_font(100), base_color="cyan", hovering_color="hotpink")
                                     
        for button in [comingsoon,  PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_question()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):                        
                        play()
        clock.tick(120)
        pygame.display.update()

        
def play():
    
    global ok_play
    global loading_finished
    while True:
        if ok_play:
            ok_play=False
            ld()
        else:
            screen.blit(bg, (0, 0))

            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            AI_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                                text_input="VS AI", font=get_font(30), base_color="#d7fcd4", hovering_color="hotpink")
            PVP_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 420), 
                                text_input="PVP", font=get_font(30), base_color="#d7fcd4", hovering_color="hotpink")
            PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="cyan", hovering_color="hotpink")

            for button in [AI_BUTTON, PVP_BUTTON ,PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_question()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        ok_play =True
                        loading_finished = False
                        main()
                    if PVP_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        get_user_name1()
                    if AI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        AI()
        clock.tick(120)
        pygame.display.update()

def about():
    global ok_about
    global loading_finished
    while True:
        if ok_about:
            ok_about = False
            ld()
        else:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            screen.blit(pt, (0, 0))

            PLAY_TEXT = get_font(20).render("y", True, "red")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            screen.blit(PLAY_TEXT, PLAY_RECT)
            PLAY_BACK = Button(image=None, pos=(110, 40), 
                                text_input="BACK", font=get_font(30), base_color="cyan", hovering_color="hotpink")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_question()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        ok_about =True
                        loading_finished = False
                        main()
        clock.tick(120)
        pygame.display.update()

on_off_music=True

def domusic():
    global on_off_music
    if on_off_music == True:
        on_off_music = False
        nhac.stop()
    else:
        on_off_music = True
        nhac.play(loops= -1)

def setting():
    global ok_setting
    global loading_finished
    global base_turn

    while True:
        if ok_setting:
            ok_setting = False
            ld()
        else:
            screen.blit(settingbg, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            if on_off_music == True:
                music_tam="assets/soundON.png"
            else:
                music_tam ="assets/soundOFF.png"

            if base_turn == 0:
                XO_tam = "assets/X.png"
            else:
                XO_tam = "assets/O.png"



            SETTING_BACK = Button(image=pygame.image.load("assets/HOME.png"), pos=(660, 520), 
                                    text_input=None, font=get_font(30), base_color="cyan", hovering_color="hotpink")

            MUSIC_BUTTON = Button(image=None, pos=(540, 300), 
                                    text_input="MUSIC", font=get_font(30), base_color="cyan", hovering_color="hotpink")
            ON_OFF_BUTTON = Button(image=pygame.image.load(music_tam), pos=(750, 300), 
                                    text_input=None, font=get_font(15), base_color="cyan", hovering_color="hotpink")

            XO_BUTTON = Button(image=None, pos=(540, 400), 
                                    text_input="X/O", font=get_font(30), base_color="cyan", hovering_color="hotpink")
            ON_OFF_XO_BUTTON = Button(image=pygame.image.load(XO_tam), pos=(750, 400), 
                                    text_input=None, font=get_font(15), base_color="cyan", hovering_color="hotpink")

            for button in [SETTING_BACK, ON_OFF_BUTTON, ON_OFF_XO_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)

            MUSIC_BUTTON.update(screen)
            XO_BUTTON.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit_question()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if SETTING_BACK.checkForInput(PLAY_MOUSE_POS):
                            ok_setting =True
                            loading_finished = False
                            main()
                        if ON_OFF_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            domusic()
                        if ON_OFF_XO_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            base_turn=(base_turn+1)%2
        clock.tick(120)
        
        pygame.display.update()

def checkxy(x,y,z):
    l=370 #goc.x
    r=100 #goc.y
    
    for i in range(10):
        for j in range(10):
            if x > (i*wide + l) and x < ( ( i +1) * wide + l)  and  y > (j*wide + r)  and y <(j*wide + wide + r) and board[i+1][j+1]==0:
                board[i+1][j+1]=z+1
                return True
    return False

def inxo():
    for i in range(10):
        for j in range(10):
            if board[i+1][j+1] == 1:
                screen.blit(cox,(370+i*wide+5, 5+100+j*wide))
            if board[i+1][j+1] == 2:
                screen.blit(coo,(370+i*wide+5, 5+ 100+j*wide))
            if board[i+1][j+1] == 3:
                screen.blit(xwin,(370+i*wide+5, 5+100+j*wide))
            if board[i+1][j+1] == 4:
                screen.blit(owin,(370+i*wide+5, 5+ 100+j*wide))

            
                
def reset():
    global turn
    global base_turn
    global board
    global time_win
    global won
    won = False
    time_win=0
    turn = base_turn
    board = [[0,0,0,0,0,0,0,0,0,0,0,0], 
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0]]
    #screen.blit(nenbanco, (0, 0)) 
    #screen.blit(banco, (370, 100)) 
    inxo()


base_turn = 0
turn = 0
kanna1="assets/kanna1.png"
kanna2="assets/kanna2.png"
kanna3="assets/kanna3.png"
goku1 = "assets/goku1.png"
goku2 = "assets/goku2.png"
muiten=pygame.image.load("assets/muiten.png")
kanna_turn=0
goku_turn = 0
muiten_x = 120
muiten_y=90
muiten_move= 20

def check_win():
    for p in range (1, 3): # check lan luot x, o
        #check row
        for i in range(0, 11):
            cnt=0
            for j in range(0, 11):
                if board[i][j]==p:
                    cnt+=1
                else:
                    cnt=0
                if cnt==5:
                    for t in range(j-5+1,j+1):
                        board[i][t]=p+2
                    return p
        #check col
        for j in range(11):
            cnt=0
            for i in range(0, 11):
                if board[i][j]==p:
                    cnt+=1
                else:
                    cnt=0
                if cnt==5:
                    for t in range(i-5+1,i+1):
                        board[t][j]=p+2
                    return p
        #check cheo chinh
        for i in range(0, 8):
            for j in range(0, 8):
                ok=True
                for t in range(0, 5):
                    if board[i+t][j+t]!=p:
                        ok=False
                        break
                if ok==True:
                    for t in range(0, 5):
                        board[i+t][j+t]=p+2
                    return p
        #check cheo phu
        for i in range(0, 8):
            for j in range(0, 8):
                ok=True
                for t in range(0, 5):
                    if board[i+t][11-j-t]!=p:
                        ok=False
                        break
                if ok==True:
                    for t in range(0, 5):
                        board[i+t][11-j-t] = p+2
                    return p
    return 0


def victory(win , name1, name2):
    global time_win
    amount_win = 0
    while True:
        check =0
        ok_check = False
        if win == 1:
            main_win=xwin
        else:
            main_win=owin
        for i in range(10):
            for j in range(10):
                if board[i+1][j+1]== (win +2):
                    check +=1
                if board[i+1][j+1] == (win +2) and time_win % 30 == 0 and check == (amount_win+1) and ok_check == False:
                    amount_win +=1
                    ok_check = True
                    screen.blit(main_win,(370+i*wide+5, 5+100+j*wide))

        


        time_win +=1
        if time_win == 151:
            show_winner(win, name1,name2)
        pygame.display.update()
        clock.tick(60)






def show_winner(w, name1, name2):
    while True: 
        screen.blit(win_bg, (0, 0))  

        p1=pygame.image.load("assets/kanna1.png")
        p2=pygame.image.load("assets/goku1.png")

        winner_text=pygame.image.load("assets/cooltext426714998961489.png")

        reset_BUTTON = Button(image=pygame.image.load("assets/Play Rect - Copy.png"), pos=(640,600), 
                        text_input="OK", font=get_font(30), base_color="cyan", hovering_color="hotpink")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        for button in [ reset_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)    
        if w==1:
            screen.blit(p1, (545, 200))
        else:
            screen.blit(p2, (440, 200))
        screen.blit(winner_text, (460, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_question()
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if reset_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    show_user_name(name1,name2) 
                    
                                         
        
        pygame.display.update()
        clock.tick(120)  
def show_user_name(user_name1, user_name2 ):
    
    global turn
    global kanna_turn
    global kanna1
    global kanna2
    global kanna3
    global muiten_x
    global muiten_y
    global muiten_move
    global goku1
    global goku2
    global goku_turn
    global won
    turn = base_turn

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=pygame.image.load("assets/HOME.png"), pos=(110, 40), 
                                    text_input=None, font=get_font(30), base_color="cyan", hovering_color="hotpink")      
        if won == True:
            tam="AGAIN"
        else:
            tam="RESET"
        reset_BUTTON = Button(image=pygame.image.load("assets/Play Rect - Copy.png"), pos=(640,670), 
                            text_input=tam, font=get_font(30), base_color="cyan", hovering_color="hotpink")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_question()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_BUTTON.checkForInput(PLAY_MOUSE_POS):                        
                        reset()
                current_pos = pygame.mouse.get_pos()
                x=current_pos[0]
                y=current_pos[1]
                if x > 370 and x < (370+540)   and y > 100 and y <640  and won == False:
                   
                    if checkxy(x,y, turn%2) == True:  
                        turn +=1 
                        if turn == 1000000:
                            turn =0 
                        inxo()
                        winner=check_win()
                        if winner!=0:
                            won=True
                            victory(winner, user_name1, user_name2)       
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        reset()
                        main()                                         
            pygame.display.update()
            
        screen.blit(nenbanco, (0, 0)) 
        screen.blit(banco, (370, 100)) 

        inxo()  
        #check win 
        

        if turn%2==1:
            uu= "assets/Play Rect.png"
            vv="assets/Play Rect - Copy.png"
            turnx="O TURN"
            u ="hotpink"
            v="cyan"            
            muiten_x = 1040
        else:
            vv= "assets/Play Rect.png"
            uu="assets/Play Rect - Copy.png"
            v ="hotpink"
            u="cyan"
            turnx="X TURN"
            
            muiten_x = 120
        X_BUTTON = Button(image=pygame.image.load("assets/Play Rect - Copy.png"), pos=(205,570), 
                            text_input=user_name1, font=get_font(30), base_color="cyan", hovering_color=v)
        O_BUTTON = Button(image=pygame.image.load("assets/Play Rect - Copy.png"), pos=(1080, 570), 
                            text_input=user_name2, font=get_font(30), base_color="hotpink", hovering_color=v)
        turn_BUTTON = Button(image=pygame.image.load("assets/Play Rect - Copy.png"), pos=(640,72), 
                            text_input=turnx, font=get_font(30), base_color=u, hovering_color=v)
        for button in [X_BUTTON, O_BUTTON, turn_BUTTON]:
            #button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for button in [ PLAY_BACK, reset_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)
        
        kanna_turn +=1
        goku_turn +=1
        if kanna_turn == 100000:
            kanna_turn = 0
        kanna_tam = kanna1
        if kanna_turn%15 == 0:
            kanna1 = kanna2
            kanna2 =kanna3
            kanna3 = kanna_tam
            muiten_y += muiten_move
            muiten_move *= -1
        if goku_turn == 1000000:
            goku_turn = 0
        goku_tam = goku1
        if goku_turn%15 ==0:
            goku1=goku2
            goku2=goku_tam
        
        
            
        anhkanna = pygame.image.load(kanna_tam)
        anhgoku = pygame.image.load(goku_tam)
        screen.blit(anhkanna,(95,320))
        screen.blit(anhgoku,(870,270))
        screen.blit(muiten,(muiten_x,muiten_y))
        clock.tick(120)

        pygame.display.update()
        clock.tick(120)


def get_user_name1():
    global namethangdautien

    ok=0
    while True:
        screen.blit(bg, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="cyan", hovering_color="hotpink")                              
        for button in [ PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)
        
        UI_REFRESH_RATE = clock.tick(60)/1000
        name1_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                            text_input="PLAYER 1", font=get_font(30), base_color="cyan", hovering_color="hotpink")
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):                        
                        play()
            if event.type == pygame.QUIT:
                exit_question()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                get_user_name2(event.text)
            if event.type == pygame.QUIT:
                exit_question()
            
                                               
            manager1.process_events(event)        
        manager1.update(UI_REFRESH_RATE)      
        name1_BUTTON.update(screen)       
        manager1.draw_ui(screen)
        pygame.display.update()
        clock.tick(120)
 


def get_user_name2(namethangdautien):
    global namthangthuhai
    while True:
        screen.blit(bg, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="cyan", hovering_color="hotpink")                              
        for button in [ PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)

        UI_REFRESH_RATE = clock.tick(60)/1000
        name2_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                            text_input="PLAYER 2", font=get_font(30), base_color="cyan", hovering_color="hotpink")
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):                        
                        get_user_name1()
            if event.type == pygame.QUIT:
                exit_question()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                    namethangthuhai = event.text
                    show_user_name(namethangdautien,event.text)     
       
            
            manager2.process_events(event)
        
        
        manager2.update(UI_REFRESH_RATE)
        name2_BUTTON.update(screen)      
        manager2.draw_ui(screen)
        pygame.display.update()
        clock.tick(120)
 

 
#nhac.play(loops = -1)
#vong lap xu ly game
run = True

def exit_question():
    global run
    while True:
        screen.blit(question_bg,(490,200))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        
        YES_BUTTON = Button(image=pygame.image.load("assets/exit.png"), pos=(490+150, 290), 
                            text_input="YES", font=get_font(25), base_color="cyan", hovering_color="hotpink")
        NO_BUTTON = Button(image=pygame.image.load("assets/exit.png"), pos=(490+150, 350), 
                            text_input="NO", font=get_font(25), base_color="cyan", hovering_color="hotpink")
        for button in [YES_BUTTON, NO_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if YES_BUTTON.checkForInput(MENU_MOUSE_POS):                        
                        pygame.quit()
                        sys.exit()
                    if NO_BUTTON.checkForInput(MENU_MOUSE_POS):
                        return
                    
       
        pygame.display.update()
        clock.tick(60)





def main(): 
    
    global ham
    global run
    while run:
        
        screen.blit(bg, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                            text_input="PLAY", font=get_font(30), base_color="cyan", hovering_color="hotpink")
        ABOUT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 420), 
                            text_input="ABOUT", font=get_font(30), base_color="cyan", hovering_color="hotpink")
        SETTING_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 490), 
                            text_input="SETTING", font=get_font(30), base_color="cyan", hovering_color="hotpink")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 560), 
                            text_input="QUIT", font=get_font(30), base_color="cyan", hovering_color="hotpink")

        for button in [PLAY_BUTTON, ABOUT_BUTTON,SETTING_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_question() 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ham=1
                    play()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ham=2
                    about()    
                if SETTING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ham=3
                    setting()          
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        exit_question()
        pygame.display.update()
        clock.tick(120)
    #pygame.quit()
   
intro()