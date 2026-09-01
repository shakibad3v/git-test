import numpy as np

data = np.array([1, 3, 5, 6, 7, 8, 9, 0, 4.5, 6, 9, 8])
print(data + 7)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)