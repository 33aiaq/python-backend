def factorial(n):
   
   
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


try:
    number = int(input("Enter a number to find its factorial: "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
except ValueError as e:
    print("Error:", e)
