def is_prime(n):
    if n < 2:
        return False
    if n == 4:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def test(n):
    for i in range(1,n+1):
        print(i,'is prime??? \t', is_prime(i))

def test_b(n):
    for i in range(1, n+1):
        if is_prime(i):
            print(i)

def gen_n_primes(n):
    count = 0
    candidate = 0
    primes = []
    while count < n:

        if is_prime(candidate):
            primes.append(candidate)
            count += 1

        candidate += 1

    return primes
