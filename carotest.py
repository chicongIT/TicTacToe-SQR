       
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
                    pygame.quit()
                    sys.exit()
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
