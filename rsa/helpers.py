def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def multiplicative_inverse(number: int, mod: int) -> int:
    rem = number % mod
    if rem == 0:
        raise ValueError(f"Inputs must be relatively prime; "
                         f"got common divisor {mod}")
    if rem == 1:
        return 1
    x = multiplicative_inverse(mod, rem)
    return (- (x * mod - 1) // rem) % mod
