import pgzrun
import random
# Updating size of screen
WIDTH=1500
HEIGHT=1000
# creating a sprite
meteor = Actor("meteor.png")
message = ""
# display the objects 
def draw():
    screen.fill("black")
    meteor.draw()
    screen.draw.text("Destroy the Meteors",center = (750,100),fontsize = 70,color = "red")
    screen.draw.text(message,center = (750,200),fontsize = 70,color = "red")
# function for random position
def rand_p():
    meteor.x = random.randint(100,1400)
    meteor.y = random.randint(100,900)
# mouse event
def on_mouse_down(pos):
    global message
    if meteor.collidepoint(pos):
        rand_p()
        message = "Boom!"


# starting up the game
pgzrun.go()

