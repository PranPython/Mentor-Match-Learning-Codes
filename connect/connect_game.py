import pgzrun
import random

HEIGHT = 1000
WIDTH = 1750
no_satelites = []
lines = []
total_sat = 6
# Time Tracking Variables

start_t = 0
end_t = 0
total_t = 0
# function for random satellites
def r_sat():
    for i in range(total_sat):
        satellite = Actor("satelite")
        satellite.x = random.randint(200,800)
        satellite.y = random.randint(200,1500)
        no_satelites.append(satellite)
def draw():
    screen.blit("space",(0,0))
    for j in no_satelites:
        j.draw()

def update():
    pass
r_sat()
pgzrun.go()