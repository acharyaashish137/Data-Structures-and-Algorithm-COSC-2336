WIDTH = 1200
HEIGHT = 675
TITLE = "Assignment 3"

def update():
    pass

def draw():
    screen.clear()
    screen.blit("bg.png", (34, 24))
    screen.draw.text(f"Clip: {player.mainWeapon.clip}", (48, 32), color="yellow", fontsize=40)
    screen.draw.text(f"Remaining Ammo: {player.mainWeapon.ammoLeft}", (0.25*WIDTH, 0.05*HEIGHT), color="yellow", fontsize=40)
    screen.draw.text("Controls: ", (0.07*WIDTH, 0.15*HEIGHT), color="yellow", fontsize=40)
    screen.draw.text("Fire: Up", (0.1*WIDTH, 0.2*HEIGHT), color="white", fontsize=30)
    screen.draw.text("Switch Weapon: Down", (0.1*WIDTH, 0.25*HEIGHT), color="white", fontsize=30)
    screen.draw.text("Reload Weapon: Left", (0.1*WIDTH, 0.3*HEIGHT), color="white", fontsize=30)
    screen.draw.text("Pick Clip: Right", (0.1*WIDTH, 0.35*HEIGHT), color="white", fontsize=30)
    player.draw()# draw the player

#on down key function to take input using arrow
def  on_key_down(key):
        if key ==keys.UP:
            player.fireWeapon()
        elif key == keys.DOWN:
            player.switchWeapons()
        elif key == keys.LEFT:
            player.reloadWeapon()
        elif key == keys.RIGHT:
            player.pickAmmo(1)
            player.mainWeapon.ammoLeft = min(player.mainWeapon.ammoLeft + player.mainWeapon.clip, player.mainWeapon.maxAmmo)
            player.mainWeapon.clip = min(player.mainWeapon.clip, player.mainWeapon.maxAmmo - player.mainWeapon.ammoLeft)


#starter parent class called Weapon
class Weapon:
    def __init__(self, n, fr, p, i):
        self.name = n
        self.fireRate = fr
        self.punch = p
        self.image = i

#The HumanWeapon class should inherit from Weapon.
class HumanWeapon(Weapon):
    def __init__(self, n, fr, p, i, a, c, m):
        super().__init__(n, fr, p, i)
        self.ammoLeft = a
        self.clip = c
        self.maxAmmo = m
#This class should have the function: reload. The weapon can only be reloaded if the variable ammoLeft is not 0.
    def reload(self):
        if self.ammoLeft != 0:
            ammoToReload = min(self.clip, self.ammoLeft)
            self.ammoLeft -= ammoToReload
            self.clip += ammoToReload
#This class  have the function: fire. The weapon can be fired if there is ammo in the clip
    def fire(self):
        if self.clip > 0:
            self.clip -= 1
#This class  have the function: addClip. This function allows the addition of one or more clips. The weapon’s ammo cannot exceed the maximum ammo value.
    def addClip(self, clips):
        self.clip = min(self.clip + clips, self.maxAmmo)

class Actor:
    def __init__(self, x, y, i):
        self.pos = (x, y)
        self.image = i

    def draw(self):
        screen.blit(self.image, self.pos)

#The Player class inherit from Actor.  the Player class get from Actor the image and pos (x, y) properties, and the draw function
class Player(Actor):
    def __init__(self, pos, mainWeapon, secondWeapon, thirdWeapon):
        super().__init__(pos[0], pos[1], mainWeapon.image)
        #stores a reference to the current weapon that the player is holding
        self.mainWeapon = mainWeapon
        # a list that stores the 3 weapons
        self.weapons = [mainWeapon, secondWeapon, thirdWeapon]
        #stores the index of the weapon that will be main when the player swaps the weapon
        self.__swapIndex = 0
#The function should switch the main weapon with the weapon that swapIndex is pointing to
    def switchWeapons(self):
        self.__swapIndex = (self.__swapIndex + 1) % len(self.weapons)
        self.mainWeapon = self.weapons[self.__swapIndex]
        self.image = self.mainWeapon.image

#The function should take one parameter: the new weapon. The function will replace the weapon that the swapIndex is pointing to.
    def pickWeapon(self, newWeapon):
        self.weapons[self.__swapIndex] = newWeapon
        self.mainWeapon = self.weapons[self.__swapIndex]
        self.image = self.mainWeapon.image
#The function will fire the weapon that the player is holding by hand.
    def fireWeapon(self):
        self.mainWeapon.fire()
 #The function will reload the weapon that the player is holding in their hand.
    def reloadWeapon(self):
        self.mainWeapon.reload()
#The function should take as a parameter the number of clips. The function will increase the main weapon’s clips by the number of clips.
    def pickAmmo(self, clips):
        self.mainWeapon.addClip(clips)

player = Player((100, 100),
    HumanWeapon("Pistol", 4, 12, "pistol.png", 48, 4, 48),
    HumanWeapon("Assault Rifle", 3, 60, "rifle.png", 180, 3, 180),
    HumanWeapon("Sniper Rifle", 4, 16, "sniper.png", 16, 4, 40))







