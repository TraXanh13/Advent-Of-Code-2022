f = open("Day_6\input.txt", "r")

content = f.read()

code = set()

for charIndex in range(0, len(content)-4):

    for i in range(0, 4):
        code.add(content[charIndex+i])

    if (len(code) == 4):
        print(charIndex + 4)
        break

    code.clear()
