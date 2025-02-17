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
givenDegree = input()
givenXvalue = input()

memotizationTable = []
reached = []
i = 0
while(i < len(givenData)):
	j = 1
	memotizationTable.append([givenData[i][1]])
	reached.append([True])
	while(j < givenDegree+1):
		memotizationTable[i].append(0)
		reached[i].append(False)
		j+=1
	i+=1

def calcP(n, degree):
	if(not reached[n-1][degree-1]):
		calcP(n-1, degree-1)
	if(not reached[n][degree-1]):
		calcP(n, degree-1)
	Pni = memotizationTable[n-1][degree-1]
	Pnj = memotizationTable[n][degree-1]
	j = n-degree
	i = n
	memotizationTable[n][degree] = (((givenXvalue-givenData[j][0])*Pnj)-((givenXvalue-givenData[i][0])*Pni))/(givenData[i][0]-givenData[j][0])
	reached[n][degree] = True

calcP(len(givenData)-1, givenDegree)
print(memotizationTable[len(givenData)-1][givenDegree])
