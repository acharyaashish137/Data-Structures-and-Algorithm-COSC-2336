from random import randint
# Global Variables
TITLE = 'Review'
BLOCK_SIZE = 64
WORLD_SIZE = 10
# Screen is 10 x 11 blocks
WIDTH = WORLD_SIZE*BLOCK_SIZE
HEIGHT = (WORLD_SIZE+1)*BLOCK_SIZE
displayGrid = True  # False: do not show grid, True: show grid

ghosts = []
for i in range(4):
    g =  Actor("ghost" + str(i) + ".png")
    ghosts.append(g)
    g.x = (4.5 + i) * BLOCK_SIZE
    g.y = 5.5 * BLOCK_SIZE

square = Actor("gridbox.png", anchor=("left","top"))
square.x = 0.0
square.y = 0.0
pacman = Actor("pacman.png")
pacman.invincible = False #adding new property to pacman
pacman.x = BLOCK_SIZE/2
pacman.y = BLOCK_SIZE/2
super_pallet = Actor("superpallet.png") #adding superpallet
random_x = (randint(0, WORLD_SIZE) + 0.5) * BLOCK_SIZE
random_y = (randint(0, WORLD_SIZE) + 0.5) * BLOCK_SIZE
super_pallet.x = random_x
super_pallet.y = random_y
def drawGrid():
    for j in range(WORLD_SIZE):
        square.y = j* BLOCK_SIZE
        for i in range(WORLD_SIZE):
            square.x = i* BLOCK_SIZE
            square.draw()
def drawGhosts():
    #for i in range(len (ghosts)):
        #ghosts[i].draw()
    for a in ghosts:
        a.draw()


def draw():
    screen.clear()
    screen.draw.text("Position:" + str(pacman.x)+"," + str(pacman.y), topleft=(2*BLOCK_SIZE, 10*BLOCK_SIZE), color="yellow", fontsize=40)
    if displayGrid:
        drawGrid()
    pacman.draw()
    drawGhosts()
    super_pallet.draw()
def on_key_up(key):
    if key == keys.LEFT: #limiting the movement of pacman inside the screen
        if pacman.x - BLOCK_SIZE >= 0:
            pacman.x -= BLOCK_SIZE
    elif key == keys.RIGHT:
        if pacman.x + BLOCK_SIZE <= WIDTH:
            pacman.x += BLOCK_SIZE
    elif key == keys.UP:
        if pacman.y - BLOCK_SIZE >= 0:
            pacman.y -= BLOCK_SIZE
    elif key == keys.DOWN:
        if pacman.y + BLOCK_SIZE <= HEIGHT:
            pacman.y += BLOCK_SIZE

def move(g):
    rNumber = randint(1,100)
    if rNumber == 100:
        xDir = randint(-1,1)
        new_x = g.x + xDir * BLOCK_SIZE
        if new_x >= 0 and new_x <= WIDTH:
            g.x = new_x
            yDir = randint(-1,1)
            new_y = g.y + yDir * BLOCK_SIZE
        if new_y >= 0 and new_y <= HEIGHT:
            g.y = new_y

def update():
    for g in ghosts:
        move(g)
    if pacman.collidepoint(super_pallet.x, super_pallet.y):
        pacman.invincible = True
        super_pallet.x = -100 # move it outside of the screen
        super_pallet.y = -100
    for g in ghosts:
        if pacman.collidepoint(g.x, g.y) and not pacman.invincible: #Added code to make the game end when Pac-man collides with a ghost when not invincible
            print("Game Over")
            quit()# end the game

        elif pacman.collidepoint(g.x, g.y) and pacman.invincible: #Added code to make the ghost return to bottomright grid when Pac-man collides with it when invincible
            g.x = (WORLD_SIZE-1) * BLOCK_SIZE
            g.y = (WORLD_SIZE-1) * BLOCK_SIZE


