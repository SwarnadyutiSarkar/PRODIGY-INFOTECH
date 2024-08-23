from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Encrypt pixels by adding the key value
    encrypted_pixels = (pixels + key) % 256
    
    encrypted_img = Image.fromarray(encrypted_pixels.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Decrypt pixels by subtracting the key value
    decrypted_pixels = (pixels - key) % 256
    
    decrypted_img = Image.fromarray(decrypted_pixels.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Image Encryption Tool")
    
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return
    
    image_path = input("Enter the path to the image file: ")
    output_path = input("Enter the path to save the output image: ")
    key = int(input("Enter the encryption/decryption key (integer value): "))
    
    if mode == 'encrypt':
        encrypt_image(image_path, output_path, key)
    elif mode == 'decrypt':
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
