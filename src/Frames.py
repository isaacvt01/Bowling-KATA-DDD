from src.Interface import Interface


class Frames(Interface):

    def __init__(self, roll):
        self.roll = roll
        self.individualScore = 0
        self.spare = False
        self.strike = False
        self.lastFrame = False
    def __repr__(self):
        return f'{self.roll} score: {self.individualScore} | '

    def computeScore(self):
        scorePerFrame = 0
        for roll in self.roll:

            if roll.isdigit():
                scorePerFrame += int(roll)
            elif roll == '-':
                scorePerFrame += 0
            elif roll == 'X':
                scorePerFrame = 10
                self.strike = True
            elif roll == '/':
                scorePerFrame = 10
                self.spare = True
            else:
                raise ValueError(f"This roll is not avaiable {roll}")
        self.individualScore = scorePerFrame



    def getLen(self):
        return len(self.roll)



