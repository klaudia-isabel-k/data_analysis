import numpy as np

from functions.k_nearest_neighbour import get_k_nearest_neighbours

# Test distance function
dataset = np.array([[2.7810836, 2.550537003],
           [1.465489372, 2.362125076],
           [3.396561688, 4.400293529],
           [1.38807019, 1.850220317],
           [3.06407232, 3.005305973],
           [7.627531214, 2.759262235],
           [5.332441248, 2.088626775],
           [6.922596716, 1.77106367],
           [8.675418651, -0.242068655],
           [7.673756466, 3.508563011]])
neighbours = get_k_nearest_neighbours(dataset, [1.5, 2.3], 3)

exp_neighbours = np.array([[1.46548937, 2.36212508],[1.38807019, 1.85022032],[2.7810836, 2.550537 ]])
assert np.sum(np.round(neighbours - exp_neighbours, 5)) < 0.0001