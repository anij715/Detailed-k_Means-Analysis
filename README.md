In this repository, I have inclued three versions of k_Means, one with knee locator algorithm, one with individual SSE calculation for 3 clusters, another with individual SSE calculation for 7 clusters.
# k_Means-Analysis
![image](https://user-images.githubusercontent.com/35270511/118576150-f24a7080-b755-11eb-8ef4-4a282e19c80f.png)
- At k=3, sum of SSE is maximum, and with the increase in the value of k, sum of SSE is decreasing. And at k=7, the sum of SSE is minimum. But here, we cannot say that k=7 is the optimum no. of clusters just by comparing the sum of SSE. Sum of Squared Errors (SSE) is calculated by accounting the distances of each point from the nearest cluster center. Also, as the number of cluster centers increases (k), the individual SSE for each cluster decreases since one more cluster has been added. Hence, the sum of SSE will decrease with the increase in the value of k and will tend to zero. Imagine we set k to its maximum value n = 210 (n is the total no. of points in the datasets), each sample will form its own cluster meaning sum of squared distances equals zero. This implies, the curve will always tend to decrease. Hence, we cannot say that the k for which the sum of SSE is minimum is the optimum number of clusters.

- Now, we see that there is a knee point at k = 5. From this, we can say that after k=5 we are not getting much improvement clustering as when we were getting before k=5. This means, at k=5 we have a better clustering at the minimum cost (value of k).

![image](https://user-images.githubusercontent.com/35270511/118576156-f5456100-b755-11eb-9f37-b95345674b60.png)
- Here, we have the highest weighted purity for k=6, and after that, it decreased for k=7. For k=3, the weighted purity is minimum. We know that purity is the ratio between the dominant class in the cluster and the size of cluster. And weighted purity is calculated by summing the product of purity and samples of each cluster and then dividing it by the total number of samples in the dataset. So, we can say that the purity for each cluster at k=6 must be higher that is why the weighted purity is maximum. This means, at k=6, the dominant class to cluster samples ratio in each cluster is greater (purer) when compared with the clusters for other values of k, which implies that the clustering is better at k=6.

- From the above two plots and observations, we can see that k=5 is optimum when we are considering the sum of SSE, and k=6 is optimum when we are considering the weighted purity. 
- The weighted purity is maximum at k=6. 
- Also, the sum of SSE is lower at k=6 than that at k=5 even though k=5 is the knee point (we cannot consider k=7 as the cost (k) is high).
###### Note: We have not eliminated the outliers from the dataset, and they can affect the SSE values. Also, SSE alone is not enough to determine the optimum k value for the clustering, this is a drawback of k-Means.

