numList = [5, 10, 8, 6, 3, 2, 9, 1, 4, 7, 12, 13]
index = 8

trackerList = [numList[0]]

for i in range(len(numList)):
    for j in range(len(trackerList)):
        if numList[i]>trackerList[j] and len(trackerList)<index and numList[i] not in trackerList:
            trackerList.insert(j,numList[i])
        elif numList[i]>trackerList[j] and numList[i] not in trackerList:
            trackerList.pop()
            trackerList.insert(j, numList[i])

print("The {}th largest number in the list is: {}".format(index, trackerList[index-1]))

