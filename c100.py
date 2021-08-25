class Ball:
    def __init__(self,colour,shape,hardness):
        self.colour=colour
        self.shape=shape
        self.hardness=hardness

    def bounce(self):
        print('the ball has bounced')

    def kick(self):
        print('the ball has been kicked')

    def checkColour(self,colour):
        print('The colour of the ball is ' + colour) 

ball1 = Ball('red','round','0.5') 
ball1.colour
