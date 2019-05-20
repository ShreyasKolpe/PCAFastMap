'''
PCA
Author - Shreyas Kolpe
Date - 2/28/2018
'''

import numpy as np 

# read data
file = open("pca-data.txt", "r")
points = []
for line in file:
	values = line.split('\t')
	points.append([float(values[0]), float(values[1]), float(values[2])])
file.close()

# store in numpy.ndarray
points = np.array(points, dtype=np.float64)

# get shape of data into N - number of samples and d- number of dimensions
N, d = points.shape

# calculate the means of the data
mean = points.sum(axis=0)/N

# center the data around the mean
X = points - mean

# calculate covariance matrix
covariance = X.transpose().dot(X)/N

# extract eigenvalues and eigenvectors from covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(covariance)

# sort eigen values in descending order and extract indices
sortedEigenIndex = np.argsort(-eigenvalues)

# construct Utruncated by taking first d-1 eigen vectors
Utruncated = eigenvectors[:,sortedEigenIndex[0:2]]

# report the principal components
print("Direction of first principal component - ")
print(Utruncated[:,0])
print("Direction of second principal component - ")
print(Utruncated[:,1])