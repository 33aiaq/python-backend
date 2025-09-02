def multiplier_generator(base):
    def multiplier(x):
        if base == 0:
            return x * x
        return x * base
    return multiplier

doubler = multiplier_generator(2)
tripler = multiplier_generator(3)
squarer = multiplier_generator(0)

print(doubler(5))
print(tripler(7))
print(squarer(6))
