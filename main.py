import pygame
import sys
import random

CELLWIDTH = 25
SIZE = (SIZEX,SIZEY) = (25,15)
print(SIZE)
pygame.init()
screen = pygame.display.set_mode((CELLWIDTH*SIZEX,CELLWIDTH*SIZEY))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()



snake_pos = [(1,1),(0,1),(3,3)]

speed = (1,0)
foodpos = (random.randint(0,24), random.randint(0,16))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if speed[0] != 0:
                if event.key == pygame.K_DOWN:
                    speed = (0,1)
                if event.key == pygame.K_UP:
                    speed = (0,-1)
            else:
                if event.key == pygame.K_LEFT:
                    speed = (-1,0)
                if event.key == pygame.K_RIGHT:
                    speed = (1,0)

    screen.fill("white")



    for index in range(len(snake_pos)-1,0,-1):
        snake_pos[index] = snake_pos[index-1]
    snake_pos[0] = (snake_pos[0][0] + speed[0], snake_pos[0][1]+speed[1])

    if snake_pos[0] == foodpos:
        foodpos = (random.randint(1,21), random.randint(1,14))
        snake_pos.append(snake_pos[-1])

    pygame.draw.rect(screen,'green',[foodpos[0]*CELLWIDTH,foodpos[1]*CELLWIDTH,25,25])
    for pos in snake_pos:
        pygame.draw.rect(screen,'red',[pos[0]*CELLWIDTH,pos[1]*CELLWIDTH, CELLWIDTH, CELLWIDTH])
    
    if snake_pos[0][0] not in range(0,SIZEX) or snake_pos[0][1] not in range(0,SIZEY):
        sys.exit()

    if snake_pos[0] in snake_pos[1:]:
        sys.exit()

    clock.tick(10)
    pygame.display.update()
