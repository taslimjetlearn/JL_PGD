import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

score=0
gameover=False

bee=Actor("bee")
bee.pos=100,100

flower = Actor("flower")
flower.pos = 200,200

def draw():
    screen.blit("background",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: "+str(score),color="black", topleft=(10,10))

    if gameover:
        screen.fill("pink")
        screen.draw.text("Time Over! Your final score is "+str(score), midtop=(WIDTH/2,10),fontsize=35,color="orange")


def placeflower():
    flower.x= randint(70, (WIDTH-70))
    flower.y= randint(70, (HEIGHT-70))

def timeup():
    global gameover
    gameover = True

def update():
    global score

    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2

    flowercount = bee.colliderect(flower)

    if flowercount:
        score=score+5
        placeflower()

clock.schedule(timeup,60.0)

pgzrun.go()