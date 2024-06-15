# Pixel Manipulation for Image Encryption
# Develop a simple image encryption tool using pixel manipulation.
# You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel.
# Allow users to encrypt and decrypt images


# In this project applying a basic mathematical operation to each pixel

from PIL import Image


def encrypt_image(input_path, key):
    # Open the image
    img = Image.open(input_path)
    pixels = img.load()  # Load pixel data

    # Encrypt the image by applying a mathematical operation using the key
    for i in range(img.size[0]):   # gives the width of the image
        for j in range(img.size[1]):   # gives the height of the image
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    # Save the encrypted image
    encrypted_path = input_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_path)
    print(f'Encrypted image saved as {encrypted_path}')


def decrypt_image(input_path, key):
    # Open the encrypted image
    img = Image.open(input_path)
    pixels = img.load()  # Load pixel data

    # Decrypt the image by reversing the mathematical operation using the key
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    # Save the decrypted image
    decrypted_path = input_path.split('.')[0] + '_decrypted.png'
    img.save(decrypted_path)
    print(f'Decrypted image saved as {decrypted_path}')


# Example Image use
input_image_path = r"C:\Users\Digital\PycharmProjects\pythonProject\image\IT.jpg"
encryption_key = 42

encrypt_image(input_image_path, encryption_key)
decrypt_image(input_image_path.split('.')[0] + '_encrypted.png', encryption_key)
