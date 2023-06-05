import matplotlib.pyplot as plt
import seaborn as sns;
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import random

sns.set()

def data_distribution(array, cluster, k, n, dim):
    cluster_content = [[] for i in range(k)]

    for i in range(n):
        min_distance = float('inf')
        situable_cluster = -1
        for j in range(k):
            distance = 0
            for q in range(dim):
                distance += (array[i][q] - cluster[j][q]) ** 2

            distance = distance ** (1 / 2)
            if distance < min_distance:
                min_distance = distance
                situable_cluster = j

        cluster_content[situable_cluster].append(array[i])

    return cluster_content


def cluster_update(cluster, cluster_content, dim):
    k = len(cluster)
    for i in range(k):  # по i кластерам
        for q in range(dim):  # по q параметрам
            updated_parameter = 0
            for j in range(len(cluster_content[i])):
                updated_parameter += cluster_content[i][j][q]
            if len(cluster_content[i]) != 0:
                updated_parameter = updated_parameter / len(cluster_content[i])
            cluster[i][q] = updated_parameter
    return cluster


def clusterization(array, k):
    n = len(array)
    dim = len(array[0])

    cluster = [[0 for i in range(dim)] for q in range(k)]
    cluster_content = [[] for i in range(k)]

    for i in range(dim):
        for q in range(k):
            cluster[q][i] = random.randint(0, 1000)

    cluster_content = data_distribution(array, cluster)

    previous_cluster = cluster.copy()
    while 1:
        cluster = cluster_update(cluster, cluster_content, dim)
        cluster_content = data_distribution(array, cluster)
        if cluster == previous_cluster:
            break
        previous_cluster = cluster.copy()
    return cluster_content, cluster


def visualisation_2d(cluster_content):
    k = len(cluster_content)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")

    for i in range(k):
        x_coordinates = []
        y_coordinates = []
        for q in range(len(cluster_content[i])):
            x_coordinates.append(cluster_content[i][q][0])
            y_coordinates.append(cluster_content[i][q][1])
        plt.scatter(x_coordinates, y_coordinates)
    plt.show()


if __name__ == "__main__":
    randomint = random.randint(0, 1000)
    X, y_true = make_blobs(n_samples=500, centers=6,
                           cluster_std=0.40, random_state=randomint) # Создание Гауссовых точек для кластеризации
    X_first = X.copy()
    Y = y_true.copy()
    kmeans = KMeans(n_clusters=6)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    plt.figure(1)
    plt.scatter(X_first[:, 0], X_first[:, 1], s=50)

    plt.figure(2)
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()