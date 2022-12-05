f = open('Day_4\input.txt', 'r')

overlaps = 0

for lines in f:
    e1Range = lines.strip('\n').split(',')[0].split('-')
    e2Range = lines.strip('\n').split(',')[1].split('-')
    for x in range(int(e2Range[0]), int(e2Range[1])+1):
        if (x in range(int(e1Range[0]), int(e1Range[1])+1)):
            overlaps += 1
            break

print(overlaps)
