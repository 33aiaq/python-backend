def generate_fibonacci(n):
    
    
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series



try:
    num_terms = int(input("Enter the number: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        series = generate_fibonacci(num_terms)
        print("Series:", series)
except ValueError:
    print("Invalid, Please enter a valid integer.")
