#!/usr/bin/python
import sys
import pygame

files = [
'c106_t1_i0.pcx',
'c106_t1_i2.pcx', 
'c106_t1_i3.pcx',
'c106_t1_i4.pcx',
'c106_t1_i5.pcx',
'c106_t1_i6.pcx',
'c106_t1_i7.pcx',
'c106_t1_i8.pcx',
'c106_t1_i9.pcx',
'c106_t1_i10.pcx',
'c106_t1_i11.pcx', 
'c106_t1_i12.pcx',
'c106_t1_i13.pcx',
'c106_t1_i14.pcx',
'c106_t1_i15.pcx',
'c106_t1_i16.pcx',
'c106_t1_i17.pcx',
'c106_t1_i18.pcx',
'c106_t1_i19.pcx',
'c106_t1_i20.pcx',
'c106_t1_i21.pcx',
'c106_t1_i22.pcx',
'c106_t1_i24.pcx',
'c106_t1_i25.pcx',
'c106_t1_i26.pcx',
'c106_t1_i27.pcx',
'c106_t1_i28.pcx',
'c106_t1_i29.pcx',
'c106_t1_i30.pcx',
'c106_t1_i31.pcx',
'c106_t1_i32.pcx',
'c106_t1_i33.pcx',
'c106_t1_i34.pcx',
'c106_t1_i35.pcx',
'c106_t1_i36.pcx',
'c106_t1_i37.pcx',
'c106_t1_i39.pcx',
'c106_t1_i40.pcx',
'c106_t1_i41.pcx'
]

if __name__ == '__main__':
    
    pygame.init()
    i = 1
    for f in files:
        image = pygame.image.load(f)
        new = pygame.transform.scale2x(image)
        pygame.image.save(new, '%02d.png'%i)
        i = i+1

    
        
# vim:ts=4:sw=4:expandtab:
