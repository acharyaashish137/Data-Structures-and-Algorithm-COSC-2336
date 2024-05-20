from random import shuffle, randint
TITLE = "Mario Kart V"
WIDTH = 640
HEIGHT = 640

#----- Q1 to 4 - Implement the RoundManager class -----#

class RoundManager:
    def __init__(self, mlaps):
        self.lap = 1                    # Q1.a lap with a value of 1.
        self.maxLaps = mlaps            #Q 1.b  a variable called maxLaps. The constructor’s parameter should be used to initialize this variable.
        self.displayTable = False       #Q 1.c Boolean variable called displayTable that determine when the table should be displayed on the screen. Initially, this variable should be false.
        self.times = [0] * 8             #Q 1.d An integer list called times that stores the lap time for each our 8 racers.Initially, all racers start with time 0.

        #Q1.e a string list called names, and initialize it with the correct name for each of our 8 racers
        self.names = ['Mario', 'Luigi', 'Princess', 'Toad', 'Yoshi', 'Kong', 'Wario', 'Bowser']

    def disqualifyRacers(self, n):       #Q2. function called disqualifyRacers that belongs to the RoundManager class. The function takes one parameter called n and returns no value.
        for i in range(n):
            idx = self.times.index(max(self.times))
            self.times.pop(idx)
            self.names.pop(idx)

 # Q.3 A function called completeLap, that belongs to the RoundManager class. It simulates how the racers will finish a lap. T
    def completeLap(self):
        shuffle(self.times)
        lapTimes = [randint(1, 180) + i*5 for i in range(8)]
        for i in range(len(self.names)):
            self.times[i] += lapTimes[i]

        if self.lap < 5:
            self.disqualifyRacers(1)
        elif self.lap == 5:
            self.disqualifyRacers(2)

        self.lap += 1

    #Q4.function called drawStandings, that belongs to the RoundManager class. The function takes no parameters and returns no value. T
    def drawStandings(self, lapTimes):
        screen.draw.text("STANDINGS", (0.3*WIDTH, 0.45*HEIGHT), fontsize=40, color="blue")
        screen.draw.text("-----------------------------------------------------------------------------------", (0.2*WIDTH, 0.50*HEIGHT), fontsize=20, color="white")
        screen.draw.text("LAP#" + str(lapTimes), (0.2*WIDTH, 0.55*HEIGHT), fontsize=30, color="blue")
        screen.draw.text("-----------------------------------------------------------------------------------", (0.2*WIDTH, 0.57*HEIGHT), fontsize=20, color="white")
        best_time = max(self.times)
        for i, name in enumerate(self.names):
            time = self.times[i]
            text = f"{i+1}. {name}: {time:.1f}s"
            y = 0.6*HEIGHT + i*30

            #Q7.The best time should be displayed in a different color (yellow).
            if time == best_time:
                screen.draw.text(text, (0.2*WIDTH, y), fontsize=20, color="yellow")
            else:
                screen.draw.text(text, (0.2*WIDTH, y), fontsize=20, color="blue")

#----- Q5 - Create an instance (object) of our class -----#
rm = RoundManager(5)


#Q6. Complete the on_key_down function so a lap is completed every time the player presses the a button, and the lap standings table drawn on the screen every time the player presses the p button.
def on_key_down(key):
    if key == keys.A and rm.lap <= rm.maxLaps:
        rm.completeLap()
    elif key == keys.P:
        rm.displayTable = not rm.displayTable


def draw():
    screen.clear()

    screen.draw.text("Elimination Race", (0.35*WIDTH, 0.25*HEIGHT), fontsize=40, color="yellow")
    screen.draw.text("Press a to advance a lap", (0.2*WIDTH, 0.35*HEIGHT), fontsize=30, color="white")
    screen.draw.text("Press p to print/hide the table of standings", (0.2*WIDTH, 0.4*HEIGHT), fontsize=30, color="white")
    #Q8. The table of standings should now display both the lap time and cumulative lap.
    if rm.displayTable:
        rm.drawStandings(rm.lap-1)
def update():
    pass
