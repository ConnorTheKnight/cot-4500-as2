import numpy as np

givenData = [[7.2,23.5492],[7.4,25.3913],[7.5,26.8224],[7.6,27.4589]]
givenDegrees = [1,2,3]
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