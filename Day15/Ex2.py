import numpy as np

arr = np.random.randint(1, 101, size=(10, 10))
print("Original Array:\n", arr)

mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

print("\nMean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)

diagonal = np.diag(arr)
print("\nMain Diagonal:", diagonal)

greater_than_80 = arr[arr > 80]
print("\nValues greater than 80:", greater_than_80)

arr[arr < 30] = 0
print("\nModified Array (values < 30 replaced with 0):\n", arr)
