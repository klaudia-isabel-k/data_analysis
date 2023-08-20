import numpy as np

# calculate the Euclidean distance between two vectors
def euclidean_distance(model_values, compare_values):
    if len(compare_values.shape) == 1:
        compare_values = compare_values.reshape(1, compare_values.size)
    return np.sqrt(((model_values - compare_values) ** 2).sum(axis=1))

# Locate the most similar neighbors
def get_k_nearest_neighbours(neighbour_matrix, target_neighbour, k_num_neighbors):
    dist = euclidean_distance(target_neighbour, neighbour_matrix)
    distance_idx_dict = {dist: loc for loc, dist in enumerate(dist)}
    distance_idx_dict = sorted(distance_idx_dict.items(), key=lambda item: item[0])
    neighbours = list()
    for i in range(k_num_neighbors):
        neighbours.append(neighbour_matrix[distance_idx_dict[i][1]])
    return np.array(neighbours)