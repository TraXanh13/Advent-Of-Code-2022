mostCal = 0
currCal = 0

f = open("Day_1\elf-calories.txt", "r")

for x in f:
    if (x == '\n'):
        if currCal > mostCal:
            mostCal = currCal
        currCal = 0
    else:
        currCal += int(x)

print(mostCal)
