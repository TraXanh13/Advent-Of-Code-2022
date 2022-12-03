from collections import Counter

badgeScore = 0

# with open('Day_3\example.txt', 'r') as file:
with open('Day_3\input.txt', 'r') as file:
    f = file.readlines()


def pt2():
    for lines in range(2, len(f), 3):
        elf1, elf2, elf3 = Counter(
            f[lines-2]), Counter(f[lines-1]), Counter(f[lines])
        commonItem = elf1 & elf2 & elf3
        addScore(commonItem.most_common(1)[0][0])

    print(badgeScore)


def addScore(i):
    global badgeScore
    if (i.islower()):
        badgeScore += ord(i) - ord('a') + 1
    else:
        badgeScore += ord(i) - ord('A') + 27


if __name__ == '__main__':
    pt2()
