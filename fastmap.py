'''
FastMap
Author - Shreyas Kolpe
Date - 2/28/2018
'''

import numpy as np 
import math
import pandas as pd 
import matplotlib.pylab as plt
import seaborn as sns


# method to find the longest axis - the farthest pair of points along which to calculate coordinates
# returns the two endpoints ordered by their object ID
def findAxis(distMatrix):
	maxDist = float('-Inf')
	axisEnd1 = None
	axisEnd2 = None
	for i in range(10):
		for j in range(10):
			if(distMatrix[i][j] > maxDist):
				axisEnd1 = i
				axisEnd2 = j
				maxDist = distMatrix[i][j]

	return (axisEnd1, axisEnd2)

# method to update distances after projetion on to hyperplane
def updateDistMatrix(distMatrix, coordinates):
	for i in range(10):
		for j in range(10):
			distMatrix[i][j] = math.sqrt(distMatrix[i][j]**2 - (coordinates[i] - coordinates[j])**2)

# reading data
file = open("fastmap-data.txt","r")
distMatrix = np.zeros((10,10))
# construct the symmetric distance matrix
for line in file:
	values = line.split('\t')
	distMatrix[int(values[0])-1, int(values[1])-1] = int(values[2])
	distMatrix[int(values[1])-1, int(values[0])-1] = int(values[2])
file.close()

# read words corresponding to object IDs
file = open('fastmap-wordlist.txt')
wordList = file.read().split('\n')
file.close()

# initialize coordinates as empty
coordinates = np.empty((10,2))
# main loop for coordinate creation
for j in range(2):
	# fix the axis
	axisEnd1, axisEnd2 = findAxis(distMatrix)
	# calculate coordnates according to general pythogoras theorem
	for i in range(10):
		coordinates[i,j] = (distMatrix[axisEnd1,i]**2 + distMatrix[axisEnd1, axisEnd2]**2 - distMatrix[i,axisEnd2]**2)/(2*distMatrix[axisEnd1, axisEnd2])
	# change distance matrix to reflect projection onto plane perpendicular to axis
	updateDistMatrix(distMatrix, coordinates[:,j])

# dataframe for visualization
df = pd.DataFrame({
	'x': coordinates[:,0],
	'y': coordinates[:,1],
	'words': wordList
	})

# printing and plotting
print("The coordinates are - starting from object 1")
print(coordinates)
scatter = sns.regplot(data=df, x = 'x', y = 'y', fit_reg=False, marker='o', color='green')
for line in range(0,df.shape[0]):
	scatter.text(df.x[line]+0.2, df.y[line], df.words[line], horizontalalignment = 'left', size='medium', color='black')

plt.show()