#!/usr/bin/python
import sys
import pygame

from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == '__main__':

    save = False
    output = 'output'

    # with -s each rectangle is saved
    if '-s' in sys.argv:
        save = True

    d = {}
    s = 1
    o = 0 

    x = 0 
    y = 0
    box = pygame.Rect(x, y, 1, 1)

    topleft = False
    step = 1

    pygame.init()
    font = pygame.font.Font(None, 20)

    screen = pygame.display.set_mode(SIZE) 
    background = pygame.image.load(sys.argv[1]).convert()

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                print d
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if not topleft:
                    box.x = x
                    box.y = y
                    topleft = True
                else:
                    o = o+1
                    topleft = False
                    print 'rectangle ' + str(box)
                    if save:
                        print 'saving rectangle ' + str(box) + ' to file ' + output + '%03d.png' % o
                        screen.blit(background, (0, 0))
                        pygame.display.update()
                        clip = screen.subsurface(box)
                        pygame.image.save(clip, output + '%03d.png' % o)

            elif event.type == KEYDOWN:
                if event.key == K_h:
                    hide = not hide 
                if event.key == K_s:
                    print 'save to ' + output + '%03d.png' % o
                    screen.blit(background, (0, 0))
                    pygame.display.update()
                    clip = screen.subsurface(box)
                    pygame.image.save(clip, output + '%03d.png' % o)
                if event.key == K_PLUS:
                    step = step + 1
                if event.key == K_MINUS:
                    if step > 0:
                        step = step - 1
                if event.key == K_DOWN:
                    x = x
                    y = y+step
                if event.key == K_UP:
                    x = x
                    y = y-step
                if event.key == K_RIGHT:
                    x = x+step
                    y = y
                if event.key == K_LEFT:
                    x = x-step
                    y = y

        x, y = pygame.mouse.get_pos()
        box.w = abs(box.x - x)
        box.h = abs(box.y - y)

        screen.blit(background, (0, 0))
        if topleft == True:
            pygame.draw.rect(screen, (255, 0, 0), (box.x, box.y,
                box.w,box.h), 1)

        info = 'position=' + str(x) + ',' + str(y) + ', x=' + str(box.x)+ ', y=' + str(box.y) + ', w=' + str(box.w) + ', h=' + str(box.h) 
        text = font.render(info, 1, (255,0,0))

        screen.blit(text, (0,0))
        pygame.display.update()
        
# vim:ts=4:sw=4:expandtab:
