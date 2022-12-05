# crates = {
#     1: ['Z', 'N'],
#     2: ['M', 'C', 'D'],
#     3: ['P']
# }

# f = open('Day_5\example.txt', 'r')

crates = {
    1: ['H', 'C', 'R'],
    2: ['B', 'J', 'H', 'L', 'S', 'F'],
    3: ['R', 'M', 'D', 'H', 'J', 'T', 'Q'],
    4: ['S', 'G', 'R', 'H', 'Z', 'B', 'J'],
    5: ['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B'],
    6: ['T', 'H', 'C', 'G'],
    7: ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L'],
    8: ['R', 'J', 'Q', 'G', 'C'],
    9: ['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']
}

f = open('Day_5\movement.txt', 'r')

'''val is Move, From, To'''


def moveCrates(val):
    if (val[0] > 0):
        for i in range(0, val[0], 1):
            crates[val[2]].append(crates[val[1]].pop())


for line in f:
    if line.startswith('move'):
        val = []
        for seg in line.split():
            if seg.isdigit():
                val.append(int(seg))
        moveCrates(val)

topItems = ''

for i in crates:
    topItems += (crates[i][-1])

print(topItems)
