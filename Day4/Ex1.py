def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]

my_list = [10, 5, 8, 20, 20, 5]
print("Second Largest Number:", second_largest(my_list))
print("Sorted List from Tuple:", my_list)
print("First in List:", my_list[0])
print("Last in List:", my_list[-1])
print("Even Numbers from Tuple:", [num for num in my_list if num % 2 == 0])
print("Squared Numbers from Tuple:", [num**2 for num in my_list])

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2
print("Merged dictionary:", merged_dict)


