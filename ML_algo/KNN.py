import collections
def KNN(X, y, new_point, k):
    #calculate dist to all labeled points
    dist = []
    for i in range(len(X)):
        distance = euclidian_distance(i, new_point)
        dist.append((distance, y[i]))
    dist.sort(lambda x:x[0])
    cur_sample = dist[:k]
    cnt = collections.defaultdict()
    cur_max = 0
    for i in cur_sample:
        cnt[i[1]] += 1
        if cnt[i[1]] > cur_max:
            cur_max = i[1]
    return cur_max

# Example usage:
# X = np.random.rand(100, 2)  # Replace with your data
# y = np.random.randint(2, size=100)  # Replace with your labels
# new_point = np.array([0.5, 0.5])  # Replace with the point you want to classify
# k = 5  # Number of neighbors to consider
# result = KNN(X, y, new_point, k)
# print(result)