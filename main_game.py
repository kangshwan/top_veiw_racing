import pygame
import point_n_rect as pnr

import random

TABLE     = (  0,128,  0)
BLACK     = (  0,  0,  0)
WHITE     = (255,255,255)
RED       = (255,  0,  0)
BROWN     = (150, 75,  0)
LIGHTBLUE = ( 75,137,220)
win_size  = [1280,960]


class Button():

    def __init__(self, color, position, width, height, text = ''):
        self.color = color
        self.posn = position
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window, outline=None):
        if outline:
            pygame.draw.rect(window, outline, (self.posn.x-2,self.posn.y-2,self.width+4,self.height+4), 0)
        pygame.draw.rect(window, self.color, (self.posn.x, self.posn.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            window.blit(text, (self.posn.x + (self.width/2 - text.get_width()/2), self.posn.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos):
        if self.posn.x < pos[0] and pos[0] <self.posn.x +self.width:
            if self.posn.y < pos[1] <self.posn.y + self.height:
                return True
        return False

pygame.init()

screen = pygame.display.set_mode(win_size)
screen.fill(WHITE)
pygame.display.set_caption("Super")

run = True
clock = pygame.time.Clock()

startButton = Button(LIGHTBLUE, pnr.Point(515, 630), 250, 100, 'Start!')
ready = True
on_table = 0

while run:
    # This limits the while loop to a max of 30 time per second
    # 30fps
    clock.tick(30)

    # Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:      #마우스 클릭시
            pos = pygame.mouse.get_pos()                #pos 에 마우스 좌표값 저장(tuple)
            print(pos)
            if startButton.isOver(pos):
                print("pressed")
                ready = False

    screen.fill(WHITE)
    if ready:
        startButton.draw(screen, BROWN)

    # This MUST happen after all the other drawing commands
    pygame.display.update()
pygame.quit()

