import pygame,sys,math
pygame.init()
screen = pygame.display.set_mode([1400,1000])
img1 = pygame.image.load('car4.png')
img1=pygame.transform.scale(img1,(90,45))
route=pygame.image.load('route5.png')
clock = pygame.time.Clock()
X,Y,dx=52,564,8
teta=30
while True:
    screen.fill((200,100,0))
    screen.blit(route,(30,170))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    X=X+dx
    
    Y=(int(200*math.sin(2 * math.pi*X/1000) )+500)
    Y_der=round(2*math.pi/5*math.cos(2*math.pi*X/1000),2)
    angle=(math.atan(Y_der))
    angle1=-round(angle*180/math.pi,2)
    
    X1=X*math.cos(math.pi*teta)-Y*math.sin(math.pi*teta)
    Y1=X*math.sin(math.pi*teta)+Y*math.cos(math.pi*teta)
    Y1_der=math.sin(math.pi*teta)+Y_der*math.cos(math.pi*teta)
    angle_turn=(math.atan(Y1_der))
    angle1_turn=-round(angle_turn*180/math.pi,2)
    

    img2=pygame.transform.rotate(img1,angle1_turn)
    rect=img2.get_rect(center=(X1,Y1))

    if X>1500:
        X,Y=52,564
 
    screen.blit(img2,rect)
    pygame.display.update()
    clock.tick(150)
    



    
    


 
 
