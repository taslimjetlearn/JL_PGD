import pgzrun
WIDTH = 400
HEIGHT=400

def draw():
    r = 200
    g = 100
    b = 230
    width = WIDTH - 50
    height = HEIGHT - 300
    #rectangle
    rect = Rect((25, 20), (width, height))
    screen.draw.filled_rect(rect,(r,g,b))
    #line
    screen.draw.line((25,130),(375,130),"white")
    #circle
    screen.draw.filled_circle((200,220),70,"green")

pgzrun.go()