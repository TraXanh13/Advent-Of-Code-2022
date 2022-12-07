class Path:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []


paths = {}


def calcSize():
    total = 0
    for path in paths.values():
        childTotal = 0
        for child in path.children:
            childTotal += paths[child].size
        if (path.size < 100000):
            total += path.size
        if (childTotal < 100000):
            total += childTotal

    return total


with open("Day_7\input.txt", "r") as f:
    root = Path("/", 0, None)
    currPath = root.name
    paths['/'] = root

    for line in f:
        line = line.strip('\n').split(" ")
        if (line[0] == "$" and line[1] == "cd"):
            if (line[2] == "/"):
                currPath = root.name
            elif (line[2] == ".." and paths[currPath].parent != None):
                currPath = paths[currPath].parent
            else:
                if (line[2] not in paths.keys()):
                    newPath = Path(line[2], 0, currPath)
                    paths[currPath].children.append(newPath.name)
                    paths[newPath.name] = newPath
                    currPath = newPath.name
                else:
                    currPath = paths[line[2]].name
        elif (line[0].isdigit()):
            paths[currPath].size += int(line[0])

print(f'Total: {calcSize()}')
