import numpy as np

nRows = input()
nCol = 2
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
givenX = input()

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
i = 0
output = 0
while(i < len(givenData)):
	j = 0
	term = memotizationTable[i][i]
	while(j<i):
		term*=(givenX-givenData[j][0])
		j+=1
	output+=term
	i+=1
print(output)
