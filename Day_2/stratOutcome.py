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
    Player
        X = Rock
        Y = Paper
        Z = Scissors
'''
totalScore = 0

f = open('Day_2\RPS_Strat.txt', 'r')

rpsDict = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

for x in f:
    totalScore += rpsDict[x.strip('\n')]

print(totalScore)
