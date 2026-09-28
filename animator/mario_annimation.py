import pgzrun, random, itertools
# 358.5
# Screen size
WIDTH = 717
HEIGHT = 400

# Actors
rocky = Actor("rock.png")
mario = Actor("mario.png")
mario.pos = 358.5,200
place = [(667,50),(667,350),(50,350),(50,50)]
result = itertools.cycle(place)


def draw():
    screen.blit("mario bg.jpg",(0,0))
    rocky.draw()
    mario.draw()

# Moving the rock
def move_rock():
    animate(rocky,'bounce_end',duration = 1,pos = next(result))

move_rock()
clock.schedule_interval(move_rock,2)



def mario_move():
    x = random.randint(100,617)
    y = random.randint(100,300)
    mario.target = x,y
    target_ang = mario.angle_to(mario.target)
    target_ang += 360 * ((mario.angle - target_ang + 180) // 360)
    animate(mario, angle = target_ang,duration = 0.5,on_finished = mariomove)

def mariomove():
    g = animate(mario, tween = 'accel_decel', pos = mario.target, duration = mario.distance_to(mario.target) / 200, on_finished = mario_move)
    
mariomove()


    
pgzrun.go()
