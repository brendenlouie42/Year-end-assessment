import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))

def draw_tree(x,y):
    
    pygame.draw.rect(screen,(117,90,0),(x,y-100,50,100))
  
    pygame.draw.circle(screen,(27,117,0),(x+25,y-120),50)

def draw_house(x,y):
    
    pygame.draw.rect(screen,(0,0,0),(x,y-180,200,180))
    
    pygame.draw.rect(screen,(89,71,0),(x+80,y-60,40,60))

    
    pygame.draw.polygon(screen, (0,0,0), ( (x,y-180),(x+100,y-250),(x+200,y-180) ) )
    draw_window(x+20,y-90)
    draw_window(x+130,y-90)
def draw_window(x,y):
  
    pygame.draw.rect(screen,(207,229,255),(x,y-50,50,50))
  
    pygame.draw.rect(screen,(0,0,0),(x,y-50,50,50),5)
    pygame.draw.rect(screen,(0,0,0),(x+23,y-50,5,50))
    pygame.draw.rect(screen,(0,0,0),(x,y-27,50,5))


pygame.draw.rect(screen,(0,160,3),(0,400,640,80))

pygame.draw.rect(screen,(150,200,255),(0,0,640,400))
 
draw_tree(400,400)
draw_tree(300,400)
draw_tree(550,400)
draw_house(30,400)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()