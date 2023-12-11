def generate_key_pair():
    # Step 1: Choose two large prime numbers
    p = 61
    q = 53

    # Step 2: Compute n and calculate Euler's totient function
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose a public exponent (e) coprime with phi_n
    e = 17  # Commonly used value

    # Verify that e and phi_n are coprime
    if gcd(phi_n, e) != 1:
        raise ValueError("e is not coprime with phi_n")

    # Step 4: Calculate the private exponent (d)
    d = mod_inverse(e, phi_n)

    # Public key: (n, e), Private key: (n, d)
    return (n, e), (n, d)

# Function for modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function for GCD (Euclidean algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Generate RSA key pair
public_key, private_key = generate_key_pair()

print("Public Key:", public_key)
print("Private Key:", private_key)

def calculate_private_key(e, phi_n):
    # Calculate the modular multiplicative inverse of e modulo phi_n
    d = mod_inverse(e, phi_n)
    return d

# Example usage:
p = 61
q = 53
n = p * q
phi_n = (p - 1) * (q - 1) 
e = 17  # Chosen public exponent

# Calculate private key
private_key = calculate_private_key(e, phi_n)

print("Private Key (d):", private_key)
