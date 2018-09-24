from math import log

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def createDataSet():
    dataSet = [[1,1,'y'], 
    [1,0,'n'],
    [1,1,'y'],
    [0,1,'n'],
    [0,1,'n']]

    labels = ['no surfacing', 'flippers']
    return dataSet, labels


if __name__ == '__main__':
    myDat, labels = createDataSet()
    shannonEnt = calcShannonEnt(myDat)
    print(myDat, labels, shannonEnt)





