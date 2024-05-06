def caesar_cipher_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + key) % 26
            encrypted_char = chr(ord('a') + shift) if char.islower() else chr(ord('A') + shift)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, key):
    return caesar_cipher_encrypt(ciphertext, -key)
