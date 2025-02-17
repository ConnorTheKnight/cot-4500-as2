import numpy as np

nRows = input()
nCol = input()
givenData = []
i = 0
while(i<nRows):
    givenData.append([])
    int j = 0
    temp = input().split()
    while(j<nCol):
        givenData[i].append(float(temp[j]))
        j+=1
    i+=1
givenDegreeTemp = input().split
givenDegrees = []
for(degree in givenDegreesTemp):
    givenDegrees.append(int(degree))

memotizationTable = []
reached = []
i = 0
while(i < len(givenData)):
	j = 1
	memotizationTable.append([givenData[i][1]])
	reached.append([True])
	while(j < len(givenData)):
		memotizationTable[i].append(0)
		reached[i].append(False)
		j+=1
	i+=1

def calcF(k, divDiffNum):
	FleftUpper = memotizationTable[k-1][divDiffNum-1]
	Fleft = memotizationTable[k][divDiffNum-1]
	if(not reached[k-1][divDiffNum-1]):
		calcF(k-1, divDiffNum-1)
		FleftUpper = memotizationTable[k-1][divDiffNum-1]
	if(not reached[k][divDiffNum-1]):
		calcF(k, divDiffNum-1)
		Fleft = memotizationTable[k][divDiffNum-1]
	Xn = givenData[k][0]
	X0 = givenData[k - divDiffNum][0]
	memotizationTable[k][divDiffNum] = (Fleft-FleftUpper)/(Xn-X0)
	reached[k][divDiffNum] = True

calcF(len(givenData)-1, len(givenData)-1)
for degree in givenDegrees:
	print(memotizationTable[degree][degree])