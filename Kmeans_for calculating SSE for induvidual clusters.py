from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist, pdist
import numpy as np
import pandas as pd
import sys
import os
from math import sqrt 

f = open('seeds.csv' , 'r')
lines = f.read().splitlines()
f.close()
items = []
classVar = []

for i in range(0, len(lines)):
  line = lines[i].split('\t')
  itemFeatures = []
  classVar.append(float(line[7])) #storing class variables in a seperate array
  for j in range(len(line)-1):
    try:
      v = float(line[j])

    except ValueError:
      continue #the float was not a number then ignore the number and skip

    itemFeatures.append(v)
  items.append(itemFeatures)

kmeans = KMeans(n_clusters=4, random_state=0).fit(items)
centroids = kmeans.cluster_centers_
#distance = kmeans.fit_transform(items)
labels = kmeans.labels_

SSE = SSE1 = SSE2 = SSE3 = SSE4 = 0
i = 0
clv1 = clv2 = clv3 = clv4 = 0

for label in labels:
  if label == 0:
    clv1 = clv1 + 1
  elif label == 1:
    clv2 = clv2 + 1
  elif label == 2:
    clv3 = clv3 + 1
  elif label == 3:
    clv4 = clv4 + 1
    

clv0_1 = 0
clv0_2 = 0
clv0_3 = 0
purity0 = 0
clv1_1 = 0
clv1_2 = 0
clv1_3 = 0
purity1 = 0
clv2_1 = 0
clv2_2 = 0
clv2_3 = 0
purity2 = 0
clv3_1 = 0
clv3_2 = 0
clv3_3 = 0
purity3 = 0

for label in labels:
 if (label == 0):
    SSE1 = SSE1 + pow((items[i][0] - centroids[0][0]), 2) + pow((items[i][1] - centroids[0][1]), 2) +\
                  pow((items[i][2] - centroids[0][2]), 2) + pow((items[i][3] - centroids[0][3]), 2) +\
                  pow((items[i][4] - centroids[0][4]), 2) + pow((items[i][5] - centroids[0][5]), 2) +\
                  pow((items[i][6] - centroids[0][6]), 2)
    
    if classVar[i] == 1:
      clv0_1 = clv0_1 + 1

    elif classVar[i] == 2:
      clv0_2 = clv0_2 + 1
    
    elif classVar[i] == 3:
      clv0_3 = clv0_3 + 1

    i = i + 1



 elif (label == 1):
    SSE2 = SSE2 + pow((items[i][0] - centroids[1][0]), 2) + pow((items[i][1] - centroids[1][1]), 2) +\
                  pow((items[i][2] - centroids[1][2]), 2) + pow((items[i][3] - centroids[1][3]), 2) +\
                  pow((items[i][4] - centroids[1][4]), 2) + pow((items[i][5] - centroids[1][5]), 2) +\
                  pow((items[i][6] - centroids[1][6]), 2)
    if classVar[i] == 1:
      clv1_1 = clv1_1 + 1

    elif classVar[i] == 2:
      clv1_2 = clv1_2 + 1
    
    elif classVar[i] == 3:
      clv1_3 = clv1_3 + 1

    i = i + 1



 elif (label == 2):
    SSE3 = SSE3 + pow((items[i][0] - centroids[2][0]), 2) + pow((items[i][1] - centroids[2][1]), 2) +\
                  pow((items[i][2] - centroids[2][2]), 2) + pow((items[i][3] - centroids[2][3]), 2) +\
                  pow((items[i][4] - centroids[2][4]), 2) + pow((items[i][5] - centroids[2][5]), 2) +\
                  pow((items[i][6] - centroids[2][6]), 2)
    if classVar[i] == 1:
      clv2_1 = clv2_1 + 1

    elif classVar[i] == 2:
      clv2_2 = clv2_2 + 1
    
    elif classVar[i] == 3:
      clv2_3 = clv2_3 + 1

    i = i + 1

 elif (label == 3):
    SSE4 = SSE4 + pow((items[i][0] - centroids[3][0]), 2) + pow((items[i][1] - centroids[3][1]), 2) +\
                  pow((items[i][2] - centroids[3][2]), 2) + pow((items[i][3] - centroids[3][3]), 2) +\
                  pow((items[i][4] - centroids[3][4]), 2) + pow((items[i][5] - centroids[3][5]), 2) +\
                  pow((items[i][6] - centroids[3][6]), 2)

    if classVar[i] == 1:
      clv3_1 = clv3_1 + 1

    elif classVar[i] == 2:
      clv3_2 = clv3_2 + 1
    
    elif classVar[i] == 3:
      clv3_3 = clv3_3 + 1

    i = i + 1

SSE = SSE1 + SSE2 + SSE3 + SSE4
max0 = max(clv0_1, clv0_2, clv0_3)
max1 = max(clv1_1, clv1_2, clv1_3)
max2 = max(clv2_1, clv2_2, clv2_3)
max3 = max(clv3_1, clv3_2, clv3_3)

purity0 = max0 / len(classVar)
purity1 = max1 / len(classVar)
purity2 = max2 / len(classVar)
purity3 = max3 / len(classVar)

wpurity0 = purity0 * clv1 
wpurity1 = purity1 * clv2 
wpurity2 = purity2 * clv3 
wpurity3 = purity3 * clv4 

wpurity = (wpurity0 + wpurity1 + wpurity2 + wpurity3) / len(classVar)

print("SSE for Cluster 0 = " , (SSE1))
print("SSE for Cluster 1 = " , (SSE2))
print("SSE for Cluster 2 = " , (SSE3))
print("SSE for all Clusters = " , (SSE))
print("Purity for Cluster 0 = ", purity0)
print("Purity for Cluster 1 = ", purity1)
print("Purity for Cluster 2 = ", purity2)
print("Purity for Cluster 3 = ", purity3)

print("Weighted Purity for Clusters = ", wpurity)


#print(len(kmeans.labels_))
#print(len(items))
#print(kmeans.cluster_centers_) #to get all the centroids
#print(kmeans.inertia_) #SSE for all clusters
#print(kmeans.labels_) #cluster to which every points belong to
