def get_numbers_from_user():
    raw = input("Enter numbers: ")
    return [float(num) for num in raw.strip().split()]
