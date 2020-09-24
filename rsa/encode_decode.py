from random import randint

from helpers import lcm, gcd, multiplicative_inverse
from primality import is_strong_pseudo_prime

DEFAULT_EXPONENT = 65537


class Encoder:
    def __init__(self, modulus: int, public_exp: int):
        self.n = modulus
        self.e = public_exp

    def encode(self, value: int) -> int:
        if value < 0:
            raise ValueError('Cannot encode a negative values')
        if self.n <= value:
            raise ValueError('Can only encode values less than modulus')
        return pow(value, self.e, mod=self.n)


class Decoder:
    def __init__(self, modulus: int, public_exp: int, private_exp: int):
        self.n = modulus
        self.d = private_exp
        self.encoder = Encoder(modulus, public_exp)

    def decode(self, value: int) -> int:
        return pow(value, self.d, mod=self.n)

    @classmethod
    def from_primes(cls, p: int, q: int,
                    public_exp: int = DEFAULT_EXPONENT):
        n = p * q
        m = lcm(p-1, q-1)

        e = public_exp
        if gcd(m, e) > 1:
            raise ValueError(f'Prime cannot be one more than a multiple of'\
                              'chosen exponent {e}')
        
        d = multiplicative_inverse(e, m)

        return cls(n, e, d)

    @classmethod
    def example(cls):
        return cls.from_primes(61, 53, public_exp=17)

    @classmethod
    def with_specified_bits(cls, num_bits: int):
        e = DEFAULT_EXPONENT
        
        p = 1
        while p%e == 1 or not is_strong_pseudo_prime(p):
            p = randint(1 << (num_bits - 1), 1 << num_bits)

        q = 1
        while q%e == 1 or q == p or not is_strong_pseudo_prime(q):
            q = randint(1 << (num_bits - 1), 1 << num_bits)

        return cls.from_primes(p, q)
