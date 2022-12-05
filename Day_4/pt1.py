f = open('Day_4\input.txt', 'r')

redundancy = 0


def checkVal(r1, r2):
    global redundancy
    if int(r1[0]) in range(int(r2[0]), int(r2[1])+1):
        if int(r1[1]) in range(int(r2[0]), int(r2[1])+1):
            redundancy += 1


for line in f:
    rangeOne = line.strip('\n').split(',')[0].split('-')
    rangeTwo = line.strip('\n').split(',')[1].split('-')
    if (rangeOne == rangeTwo):
        redundancy += 1
    else:
        checkVal(rangeOne, rangeTwo)
        checkVal(rangeTwo, rangeOne)

print(redundancy)
