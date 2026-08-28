import pgzrun
import random
import time

WIDTH = 1750
HEIGHT = 1000

no_satelites = []
lines = []
total_sat = 6
next_sat = 0
# Time Tracking Variables

start_t = 0
end_t = 0
total_t = 0
# function for random satellites
def r_sat():
    global start_t
    for i in range(total_sat):
        satellite = Actor("satelite")
        satellite.y = random.randint(200,800)
        satellite.x = random.randint(200,1500)
        no_satelites.append(satellite)
    start_t = time.time()
def draw():
    global total_t, next_sat ,total_sat
    screen.blit("space",(0,0))
    count = 1
    for j in no_satelites:
        j.draw()
        screen.draw.text(str(count),(j.pos[0], j.pos[1]+20),color = "black",fontsize = 35)
        count += 1
    if next_sat < total_sat:
        total_t = time.time() - start_t
        screen.draw.text(str(round(total_t,1)),(20,20),color = "skyblue",fontsize = 40)

def update():
    pass
r_sat()
pgzrun.go()
