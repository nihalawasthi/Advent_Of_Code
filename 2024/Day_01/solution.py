import numpy as np

def calculate_total_distance(file_path):
    data = np.loadtxt(file_path)
    left_list = data[:, 0]
    right_list = data[:, 1]
    left_sorted = np.sort(left_list)
    right_sorted = np.sort(right_list)
    distances = np.abs(left_sorted - right_sorted)
    total_distance = np.sum(distances)
    return total_distance

file_path = 'day_1.txt'
total_distance = calculate_total_distance(file_path)

print(f"The total distance between the two lists is: {total_distance}")
