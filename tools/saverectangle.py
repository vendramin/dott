#!/usr/bin/python
import sys
import pygame

def display_help():
    print 'Usage: save_rectangle.py -i <input> -o <output> -r <rectangle>'
    print 'Rectangle format:'
    print 'left, top, width, height'
    sys.exit(0)

if __name__ == '__main__':
    
    output = 'output.png' 
    if '-o' in sys.argv:
        pos = sys.argv.index('-o')
        if pos < len(sys.argv)-1 and sys.argv[pos+1][0] != '-':
            output = sys.argv[pos+1]
            sys.argv = sys.argv[:pos] + sys.argv[pos+2:]
            print 'Output file: %s' % output 
        else:
            print 'Missing destination file operand after -o';
            sys.exit(0)
    
    if '-h' in sys.argv:
        display_help()
        sys.exit(0)

    if '-i' in sys.argv:
        pos = sys.argv.index('-i')
        if pos < len(sys.argv)-1 and sys.argv[pos+1][0] != '-':
            filename = sys.argv[pos+1]
            sys.argv = sys.argv[:pos] + sys.argv[pos+2:]
        else:
            print 'Missing destination file operand after -i';
            sys.exit(0)
    else:
        display_help()
        sys.exit(0)

    if '-r' in sys.argv:
        pos = sys.argv.index('-r')
        if pos < len(sys.argv)-1 and sys.argv[pos+1][0] != '-':
            tmp = [x.split(',') for x in sys.argv[pos+1:]] 
            rect = []
            for x in tmp:
                for y in x:
                    try:
                        rect.append(int(y))
                    except:
                        pass
        else:
            print 'Missing rectangle after -r';
            sys.exit(0)
    else:
        display_help()
        sys.exit(0)

    pygame.init()
    image = pygame.image.load(filename)
    clip = image.subsurface(rect[0], rect[1], rect[2], rect[3])
    pygame.image.save(clip, output)
    
        
# vim:ts=4:sw=4:expandtab:
