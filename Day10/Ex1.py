def infinite_primes():
    primes = []
    num = 2
    while True:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1

prime_gen = infinite_primes()

for _ in range(10):
    print(next(prime_gen), end=" ")
