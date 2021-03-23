##import timeit
##
##
##code = """
##inputVal = 9164488995834946632
##currentVal = inputVal
##if len(str(inputVal)) % 2 == 0:
##    firstHalf = str(inputVal)[0:int(len(str(inputVal))/2)]
##    secondHalf = str(inputVal)[int(len(str(inputVal))/2):int(len(str(inputVal)))]
##else:
##    firstHalf = str(inputVal)[0:int((len(str(inputVal))-1)/2)]
##    secondHalf = str(inputVal)[int(len((str(inputVal))-1)/2):int(len(str(inputVal)))]
##    middleNum = str(inputVal)[int(len(str(inputVal))/2)]
##
##if firstHalf[::-1] < secondHalf:
##    if len(str(inputVal)) % 2 == 0:
##        firstHalf = str(int(firstHalf) + 1)
##        print(firstHalf+firstHalf[::-1])
##    else:
##        middleNum = str(int(middleNum) + 1)
##        print(firstHalf+middleNum +firstHalf[::-1])
##
##"""
##
##execution_time = timeit.timeit(code, number=1)
##
##print(execution_time)


inputVal = 9164488995834946632
currentVal = inputVal
if len(str(inputVal)) % 2 == 0:
    firstHalf = str(inputVal)[0:int(len(str(inputVal))/2)]
    secondHalf = str(inputVal)[int(len(str(inputVal))/2):int(len(str(inputVal)))]
else:
    firstHalf = str(inputVal)[0:int((len(str(inputVal))-1)/2)]
    secondHalf = str(inputVal)[(int(len((str(inputVal))))/2):(int(len(str(inputVal))))]
    middleNum = str(inputVal)[int(len(str(inputVal))/2)]

if firstHalf[::-1] < secondHalf:
    if len(str(inputVal)) % 2 == 0:
        firstHalf = str(int(firstHalf) + 1)
        print(firstHalf+firstHalf[::-1])
    else:
        middleNum = str(int(middleNum) + 1)
        print(firstHalf+middleNum+firstHalf[::-1])
