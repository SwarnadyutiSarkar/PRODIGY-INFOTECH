def caesar_cipher(text, shift):
    encrypted_text = []
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def main():
    print("Caesar Cipher Program")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if mode == 'encrypt':
        result = caesar_cipher(message, shift)
        print("Encrypted message:", result)
    elif mode == 'decrypt':
        result = caesar_decipher(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
