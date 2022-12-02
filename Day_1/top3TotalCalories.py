from array import *

currCal = 0

f = open("Day_1\elf-calories.txt", "r")

# Create an array of 3 elements, all initialized to 0
top3 = []

for x in f:
    if (x == '\n'):
        if (len(top3) < 3):
            top3.append(currCal)
        else:
            top3.sort()
            if (currCal > top3[0]):
                top3[0] = currCal
        currCal = 0
    else:
        currCal += int(x)

print(sum(top3))
