def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield sign * num
        sign *= -1

nums = [1, 2, 3, 4, 5]
for val in alternating_signs(nums):
    print(val, end=" ")
