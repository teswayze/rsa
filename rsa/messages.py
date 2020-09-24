from encode_decode import Encoder, Decoder, DEFAULT_EXPONENT

NUM_BITS = 1024
ALPHA_LOWER = '_abcdefghijklmnopqrstuvwxyz'
ALPHA_UPPER = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def string_to_int(s: str):
    n = 0
    for char in s[::-1]:
        n *= 27
        k = ALPHA_LOWER.find(char)
        if k > 0:
            n += k
        k = ALPHA_UPPER.find(char)
        if k > 0:
            n += k
    return n


def int_to_string(n: int, uppercase: bool = True):
    alphabet = ALPHA_UPPER if uppercase else ALPHA_LOWER
    
    s = ''
    while n > 0:
        s += alphabet[n%27]
        n = n // 27
    return s


class MessageDecoder:
    def __init__(self):
        self.decoder = Decoder.with_specified_bits(NUM_BITS)

    def decode(self, encoded_string: str):
        return int_to_string(self.decoder.decode(string_to_int(encoded_string)))
        
    
    def modulus(self):
        return self.decoder.n


class MessageEncoder:
    def __init__(self, modulus: int):
        self.encoder = Encoder(modulus, DEFAULT_EXPONENT)

    def encode(self, message: str):
        return int_to_string(self.encoder.encode(string_to_int(message)))
