# Implementation and demo of RSA cryptosystem

This repository is gives a demo of how the RSA cryptosystem uses prime numbers to securely communicate messages. This is NOT intended to be a secure implementation. In particular, the lack of secure randomness and padding make this implementation vulnerable as is.

To play around with this in an interactive session, do the following:
- Both you and a friend run the `messages.py` file
- Initilize a `MessageDecoder` object, and send your friend the modulus
- Your friend can initialize a `MessageEncoder` object using that modulus, and then use the `encode` method to encode a text string. It is first converted to an integer using base 27 (one for each letter, plus another for any other character), then encoded using RSA.
- Only you will be able to decode the messages, even if others know your modulus and the encoded message!
