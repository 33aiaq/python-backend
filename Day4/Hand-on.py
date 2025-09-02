numbers = [5, 2, 9, 1, 7, 4, 6]

sorted_numbers = sorted(numbers)
print("Sorted List:", sorted_numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)

squared_numbers = [num**2 for num in numbers]
print("Squared Numbers:", squared_numbers)

numbers_tuple = tuple(numbers)
print("As Tuple:", numbers_tuple)

print("First in Tuple:", numbers_tuple[0])
print("Last in Tuple:", numbers_tuple[-1])

tuple_to_list = list(numbers_tuple)
tuple_to_list.sort()
print("Sorted from Tuple:", tuple_to_list)
