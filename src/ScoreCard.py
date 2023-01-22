from src.Frames import Frames
from src.LastFrame import LastFrame
class ScoreCard:
    def __init__(self, card):
        self.card = card
        self.frames = []
        self.score = 0
        self.symbols = "-123456789/"


    def __repr__(self):
        return f'TOTAL: {self.score}, Frames: {self.frames}, card: {self.card}'

    def splitLastFrame(self, last_roll):

        self.frames.append(LastFrame(last_roll))

    def splitFrames(self):

        number_rolls = 0

        frame = 0

        complete_roll = ''

        last_roll = ''

        LastFrame = False

        for roll in self.card:

            if LastFrame == False:

                if number_rolls == 2:
                    self.frames.append(Frames(complete_roll))
                    number_rolls = 0
                    frame += 1
                    complete_roll = ''

                if roll in self.symbols:
                    complete_roll += roll
                    number_rolls += 1

                if frame == 9:
                    LastFrame = True
                    last_roll += roll

                if roll == 'X' and LastFrame == False:
                    self.frames.append(Frames(roll))
                    frame += 1
                    number_rolls = 0
            else:
                    last_roll += roll

        self.splitLastFrame(last_roll)

    def setScore(self, score):
        self.score += score


    def getTotalScore(self):
        return self.score

    def checkFrames(self):
        return len(self.frames) == 10

    def double(self, index):
        if (index + 2) < len(self.frames):
            if self.frames[index + 1].strike:
                return (20 + (self.frames[index + 2].individualScore))
            else:
                return False
        else:
            return False

    def triple(self, index):
        if (index + 2) < len(self.frames) and (index + 2) < len(self.frames):
            if self.frames[index +1].strike and self.frames[index + 2].strike:
                return 30
            else:
                return  False
        else:
            return False

    def strikeBonus(self, index):
        strike = self.frames[index]
        score = 0
        if self.frames[index].lastFrame == False:
            if self.triple(index):
                score += self.triple(index)
            elif self.double(index):
                score += self.double(index)
            for i in range(0, (self.frames[index].getLen())):
                if self.frames[index + 1].roll[i] in self.symbols:
                    score += 10
                    score += self.symbols.find(self.frames[index + 1].roll[i])
        else:
            if self.triple(index):
                score += self.triple(index)
            elif self.frames[index].triple():
                score += self.frames[index].triple()
            else:
                score += strike.individualScore


        return score

    def spareBonus(self, index):
        score = 0
        if self.frames[index].lastFrame == False:
            for roll in range(self.frames[index + 1].getLen()):
                if roll == 0:
                    if self.frames[index + 1].roll[0].isdigit():
                        score += int(self.frames[index + 1].roll[0])
                    elif self.frames[index + 1].roll[0] == '-':
                        score += 0
                    elif self.frames[index + 1].roll[0] == 'X':
                        score += 10
                    elif self.frames[index + 1].roll[0] == '/':
                        scorePerFrame += 10
        else:
            return self.frames[index].individualScore
        return score + self.frames[index].individualScore






    def calculateScore(self):
        self.splitFrames()
        for i in range(0, len(self.frames)):
            self.frames[i].computeScore()
        for i in range(0, len(self.frames)):

            if self.frames[i].spare:
                self.score += self.spareBonus(i)

            elif self.frames[i].strike:
                self.score += self.strikeBonus(i)

            else:
                self.score += self.frames[i].individualScore




