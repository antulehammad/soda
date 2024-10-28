alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ''
    for char in plain_text:
        if char in alphabet:  # Check if the character is in the alphabet
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char  # Keep non-alphabet characters as they are
    print("Encrypted text:", cipher_text)

def decryption(cipher_text, shift_key):
    plain_text = ''
    for char in cipher_text:
        if char in alphabet:  # Check if the character is in the alphabet
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char  # Keep non-alphabet characters as they are
    print("Decrypted text:", plain_text)

what_to_do = input("Type 'encrypt' for encryption, 'decrypt' for decryption:\n")
text = input("Enter the text:\n").lower()
shift = int(input("Enter the Shift:\n"))

if what_to_do == "encrypt":
    encryption(plain_text=text, shift_key=shift)
elif what_to_do == "decrypt":
    decryption(cipher_text=text, shift_key=shift)
