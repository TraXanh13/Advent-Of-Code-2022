f = open("Day_6\input.txt", "r")

content = f.read()

code = set()

for charIndex in range(0, len(content)-14):

    for i in range(0, 14):
        code.add(content[charIndex+i])

    if (len(code) == 14):
        print(charIndex + 14)
        break

    code.clear()
