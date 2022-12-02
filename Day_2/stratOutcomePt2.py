'''
Shape Score:
    1 = Rock
    2 = Paper
    3 = Scissors

Outcome score:
    0 = Lost
    3 = Draw
    6 = Win

Symbols:
    Opponent
        A = Rock
        B = Paper
        C = Scissors
    Needed Outcome
        X = Lose
        Y = Draw
        Z = Win
'''
from enum import Enum

totalScore = 0

f = open('Day_2\RPS_Strat.txt', 'r')


class outcome(Enum):
    win = 6
    draw = 3
    lose = 0


class shape(Enum):
    rock = 1
    paper = 2
    scissors = 3


rpsDict = {
    'A X': outcome.lose.value + shape.scissors.value,
    'A Y': outcome.draw.value + shape.rock.value,
    'A Z': outcome.win.value + shape.paper.value,
    'B X': outcome.lose.value + shape.rock.value,
    'B Y': outcome.draw.value + shape.paper.value,
    'B Z': outcome.win.value + shape.scissors.value,
    'C X': outcome.lose.value + shape.paper.value,
    'C Y': outcome.draw.value + shape.scissors.value,
    'C Z': outcome.win.value + shape.rock.value
}

for x in f:
    totalScore += rpsDict[x.strip('\n')]

print(totalScore)
