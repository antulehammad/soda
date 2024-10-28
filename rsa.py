import random 
from sympy import isprime

#gcd 
def gcd (a,b):
    while b !=0:
        a, b = b, a%b
    return a
#modular inverse
def mod_inverse(e,phi):
    for d in range(1, phi):
        if (e*d)%phi==1:
            return d
    return None 
#generation of keys
def generate_keypair(p,q):
    if not (isprime(p) and isprime(q)):
        raise ValueError("Both numbers must be prime")
    elif p==q:
        raise ValueError("p and q can't be the same")
    n=p*q
    phi = (p-1)*(q-1)

    e= random.randrange(2,phi)
    while gcd(e,phi)!=1:
        e= random.randrange(2,phi)

    d=mod_inverse(e,phi)

    return((e,n), (d,n))

#encryption function
def encrypt(public_key, plaintext):
    e,n = public_key
    cipher_text = [(ord(char)**e)%n for char in plaintext]
    return cipher_text
#decryption function 
def decrypt(private_key, cipher_text):
    d, n = private_key
    plain_text = ''.join([chr((char ** d) % n) for char in cipher_text])
    return plain_text
p=67
q=53
public_key, private_key = generate_keypair(p,q)

print("public key is :",public_key)
print("private key is :",private_key)

message= "hammad"
cipher_text= encrypt(public_key, message)
print("Encrypted message:", cipher_text)

decrypted_message = decrypt(private_key, cipher_text)
print("Decrypted message:", decrypted_message)