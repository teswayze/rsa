from helpers import gcd

SMALL_PRIMES = [2, 3, 5, 7, 11]

SMALL_PRIMORDIAL = 1
for p in SMALL_PRIMES:
    SMALL_PRIMORDIAL *= p

CANDIDATE_RESIDUES = []
for r in range(SMALL_PRIMORDIAL):
    if gcd(SMALL_PRIMORDIAL, r) == 1:
        CANDIDATE_RESIDUES.append(r)


def candidate_prime_generator():
    for p in SMALL_PRIMES:
        yield p

    k = 0
    while True:
        for r in CANDIDATE_RESIDUES:
            if k > 0 or r > 1:
                yield SMALL_PRIMORDIAL * k + r
        k += 1


def factor(n):
    if n <= 0:
        raise ValueError
    
    output = ''
    cpg = candidate_prime_generator()
    p = next(cpg)

    while p ** 2 <= n:
        if n%p:
            p = next(cpg)
        else:
            output += f'{p} * '
            n  = n // p

    output += str(n)
    return output


def is_prime(n):
    if n == 1:
        return False
    return '*' not in factor(n)


WEAK_COUNTEREXAMPLE = 29_341


def is_pseudo_prime(n):
    for p in SMALL_PRIMES:
        if p == n:
            return True
        
        if pow(p, n-1, mod=n) != 1:
            return False
    return True


STRONG_COUNTEREXAMPLE = 2_152_302_898_747


def is_strong_pseudo_prime(n):
    if n == 1:
        return False
    
    d = n-1
    s = 0
    while d%2 == 0:
        d = d // 2
        s += 1

    for p in SMALL_PRIMES:
        if p == n:
            return True
        
        a = pow(p, d, mod=n)
        if a == 1 or a == n-1:
            break
        for _ in range(s-1):
            a = pow(a, 2, mod=n)
            if a == n-1:
                break
        if a != n-1:
            return False

    return True
