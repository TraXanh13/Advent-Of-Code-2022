'''
2 compartments (half of the line of text)

Each compartment should contain unique values (both sides can't have the same letter)
'''

import itertools as it
f = open('Day_3\input.txt', 'r')
# f = open('Day_3\example.txt', 'r')

dups = []
letterErrs = {}
letterErrs = set()


def pt1():
    totalErrors = 0
    for line in f:
        firstHalf = line[:len(line)//2]
        secondHalf = line[len(line)//2:]
        checkSimilar(firstHalf, secondHalf)
        totalErrors += getLetterVal()

    print(totalErrors)


def checkSimilar(ln1, ln2):
    for i in range(len(ln1)):
        for j in range(len(ln2)):
            if ln1[i] == ln2[j]:
                letterErrs.add(ln1[i])


def getLetterVal():
    totalScore = 0
    for x in letterErrs:
        if (x.islower()):
            totalScore += ord(x) - ord('a') + 1
        else:
            totalScore += ord(x) - ord('A') + 27

    letterErrs.clear()
    return totalScore


if __name__ == '__main__':
    pt1()
