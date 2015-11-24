#!/usr/bin/python
import os,socket,pygame,sys,eztext
from pygame import *

def check_address(address):
    try:
        address.split('.') == True
        for n in address.split('.'):
            try:
                int(n)
            except:
                x = socket.gethostbyname(address)
                return x
        x = socket.gethostbyaddr(address)[0]
    except:
        x = socket.gethostbyname(address)
    return x

#fixed window position
wx,wy = 0,0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (wx,wy)

pygame.init()

w,h = 320,16
screen = pygame.display.set_mode((w,h), pygame.NOFRAME)

#eztext
txtbx = eztext.Input(maxlength=60, color=(255,255,255), prompt='HOST: ')
font = pygame.font.Font('airstrip.ttf',10)
txtbx.set_pos(2,2)
txtbx.set_font(font)

clock = pygame.time.Clock()

while 1:
    mx,my = pygame.mouse.get_pos()

    events = pygame.event.get()
    for event in events:
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RETURN:
            address = txtbx.update(events)
            try:
                result = check_address(address)
            except:
                result = 'ERROR'
            txtbx.value = result

    screen.fill((0,0,100))
    
    txtbx.update(events)
    txtbx.draw(screen)
    pygame.display.update()
