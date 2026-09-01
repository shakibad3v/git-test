import numpy as np

data = np.array([1, 3, 5, 6, 7, 8, 9, 0, 4.5, 6, 3])
print(data + 3)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)