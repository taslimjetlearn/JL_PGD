import pgzrun
from random import randint

TITLE = "Good Shot"
WIDTH = 500
HEIGHT = 500

message = ""

#decide the character using built in Actor
alien = Actor('alien')
pink = Actor('pink')

def draw():
    screen.clear()
    screen.fill(color = (128,50,0))
    alien.draw()
    pink.draw()
    screen.draw.text(message, center=(400,10),fontsize=30)

def place_alien():
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)

def place_pink():
    pink.x = randint(50,WIDTH-50)
    pink.x = randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if alien.x < 0:
        alien.x = 500
    else:
        alien.x-=20

def on_key_down(key):
    global message
    if pink.x < 0:
        pink.x = 500
    else:
        pink.x-=20  

place_alien()
place_pink()
pgzrun.go()