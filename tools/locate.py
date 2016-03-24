#!/usr/bin/python
import sys
import pygame

from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

def load_image(filename, colorkey=None):
    if not colorkey == None:
        tmp = pygame.image.load(files[s]).convert()
        tmp.set_colorkey(colorkey)
        return tmp
    else:
        return pygame.image.load(files[s]).convert_alpha()

"""
Alternativas para usar este script
    1) python locate.py background.png sprite1.png sprite2.png (...)
    2) python locate.py datos.txt
"""
if __name__ == '__main__':

    key = None
    if '-c' in sys.argv:
        pos = sys.argv.index('-c')
        if pos < len(sys.argv)-1 and sys.argv[pos+1][0] != '-':
            key = eval(sys.argv[pos+1])
            sys.argv = sys.argv[:pos] + sys.argv[pos+2:]
            print 'colorkey=' + str(key)
        else:
            print 'Missing destination file operand after -c';
            sys.exit(0)
 
    # la primera entrada del archivo es el background 
    # el resto los sprites
    files = []
    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        for line in f.readlines():
            files.append(line.rstrip('\n'))
        f.close()
    else:
        files = sys.argv[1:]

    output = 'output'

    d = {}

    s = 1
    o = 0 
    x = 0 
    y = 0
    step = 1
    hide = False

    pygame.init()

    font = pygame.font.Font(None, 20)

    screen = pygame.display.set_mode(SIZE) 
    background = pygame.image.load(files[0]).convert()
    image = load_image(files[s], colorkey=key)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                print d
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
            elif event.type == KEYDOWN:
                if event.key == K_h:
                    hide = not hide 
                if event.key == K_s:
                    print 'save to ' + output + '%03d.png' % o
                    screen.blit(background, (0, 0))
                    if not hide:
                        screen.blit(image, (x, y))
                    pygame.display.update()
                    clip = screen.subsurface(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
                    pygame.image.save(clip, output + '%03d.png' % o)
                    o = o + 1
                if event.key == K_SPACE:
                    if s < len(files)-1:
                        s = s + 1
                    else:
                        s = 1
                    image = load_image(files[s], colorkey=key)
                    try:
                        x = d[files[s]][0]
                        y = d[files[s]][1]
                    except:
                        pass

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

        d[files[s]] = (x,y)

        info = 'x=' + str(x) + ', y=' + str(y) + ', filename: ' + files[s]
        text = font.render(info, 1, (255,0,0))

        screen.blit(background, (0, 0))
        if not hide:
            screen.blit(image, (x, y))
        screen.blit(text, (0,0))
        pygame.display.update()
        
# vim:ts=4:sw=4:expandtab:
