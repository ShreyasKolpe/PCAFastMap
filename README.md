# PCA and FastMap

Both PCA and FastMap are unsupervised schemes. PCA is primarily used for reducing the dimension of the data while minimizing the loss of information. 

## PCA

The program `pca.py` reads data from `pca-data.txt` and stores it in the `numpy` `ndarray` object `points`.
To calculate the covariance matrix, the data needs to be centered on the mean. Therefore `mean` is calculated, and X, the data matrix is calculated as the mean centered data.
The covariance matrix `covariance` is built as the product of the data matrix and its transpose, normalized by N – the number of data points.
The eigen values and corresponding eigen vectors are extracted from covariance. `sortedEigenIndex` gives the indices of the eigenvalues sorted in descending order. This `sortedEigenIndex` is used to extract the two columns from eigenvectors corresponding to the eigenvectors for the largest two eigenvalues.
These vectors represent the direction of the first principal component and second principal component respectively (for retaining the first two dimensions).

## FastMap

[FastMap](https://www.researchgate.net/publication/2609830_FastMap_A_Fast_Algorithm_for_Indexing_Data-Mining_and_Visualization_of_Traditional_and_Multimedia_Datasets) is an algorithm to find numerical representations (vectors) for data points that don't have such a representation, but there is a similarity metric that computes the similarity for two objects. This representation must give similar vectors for objects that are similar to each other. FastMap has O(N^2) complexity compared to methods like Multi Dimensional Scaling with O(N^3).

The problem in this case is to give a two-dimensional vector for a number of words in `fastmap-wordlist.txt`, with `fastmap-data.txt` containing the edit distance between pairs of words to be used as the similarity metric.

The program `fastmap.py` is organized as follows –
* Method to find the axis along which to calculate coordinates – `findAxis(distMatrix)` – returns `(axisEnd1, axisEnd2)`, the object IDs representing the endpoints of the longest axis between objects. `axisEnd1` is the smaller object ID of the two.
* Method to find the axis along which to calculate coordinates – `updateDistMatrix(distMatrix, coordinates)` – After the latest round of the coordinate creation loop, it updates the distance matrix distMatrix with the new distance where `coordinates` is the latest computed coordinate for all the points.

        D'(oi, oj) = sqrt(D(oi, oj)^2 - (xi - xj)^2)
* The code that follows loads the data from `fastmap-data.txt` and constructs the symmetric distance matrix `distMatrix` using the data read from the file.
Following that, `wordList` is initialized with the words read from `fastmap-wordlist.txt`.
The coordinate matrix coordinates is initialized to be an empty `numpy` `ndarray` of shape (10,2). Since there are two coordinates to be created, we loop twice, calculating the coordinates for all the points within the loop. Firstly, the axis for projection is found as the farthest pair of objects by calling `findAxis()`. `axisEnd1` is the lesser object ID compared to `axisEnd2`. Then for each of the points, the first coordinate is calculated using the formula:

        xi = (dai^2 + dab^2 - dbi^2)/2dab

    After this one round, the distance matrix is updated by calling `updateDistMatrix()`. The next iteration will similarly calculate the second coordinate.
Finally the coordinates are displayed and the points represented by them are plotted along with the labels of the words they correspond to.
