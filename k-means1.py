import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data = list(zip(x, y))
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()