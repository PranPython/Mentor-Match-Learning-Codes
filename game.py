import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ship = Actor("ship")
ship.pos = (400, 550)

rock = Actor("meteor")
rock.pos = (random.randint(50, 750), 0)

score = 0
game_over = False



def draw():
    screen.clear()
    screen.fill("black")

    ship.draw()
    rock.draw()

    screen.draw.text("Score: " + str(score), (20, 20), fontsize=35)

    if game_over:
        screen.draw.text("GAME OVER", center=(400, 300), fontsize=60)

def update():
    global score, game_over

    if game_over:
        return

    if keyboard.left:
        ship.x -= 5

    if keyboard.right:
        ship.x += 5

    rock.y += 5

    if rock.y > 600:
        rock.y = 0
        rock.x = random.randint(50, 750)
        score += 1

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


pgzrun.go()
