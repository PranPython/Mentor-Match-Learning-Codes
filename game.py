import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ship = Actor("ship")
ship.pos = (400, 550)
beam = Actor("beam")
rock = Actor("meteor")
rock.pos = (random.randint(50, 750), 0)

score = 0
game_over = False
bullet_active = False


def draw():
    screen.clear()
    screen.fill("black")

    ship.draw()
    rock.draw()
    if bullet_active == True:
        beam.draw()
    screen.draw.text("Score: " + str(score), (20, 20), fontsize=35)

    if game_over:
        screen.draw.text("GAME OVER", center=(400, 300), fontsize=60)

def update():
    global score, game_over, bullet_active

    if game_over:
        return

    if keyboard.left:
        ship.x -= 5

    if keyboard.right:
        ship.x += 5

    if bullet_active == True:
        beam.y -= 5
        if beam.bottom < 0:
            bullet_active = False

    rock.y += 5

    if rock.y > 600:
        rock.y = 0
        rock.x = random.randint(50, 750)

    if ship.colliderect(rock):
        game_over = True

    if ship.left < 0:
        ship.left = 0
    if ship.right > WIDTH:
        ship.right = WIDTH
    if ship.top < 0:
        ship.top = 0
    if ship.bottom > HEIGHT:
        ship.bottom = HEIGHT

    if beam.colliderect(rock):
        rock.y = 0
        rock.x = random.randint(50, 750)
        score += 1
        bullet_active = False

        


def on_key_down(key):
    global bullet_active
    if key == keys.SPACE:
        if not bullet_active:
            beam.pos = (ship.x,ship.top)
            bullet_active = True

    
pgzrun.go()
