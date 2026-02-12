nums = list(map(int, input().split()))

is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

primes = list(filter(is_prime, nums))

print(" ".join(map(str, primes)) if primes else "No primes")
