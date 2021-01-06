import pygame
pygame.init()
dis_height = 600
dis_width = 600
dis = pygame.display.set_mode((dis_height,dis_width))#set display dimension(pixels)

#TODO Random food placement
#if snake_head == food location add to snake body
#maybe use an array to display snakes parts
#if head == snake_array[i] end game
#display score
#display end game

pygame.display.set_caption('Snake Game by Quenten')
game_over = False

x1 = 300
y1 = 300

x1_delta = 0
y1_delta = 0

clock = pygame.time.Clock() #set ping rate on user inputs

#colors
blue = (0,0, 255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        #enable movement for keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_delta = -10
                y1_delta = 0
            elif event.key == pygame.K_RIGHT:
                x1_delta = 10
                y1_delta = 0
            elif event.key == pygame.K_UP:
                x1_delta = 0
                y1_delta = -10
            elif event.key == pygame.K_DOWN:
                x1_delta = 0
                y1_delta = 10
        #game over if snake goes out of bounds
        if x1 < 0 or x1 > dis_width or y1 <0 or y1 > dis_height:
            game_over = True

    x1 += x1_delta
    y1 += y1_delta
    dis.fill(black)
    pygame.draw.rect(dis,blue,[x1,y1,10,10])
    
    
    pygame.display.update()

    clock.tick(30)
pygame.quit
quit()
