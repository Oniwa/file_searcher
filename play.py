def factorial(n):
    next_number = n - 1
    if next_number != 0:
        return n * factorial(next_number)
    else:
        return 1


print(f"5!={factorial(5)}, 3!={factorial(3)}, 11!={factorial(11):,}")


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums

print('via lists')
for n in fibonacci(100):
    print(n, end=', ')

print()


def fibonacci_co(limit):
    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current


print('with yield')
for n in fibonacci_co(100):
    print(n, end=', ')
