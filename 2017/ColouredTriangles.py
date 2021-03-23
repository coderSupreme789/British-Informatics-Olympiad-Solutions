firstLine = list(str(input()))

iters = len(firstLine) - 1
nextLine = firstLine
for i in range(iters):
    tempLine= []
    for i in range(len(nextLine)-1):
        if nextLine[i] == nextLine[i+1]:
            tempLine.append(nextLine[i])
        else:
            colours = ["R", "G", "B"]
            colours.remove(nextLine[i])
            colours.remove(nextLine[i+1])
            tempLine.append(colours[0])
    nextLine = tempLine
    print(nextLine)


print(nextLine[0])
