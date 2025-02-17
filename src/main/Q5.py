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

matrixA = []
a = []
h = []
b = []
x = []
n = len(givenData)-1

i = 0
while(i<len(givenData)):
	a.append(givenData[i][1])	
	i+=1

i = 0
while(i<n):
	h.append(givenData[i+1][0]-givenData[i][0])
	i+=1

b.append(0)
i = 1
while(i<n):
	b.append(((3/h[i])*(a[i+1]-a[i]))-((3/h[i-1])*(a[i]-a[i-1])))
	i+=1
b.append(0)

i=0
while(i<n+1):
	x.append(0)
	i+=1

i = 0
while(i < n+1):
	j = 0
	matrixA.append([])
	while(j < n+1):
		matrixA[i].append(0)
		j+=1
	i+=1
i = 1
matrixA[0][0] = 1
matrixA[n][n] = 1
while(i < n):
	matrixA[i][i-1] = h[i-1]
	matrixA[i][i] = 2*(h[i-1]+h[i])
	matrixA[i][i+1] = h[i]
	i+=1

x[0] = b[0]
x[n] = b[n]

Iota = [1]
Mu = [0]
Zeta = [0]
i = 1
while(i < n):
	Iota.append((2*(givenData[i+1][0]-givenData[i-1][0]))-(h[i-1]*Mu[i-1]))
	Mu.append(h[i]/Iota[i])
	Zeta.append((b[i]-(h[i-1]*Zeta[i-1]))/Iota[i])
	i+=1
Iota.append(1)
Zeta.append(0)
i = n-1
while(i >= 0):
	x[i] = Zeta[i] - (Mu[i]*x[i+1])
	i-=1

output = ""
i = 0
while(i < n+1):
	j = 0
	output += "["
	while(j < n+1):
		output += " " + str(matrixA[i][j])
		j+=1
	output += "]\n"
	i+=1

print(output, end="")
output = "["
i=0
while(i<n+1):
	output += " " + str(b[i])
	i+=1
output+="]"
print(output)
output = "["
i=0
while(i<n+1):
	output += " " + str(x[i])
	i+=1
output+="]"
print(output)
