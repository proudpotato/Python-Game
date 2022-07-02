import pygame #載入遊戲模組

pygame.init() #遊戲模組啟動
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))#產生畫布
pygame.display.set_caption("My first pygame!")

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)
CYAN = (0,255,255)
MEG = (255,0,255)
GRAY = (192,192,192)

displayscreen.fill(GRAY) #填滿畫布背景
#pygame.draw.line(畫布名稱, color, start, end, thickness)
pygame.draw.line(displayscreen, Green, (0, WINDOW_HEIGHT/2), (WINDOW_WIDTH, WINDOW_HEIGHT/2), 3)
pygame.draw.line(displayscreen, Red, (WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT), 3)
pygame.draw.line(displayscreen, Green, (0,0), (WINDOW_WIDTH, WINDOW_HEIGHT), 3)
pygame.draw.line(displayscreen, Red, (WINDOW_WIDTH, 0), (0, WINDOW_HEIGHT), 3)

#pygame.draw.circle(畫布名稱, 顏色， 中心點， 半徑, thickness)thickness==0(填滿), 1,2,...10(線條寬度)
pygame.draw.circle(displayscreen, CYAN, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2), 200, 6)
pygame.draw.circle(displayscreen, CYAN, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2), 180, 0)

#pygame.draw.rect(畫布名稱, 顏色, (topleft-x, topleft-y, width, height), thickness)
pygame.draw.rect(displayscreen, Red, (0,0,WINDOW_WIDTH, 50),0)


running = True
while running:
    for event in pygame.event.get(): #抓取畫布上的事件
        #print(event)
        if event.type==pygame.QUIT: 
            running = False
    pygame.display.update() #畫布更新

pygame.quit() #遊戲模組結束