import numpy as np

nRows = input()
nCol = 3
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

memotizationTable = []
reached = []
i = 0
while(i < len(givenData)*2):
	j = 2
	memotizationTable.append([givenData[int(i/2)][1]])
	reached.append([True])
	if(i%2==1):
		memotizationTable[i].append(givenData[int(i/2)][2])
		reached[i].append(True)
	else:
		memotizationTable[i].append(0)
		reached[i].append(False)
	while(j < len(givenData)*2):
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
	Xn = givenData[int(k/2)][0]
	X0 = givenData[int((k - divDiffNum)/2)][0]
	memotizationTable[k][divDiffNum] = (Fleft-FleftUpper)/(Xn-X0)

calcF((len(givenData)*2)-1, (len(givenData)*2)-1)
i = 0
output = ""
while(i < len(givenData)*2):
	j = 0
	output += "[ {Value: .8e}".format(Value=givenData[int(i/2)][0])
	while(j<(len(givenData)-1)*2):
		output += " {Value: .8e}".format(Value=memotizationTable[i][j])
		j+=1
	output += "]\n"
	i+=1
print(output)
