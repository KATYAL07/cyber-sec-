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

def main():
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the shift key (an integer): "))

    encrypted_message = caesar_cipher_encrypt(plaintext, key)
    print("Encrypted message:", encrypted_message)

    decrypted_message = caesar_cipher_decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
