# K-Means Clustering Analysis on the Seeds Dataset

This project performs a detailed analysis to determine the optimal number of clusters (k) for the k-Means algorithm when applied to the public "seeds" dataset. The analysis uses two distinct metrics for evaluation: the Sum of Squared Errors (SSE) via the Elbow Method and the Weighted Purity score.


## 📜 Project Objective

The goal is to identify the best value for 'k' by comparing the results from two different evaluation techniques. This highlights the common machine learning challenge where different metrics can suggest different optimal parameters, requiring a deeper analysis to make a final decision.

---

## 💾 Dataset

The analysis is performed on the **Seeds dataset**, which contains measurements of geometrical properties of wheat kernels belonging to three different varieties: Kama, Rosa, and Canadian. The dataset has 210 instances, each with 7 feature attributes and 1 target class attribute.

---

## 🛠️ Methodology

To find the optimal 'k', the project evaluates the clustering performance for k values from 1 to 7 using the following methods:

* **Elbow Method (Sum of Squared Errors - SSE)**: SSE measures the total squared distance between each data point and its assigned cluster's center. A lower SSE generally means better clustering. We look for the "elbow point" on the SSE vs. k graph, which represents a good trade-off between cost (k) and performance. This project uses the `kneed` library's `KneeLocator` to programmatically find this point.
* **Weighted Purity**: Since the dataset includes true labels, purity can be calculated. Purity measures the extent to which each cluster contains data points from a single class. A higher purity score signifies better clustering that aligns with the ground truth.

---

## 🛠️ Discussion

![image](https://user-images.githubusercontent.com/35270511/118576150-f24a7080-b755-11eb-8ef4-4a282e19c80f.png)
- At k=3, sum of SSE is maximum, and with the increase in the value of k, sum of SSE is decreasing. And at k=7, the sum of SSE is minimum. But here, we cannot say that k=7 is the optimum no. of clusters just by comparing the sum of SSE. Sum of Squared Errors (SSE) is calculated by accounting the distances of each point from the nearest cluster center. Also, as the number of cluster centers increases (k), the individual SSE for each cluster decreases since one more cluster has been added. Hence, the sum of SSE will decrease with the increase in the value of k and will tend to zero. Imagine we set k to its maximum value n = 210 (n is the total no. of points in the datasets), each sample will form its own cluster meaning sum of squared distances equals zero. This implies, the curve will always tend to decrease. Hence, we cannot say that the k for which the sum of SSE is minimum is the optimum number of clusters.

- Now, we see that there is a knee point at k = 5. From this, we can say that after k=5 we are not getting much improvement clustering as when we were getting before k=5. This means, at k=5 we have a better clustering at the minimum cost (value of k).

![image](https://user-images.githubusercontent.com/35270511/118576156-f5456100-b755-11eb-9f37-b95345674b60.png)
- Here, we have the highest weighted purity for k=6, and after that, it decreased for k=7. For k=3, the weighted purity is minimum. We know that purity is the ratio between the dominant class in the cluster and the size of cluster. And weighted purity is calculated by summing the product of purity and samples of each cluster and then dividing it by the total number of samples in the dataset. So, we can say that the purity for each cluster at k=6 must be higher that is why the weighted purity is maximum. This means, at k=6, the dominant class to cluster samples ratio in each cluster is greater (purer) when compared with the clusters for other values of k, which implies that the clustering is better at k=6.

- From the above two plots and observations, we can see that k=5 is optimum when we are considering the sum of SSE, and k=6 is optimum when we are considering the weighted purity. 
- The weighted purity is maximum at k=6. 
- Also, the sum of SSE is lower at k=6 than that at k=5 even though k=5 is the knee point (we cannot consider k=7 as the cost (k) is high).

---

## ⚙️ How to Run the Project

### Prerequisites

Ensure you have Python 3 installed, along with the following libraries:
* pandas
* scikit-learn
* matplotlib
* numpy

You can install them using pip:
```bash
pip install pandas scikit-learn matplotlib numpy kneed
```

### Execution

To run the main analysis and generate the SSE plot, execute the primary script:
```bash
python Kmeans-with-knee-locator.py
```

---

## 📊 Results and Analysis

The analysis produced two key findings:

1.  **Optimal k based on SSE**: The plot of SSE versus the number of clusters shows a distinct "elbow" at **k=5**. This is the point where increasing the number of clusters stops providing a significant reduction in SSE.
2.  **Optimal k based on Weighted Purity**: The calculation of weighted purity revealed that the highest score was achieved at **k=6**. This indicates that a 6-cluster solution does the best job of grouping data points from the same original wheat variety.


### Conclusion

From the analysis, we have a conflict:
- The Elbow Method suggests **k=5** is optimal.
- The Weighted Purity metric suggests **k=6** is optimal.

Given that the SSE for k=6 is lower than for k=5 and that k=6 produces "purer" clusters that better reflect the true labels, **k=6 is arguably the better choice for this specific dataset**. This demonstrates the limitation of relying solely on SSE for determining the optimal number of clusters.

*__Note__: The dataset was not pre-processed to remove outliers, which can influence SSE values.*

---

## 🚀 Future Work

* **Outlier Removal**: Implement a pre-processing step to identify and handle outliers to see how it affects the SSE and the location of the elbow point.
* **Alternative Metrics**: Incorporate other clustering evaluation metrics like the **Silhouette Score** or **Calinski-Harabasz Index** to see if they corroborate the findings from the Elbow Method or Purity score.
* **Explore Other Algorithms**: Compare the results of k-Means with other clustering algorithms like DBSCAN or Gaussian Mixture Models.
