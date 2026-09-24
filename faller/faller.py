import pgzrun
import random

# Screen Size
WIDTH = 889
HEIGHT = 500

# Actors
Actors = ["bag.png","book.png","laptop.png","pencil.png","pouch.png"]
# Variables
game_over = False
game_win = False
lvl = 1
tot_lvl = 6
speed_of_obj = 8
target_obj = None
current_falling = []
marquee = Rect(0,0,889,50)

def draw():
    screen.blit("school.jpg",(0,0))
    if game_over:
        screen.draw.text("You lost :(",(384.5,150), fontsize = 55, color = "black")
        screen.draw.text("Click to restart",(384.5,200), fontsize = 35, color = "black")
        screen.draw.text("Level : "+ str(lvl),(25,25), fontsize = 55, color = "black")
    elif game_win:
        screen.draw.text("You win :)",(384.5,150), fontsize = 55, color = "black")
        screen.draw.text("Click to restart",(384.5,200), fontsize = 35, color = "black")
        screen.draw.text("Level : "+ str(lvl),(25,25), fontsize = 55, color = "black")
    else:
        screen.draw.text("Level : "+ str(lvl),(25,25), fontsize = 55, color = "black")
        for x in current_falling:
            x.draw()
        screen.draw.rect(marquee,"white")
        screen.draw.textbox(f"Click the {target_obj.split('.')[0].capitalize()}!",marquee, color = "dark Red")
# Function for Game Over
def gameover():
    global game_over
    game_over = True


def edge_of_screen(actor):
    global game_over, game_win
    if game_over or game_win:
        return
    if not actor.active:
        return
    if actor.image == target_obj:
        game_over = True
# Function to create falling items
def fall(extra):
    global target_obj, Actors
    l1 = []
    target_obj = random.choice(Actors)
    l2 = random.choices([i for i in Actors if i != target_obj], k=extra)
    l_total = [target_obj]+l2
    random.shuffle(l_total)
    distance = WIDTH / (len(l_total) + 1)
    for u, img in enumerate(l_total):
        acting = Actor(img)
        acting.active = True
        acting.x = (u + 1) * distance
        acting.y = random.randint(-51,0)
        l1.append(acting)
        animate(acting, duration = max(1,speed_of_obj - lvl), on_finished = lambda a=acting: edge_of_screen(a),y = HEIGHT )
    return l1

def on_mouse_down(pos):
    global current_falling, lvl, game_win, game_over
    if game_over or game_win:
        restart()
        return
    else:
        for d in current_falling:
            if d.collidepoint(pos):
                if d.image == target_obj:
                    if lvl == 6:
                        game_win = True
                        for i in current_falling:
                            i.active = False
                        current_falling = []
                    else:
                        lvl += 1
                        for i in current_falling:
                            i.active = False
                        current_falling = []
                else:
                    gameover()


def restart():
    global game_over, game_win, target_obj, lvl, current_falling
    for g in current_falling:
        g.active = False
    game_over = False
    game_win = False        
    lvl = 1
    current_falling = []
    target_obj = None

def update():
    global current_falling, lvl
    if game_over or game_win == True:
        return
    if len(current_falling) == 0:
        current_falling = fall(lvl)
pgzrun.go()
