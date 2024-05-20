TITLE = "Mario Kart IV"
WIDTH = 640
HEIGHT = 640

# Q1: Declare the list of images here
images = ["bowser.png", "kong.png", "luigi.png", "mario.png", "peach.png", "toad.png", "wario.png","yoshi.png"]

# Q2: Declare the Racer class here:
class Racer:
    def __init__(self, driverImage="", coDriverImage=""):
        self.driverImage = driverImage
        self.coDriverImage = coDriverImage

    def swapDrivers(self):
        self.driverImage, self.coDriverImage = self.coDriverImage, self.driverImage

# Q3: Declare the MKNode class here:
class MKNode:
    def __init__(self, content, previous=None, next=None):
        self.content = content
        self.previous = previous
        self.next = next

# Q4: Declare the MKList class here:
class MKList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def draw(self):
        current = self.head
        rank = 1
        while current is not None:
            screen.blit(current.content.driverImage, (0.1*WIDTH, 0.1*HEIGHT+rank*50))
            screen.blit(current.content.coDriverImage, (0.3*WIDTH, 0.1*HEIGHT+rank*50))
            screen.draw.text(str(rank), (0.03*WIDTH, 0.1*HEIGHT+rank*50), fontsize=30, color="yellow")
            current = current.next
            rank += 1

    def get_size(self):
        return self.size

    def addRacerToTop(self, driverImage, coDriverImage):
        new_node = MKNode(Racer(driverImage, coDriverImage))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.size += 1

    def addRacerToEnd(self, driverImage, coDriverImage):
        new_node = MKNode(Racer(driverImage, coDriverImage))
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def removerRacerEnd(self):
        if self.tail is None:
            return
        elif self.tail.previous is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.size -= 1

racers = MKList()
racers.addRacerToTop(images[3], images[4])
racers.addRacerToTop(images[2], images[7])
racers.addRacerToEnd(images[5], images[1])
racers.addRacerToEnd(images[7], images[6])

def draw():
    screen.clear()
    screen.draw.text("Ranks", (0.45*WIDTH, 0.03*HEIGHT), fontsize=40, color="blue")
    racers.draw()

def update():
    pass
