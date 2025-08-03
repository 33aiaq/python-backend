import math
import statistics
import utils


numbers = utils.get_numbers_from_user()

total = sum(numbers)
mean = statistics.mean(numbers)
stdev = statistics.stdev(numbers) if len(numbers) > 1 else 0
max_num = max(numbers)
min_num = min(numbers)

print("Statistics Summary:")
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Mean (Average): {mean}")
print(f"Standard Deviation: {stdev}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")
