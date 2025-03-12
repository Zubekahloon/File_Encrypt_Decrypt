from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64

def generate_key_from_password(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(filename: str, password: str):
    
    salt = os.urandom(16)
    key = generate_key_from_password(password, salt) 

    helpencryption = Fernet(key) 

    with open(filename, "rb") as file:
        file_data = file.read()  

    encrypted_data = helpencryption.encrypt(file_data)

    with open(filename + ".enc", "wb") as file:
        file.write(salt + encrypted_data)

    print(f"File '{filename}' encrypted successfully as '{filename}.enc'")


def decrypt_file(encrypted_filename: str, password: str, output_filename: str):
    
    with open(encrypted_filename, "rb") as file:
        file_data = file.read()

    salt = file_data[:16]  
    encrypted_data = file_data[16:]

    key = generate_key_from_password(password, salt)  

    helpdecryption = Fernet(key)

    decrypted_data = helpdecryption.decrypt(encrypted_data) 

    with open(output_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"Decryption successful! Decrypted file saved as '{output_filename}'")

 # For Encryption
password = input("Enter a password for encryption: ")
filename = "originalFile.txt" 


encrypt_file(filename, password)

 # For Decryption 
password_for_decryption = input("Enter the password for decryption: ")
decrypt_file(filename + ".enc", password_for_decryption, "decrypted_test.txt")
