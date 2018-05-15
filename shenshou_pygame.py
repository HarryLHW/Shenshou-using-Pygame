import sys, pygame, random, time
pygame.init()

size = width, height = 320, 700
speed = 10
white = 255, 255, 255
time_interval=0.27
radius=25
probability_no_stone=0.1

def overlap(a,b):
    return abs(a.center[1]-b.center[1])<radius and a.center==b.center

def exit(i):
    print(i)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if pygame.key.get_pressed()[32]:
            play()

def play():
    global speed,time_interval,radius,probability_no_stone
    probability2=(1-probability_no_stone)/2+probability_no_stone

    screen = pygame.display.set_mode(size)

    finger1=pygame.image.load('finger.png')
    finger2=pygame.image.load('finger.png')
    finger1rect=finger1.get_rect()
    finger2rect=finger2.get_rect()
    finger1rect.center=[120,600]
    finger2rect.center=[200,600]
    stone1s=[]
    stonerect1s=[]
    stone2s=[]
    stonerect2s=[]
    prev=time.time()
    start=time.time()

    score=pygame.font.SysFont("arial", 64)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        current=time.time()
        if current-prev>time_interval:
            prev=time.time()
            stone1=pygame.image.load('stone.png')
            stone2=pygame.image.load('stone.png')
            stone1rect=stone1.get_rect()
            stone2rect=stone2.get_rect()
            a=random.random()
            b=random.random()
            if a<probability_no_stone:
                stone1rect.center=[420,0]
            elif a<probability2:
                stone1rect.center=[40,-40]
            else:
                stone1rect.center=[120,-40]
            if b<probability_no_stone:
                stone2rect.center=[420,0]
            elif b<probability2:
                stone2rect.center=[280,-40]
            else:
                stone2rect.center=[200,-40]

            stone1s.append(stone1)
            stone2s.append(stone2)
            stonerect1s.append(stone1rect)
            stonerect2s.append(stone2rect)

        screen.fill(white)
        delete1=[]
        delete2=[]
        for i in range(len(stone1s)):
            stonerect1s[i]=stonerect1s[i].move([0,speed])
            if overlap(stonerect1s[i],finger1rect):
                exit(str(int(time.time()-start)))
            if stonerect1s[i].top>height+200:
                delete1.append(i)
            else:
                screen.blit(stone1s[i],stonerect1s[i])
        for i in delete1:
            del stone1s[i]
            del stonerect1s[i]
        for i in range(len(stone2s)):
            stonerect2s[i]=stonerect2s[i].move([0,speed])
            if overlap(stonerect2s[i],finger2rect):
                exit(str(int(time.time()-start)))
            if stonerect2s[i].top>height+200:
                delete2.append(i)
            else:
                screen.blit(stone2s[i],stonerect2s[i])
        for i in delete2:
            del stone2s[i]
            del stonerect2s[i]

        scoresurface = score.render(str(int(time.time()-start)), True, (0,0,255))
        screen.blit(scoresurface, (140, 25))
        screen.blit(finger1, finger1rect)
        screen.blit(finger2, finger2rect)
        pygame.display.flip()
        if pygame.key.get_pressed()[118]:
            finger1rect.center=[40,600]
        else:
            finger1rect.center=[120,600]
        if pygame.key.get_pressed()[110]:
            finger2rect.center=[280,600]
        else:
            finger2rect.center=[200,600]

play()
