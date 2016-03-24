#!/usr/bin/python
import sys
import pygame

def display_help():
    print 'Usage: 2x.py -i <input> -o <output>'
    sys.exit(0)

if __name__ == '__main__':
    
    output = 'output.png' 
    if '-o' in sys.argv:
        pos = sys.argv.index('-o')
        if pos < len(sys.argv)-1 and sys.argv[pos+1][0] != '-':
            output = sys.argv[pos+1]
            sys.argv = sys.argv[:pos] + sys.argv[pos+2:]
            print 'Output gnuplot file will be: %s' % output 
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

    pygame.init()
    image = pygame.image.load(filename)
    new = pygame.transform.scale2x(image)
    pygame.image.save(new, output)
    
        
# vim:ts=4:sw=4:expandtab:
