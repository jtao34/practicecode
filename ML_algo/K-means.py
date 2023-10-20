def kMeans(X, k, max_iter):
    #random k centroids
    centroid = X[np.random.choice(X.shape[0], k, replace = False)]
    #for each centroid, find distance to other points and return cluster
    for _ in range(max_iter):
        cluster = []
        for p in X:
            distance = [euclidian_distence(p, i) for i in centroid]
            cluster.append(np.argmin(distance))
        #then update new centroid
        new_centroid = []
        for i in range(k):
            cluster_points = X[np.array(cluster) == i]
            if cluster_points:
                new_centroid.append(np.mean(cluster_points, axis = 0))
            else:
                new_centroid.append(centroid[i])
        new_centroid = np.array(new_centroid)
        if np.all(new_centroid == centroid):
            break
        centroid = new_centroid
    return centroid, cluster