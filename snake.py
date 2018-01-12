def snakegame():
    import pygame
    import sys
    import time
    import random
    errors=pygame.init()
    if(errors[1]!=0):
        print("Failed to initialize the modules")
        sys.exit()
    else:
        print("No errors..... The game will now start")
    #play surface
    playSurf=pygame.display.set_mode((1080,720))
    pygame.display.set_caption('Snake Game')

    #colors
    red=pygame.Color(255,0,0)#gameover
    brown=pygame.Color(165,42,42)#snake
    blue=pygame.Color(0,0,255)#food
    black=pygame.Color(0,0,0)#score
    white=pygame.Color(255,255,255)#back
    green=pygame.Color(0,255,0)#green

    #FPS controller
    fpsControl=pygame.time.Clock()

    #import Variables
    snakePos=[540,360]
    snakeBody=[[540,360],[530,360],[520,360],[510,360]]
    foodPos=[random.randint(1,108)*10,random.randint(1,72)*10]
    foodSpawn=True
    direction='RIGHT' 
    changeto=direction 
    score=0

    #Game over
    def gameOver():
        myFont=pygame.font.SysFont('monaco',72)
        GOSurf=myFont.render('Game Over',True,red)
        GOSurf2=myFont.render('Restart game?(y/n)',True,green)
        GORect=GOSurf.get_rect()
        GORect2=GOSurf2.get_rect()
        GORect.midtop=(560,100)
        GORect2.midtop=(560,250)
        playSurf.blit(GOSurf,GORect)
        playSurf.blit(GOSurf2,GORect2)
        showscore(0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.key==ord('y') or event.key==ord('Y'):
                snakegame()
            elif event.key==ord('n') or event.key==ord('N'):
                GBMSG=myFont.render('The game will now quit',True,black)
                playSurf.fill(white)
                GBRect=GBMSG.get_rect()
                GBRect.midtop=(560,150)
                playSurf.blit(GBMSG,GBRect)
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                sys.exit()

    #score
    def showscore(choice):
        if choice==1:
            sFont=pygame.font.SysFont('monaco',24)
            Ssurf=sFont.render('Score : {0}'.format(score),True,black)
            Srect=Ssurf.get_rect()
            Srect.midtop=(80,10)
        else:
            sFont=pygame.font.SysFont('monaco',48)
            Ssurf=sFont.render('Score : {0}'.format(score),True,black)
            Srect=Ssurf.get_rect()
            Srect.midtop=(560,450)        
        playSurf.blit(Ssurf,Srect)

    #Logic of Game
    while 1>0 :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT or event.key==ord('d') or event.key==ord('D'):
                    changeto='RIGHT'
                if event.key==pygame.K_LEFT or event.key==ord('a') or event.key==ord('A'):
                    changeto='LEFT'
                if event.key==pygame.K_UP or event.key==ord('w') or event.key==ord('W'):
                    changeto='UP'
                if event.key==pygame.K_DOWN or event.key==ord('s') or event.key==ord('S'):
                    changeto='DOWN'
                if event.key==pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        #Validation of directions
        if changeto=='RIGHT' and not direction=='LEFT':
            direction='RIGHT'
        if changeto=='LEFT' and not direction=='RIGHT':
            direction='LEFT'
        if changeto=='DOWN' and not direction=='UP':
            direction='DOWN'
        if changeto=='UP' and not direction=='DOWN':
            direction='UP'

        if direction=='RIGHT':
            snakePos[0] +=10;
        if direction=='LEFT':
            snakePos[0] -=10;
        if direction=='DOWN':
            snakePos[1] +=10;
        if direction=='UP':
            snakePos[1] -=10;

        #body 
        snakeBody.insert(0,list(snakePos))
        if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
            foodSpawn=False
            score+=1
        else:
            snakeBody.pop()




        #Food spawn
        if foodSpawn==False:
            foodPos=[random.randint(1,108)*10,random.randint(1,72)*10]
        foodSpawn=True

        playSurf.fill(white)
        for pos in snakeBody:
            pygame.draw.rect(playSurf,brown,pygame.Rect(pos[0],pos[1],10,10))
        pygame.draw.rect(playSurf,blue,pygame.Rect(foodPos[0],foodPos[1],10,10))

        if snakePos[0]>1070 or snakePos[0]<0:
            gameOver()
        if snakePos[1]>710 or snakePos[1]<0:
            gameOver()

        for block in snakeBody[1:]:
            if snakePos[0]==block[0] and snakePos[1]==block[1]:
                gameOver()

        showscore(1)
        pygame.display.flip()
        fpsControl.tick(20)
        
snakegame()