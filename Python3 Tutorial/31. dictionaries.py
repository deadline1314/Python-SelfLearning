# unordered unsorted data set

exDict = {'Jack': [15, 'blonde'], 'Bob': [22, 'brown'], 'Alice': [12, 'black'], 'Kevin': [17, 'gold']}

print(exDict)
print(exDict['Jack'][1])

exDict['Tim'] = [14, 'yellow']
print(exDict)

exDict['Tim'] = [50, 'red']
print(exDict)

del exDict['Jack']
print(exDict)
