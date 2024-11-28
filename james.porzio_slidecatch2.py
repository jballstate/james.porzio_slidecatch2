# import necessary modules like pygame, simpleGE, and random
import pygame, random, simpleGE
# define class for falling gold
class Gold(simpleGE.Sprite):
# initialize gold
    def __init__(self, scene):
        super().__init__(scene)
# set image for gold
        self.setImage("Gold.png")
# scale sprite correctly
        self.setSize(31, 31)
# reset sprite position
        self.reset()
# method to reset gold      
    def reset(self):
# gold starts falling from sky
        self.y = 11
# random integer for x 
        self.x = random.randint(0, self.screenWidth)
# random integer for y speed
        self.dy = random.randint(4, 6)
# method to check if gold is off screen       
    def checkBounds(self):
# reset when gold is off screen
        if self.bottom > self.screenHeight:
            self.reset()
# define new class for the robot character
class Robot(simpleGE.Sprite):
# initialize robot
    def __init__(self, scene):
        super().__init__(scene)
# set image for robot
        self.setImage("robot.png")
# scale sprite correctly
        self.setSize(65, 65)
# robot starts on the ground
        self.position = (300, 450)
# robot move speed
        self.moveSpeed = 3
# method for movement
    def process(self):
# move robot left if left arrow key is pressed
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
# move robot right if right arrow key is pressed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
# move robot up if up arrow key is pressed
        if self.isKeyPressed(pygame.K_UP): 
            self.y -= self.moveSpeed
# move robot down if down arrow key is pressed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
# define class for score
class LblScore(simpleGE.Label):
# initialize score
    def __init__(self):
        super().__init__()
# score amount text
        self.text = "Score: "
# score amount text position
        self.center = (90, 300)
# define class for time      
class LblTime(simpleGE.Label):
# initialize time 
    def __init__(self):
        super().__init__()
# amount time left text
        self.text = "Time Left: "
# amount time left text position
        self.center = (550, 300)
# define class for game
class Game(simpleGE.Scene):
# initialize game
    def __init__(self):
        super().__init__()
# set image for background
        self.setImage("backgg.png")
# create game timer
        self.timer = simpleGE.Timer()
# set timer to 5 seconds
        self.timer.totalTime = 5
# starting score
        self.score = 0
# set sound for collision 
        self.sndGold = simpleGE.Sound("my_original_sound.wav")
# create robot
        self.robot = Robot(self)
# create gold
        self.golds = []
        for i in range(4):
            self.golds.append(Gold(self))
# add game score
        self.lblScore = LblScore()
# add game timer
        self.lblTime = LblTime()
# add robot, gold, time, and score sprite to scene
        self.sprites = [self.robot,
                        self.golds,
                        self.lblScore, 
                        self.lblTime]
# method for collision
    def process(self):
        for gold in self.golds:
# robot gold collision
            if self.robot.collidesWith(gold):
# play my original sound
                self.sndGold.play()
# reset gold
                gold.reset()
# increase score by 1 when you touch gold
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
# countdown timer  
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
# if time is 0, game is over
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()
# define class for instructions
class Instructions(simpleGE.Scene):
# initialize instructions
    def __init__(self, score):
        super().__init__()
# set image for background
        self.setImage("backgg.png")
# Play makes game start
        self.response = "Play"
# label to make instructions text
        self.instructions = simpleGE.MultiLabel()
# game instructions
        self.instructions.textLines = [
        "Robot Game",
        "Move in all directions using arrow keys",
        "Collect the gold in 5 seconds",
        "",]
# instructions postion
        self.instructions.center = (250, 380)
# instructions size
        self.instructions.size = (400, 150)
# your score becomes previous score
        self.prevScore = score
        self.lblScore = simpleGE.Label()
# previous score text
        self.lblScore.text = f"Prev score: {self.prevScore}"
# previous score text position
        self.lblScore.center = (320, 100)
# add play button
        self.btnPlay = simpleGE.Button()
# play button text
        self.btnPlay.text = "Click to Play"
# play button position
        self.btnPlay.center = (100, 190)
# add quit button
        self.btnQuit = simpleGE.Button()
# quit button text
        self.btnQuit.text = "Click to Quit"
# quit button position
        self.btnQuit.center = (550, 50)
# add instructions, score, quit, and play sprite to scene
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnQuit,
                        self.btnPlay]
# method for buttons
    def process(self):
# if you click quit button
        if self.btnQuit.clicked:
# response is quit
            self.response = "Quit"
# stop scene
            self.stop()
# if you click play button
        if self.btnPlay.clicked:
# response is play
            self.response = "Play"
# stop scene
            self.stop()
# define new function for main
def main():
    keepGoing = True
# initial score is 0
    score = 0
# game loop
    while keepGoing:
# display score on instructions scene   
        instructions = Instructions(score)
# instructions scene
        instructions.start()
# if user chooses play                
        if instructions.response == "Play":
# run game class
            game = Game()
# start game
            game.start()
# show score from game
            score = game.score
# if user chooses quit, end game loop
        else:
            keepGoing = False    
# if name is main, call main function to start game
if __name__ == "__main__":
    main()
