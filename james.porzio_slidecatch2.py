import pygame, random, simpleGE

class Gold(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Gold.png")
        self.setSize(31, 31)
        self.reset()
        
    def reset(self):
        self.y = 11
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(4, 6)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Robot(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Robot.png")
        self.setSize(65, 65)
        self.position = (300, 450)
        self.moveSpeed = 3
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_UP): 
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: "
        self.center = (90, 300)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: "
        self.center = (550, 300)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("backgg.png")
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 5
        self.score = 0
        
        self.sndGold = simpleGE.Sound("my_original_sound.wav")
        
        self.robot = Robot(self)
        self.golds = []
        for i in range(4):
            self.golds.append(Gold(self))
            
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        self.sprites = [self.robot,
                        self.golds,
                        self.lblScore, 
                        self.lblTime]
        
    def process(self):
        for gold in self.golds:
            if self.robot.collidesWith(gold):
                self.sndGold.play()
                gold.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("backgg.png")
        
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
        "Robot Game",
        "Move in all directions using arrow keys",
        "Collect the gold in 5 seconds",
        "",]
        
        self.instructions.center = (250, 380)
        self.instructions.size = (400, 150)
        
        self.prevScore = score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"High score: {self.prevScore}"
        self.lblScore.center = (320, 100)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Click to Play"
        self.btnPlay.center = (100, 190)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Click to Quit"
        self.btnQuit.center = (550, 50)
        
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnQuit,
                        self.btnPlay]
        
    def process(self):
        #buttons
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        
def main():
    keepGoing = True
    score = 0
    while keepGoing:
        
        instructions = Instructions(score)
        instructions.start()
                
        if instructions.response == "Play":    
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False
            
            
if __name__ == "__main__":
    main()