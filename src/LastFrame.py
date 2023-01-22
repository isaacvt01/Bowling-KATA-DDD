from src.Frames import Frames
from src.Interface import Interface


class LastFrame(Frames, Interface):

    def __init__(self, roll):
        Frames.__init__(self,roll)



    def computeScore(self):
        scorePerFrame = 0
        self.lastFrame = True
        for roll in self.roll:

            if roll.isdigit():
                scorePerFrame += int(roll)
            elif roll == '-':
                scorePerFrame += 0
            elif roll == 'X':
                scorePerFrame += 10
                self.strike = True
            elif roll == '/':
                scorePerFrame = 10
                self.spare = True
            else:
                raise ValueError(f"This roll is not avaiable {roll}")
        self.individualScore = scorePerFrame

    def triple(self):
        if self.roll.count('X') == 3:
            return 60
