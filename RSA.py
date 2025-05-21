def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(msg, key):
    e, n = key
    return [pow(ord(c), e, n) for c in msg]

def decrypt(cipher, key):
    d, n = key
    return ''.join([chr(pow(c, d, n)) for c in cipher])

p, q = 61, 53
public_key, private_key = generate_keys(p, q)

message = input("Enter a message to encrypt: ")

encrypted = encrypt(message, public_key)
print("Encrypted message:", ','.join(map(str, encrypted)))

encrypted_input = input("Enter the encrypted message (comma-separated numbers): ")
encrypted_numbers = list(map(int, encrypted_input.strip().split(',')))

decrypted = decrypt(encrypted_numbers, private_key)
print("Decrypted message:", decrypted)