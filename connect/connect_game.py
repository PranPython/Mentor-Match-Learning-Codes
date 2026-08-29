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
    else:
        screen.draw.text(str(round(total_t,1)),(20,20),color = "skyblue",fontsize = 40)
    for q in lines:
        screen.draw.line(q[0],q[1],"red")
def on_mouse_down(pos):
    global lines ,next_sat, no_satelites
    if next_sat < 6:
        if no_satelites[next_sat].collidepoint(pos):
            if next_sat:
                lines.append((no_satelites[next_sat-1].pos,no_satelites[next_sat].pos))
            next_sat += 1
        else:
            lines = []
            next_sat = 0



def update():
    pass
r_sat()
pgzrun.go()
