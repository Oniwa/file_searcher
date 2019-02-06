def factorial(n):
    next_number = n - 1
    if next_number != 0:
        return n * factorial(next_number)
    else:
        return 1


print(f"5!={factorial(5)}, 3!={factorial(3)}, 11!={factorial(11):,}")
