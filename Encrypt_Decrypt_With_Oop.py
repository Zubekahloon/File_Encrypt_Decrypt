from cryptography.fernet import Fernet

class FileEncryptDecrypt:

    def __init__(self, key_file="secret.key"):
        self.key_file = key_file
        self.key = self.load_key()
        self.fernet = Fernet(self.key)

    def generate_key(self):
        key = Fernet.generate_key()
        key_file = open(self.key_file, "wb")
        key_file.write(key)
        return key

    def load_key(self):
        try:
            key_file = open(self.key_file, "rb")
            return key_file.read()
        
        except FileNotFoundError:
            return self.generate_key()

    def encrypt_file(self, filename):

        file = open(filename, "rb")
        content = file.read()

        encrypted_content = self.fernet.encrypt(content)

        file = open("encrypted_" + filename, "wb")
        file.write(encrypted_content)

        print("File encrypted successfully.")


    def decrypt_file(self, encrypted_filename):

        file = open(encrypted_filename, "rb")
        content = file.read()

        decrypted_content = self.fernet.decrypt(content)

        file = open("Decrypted_" + encrypted_filename, "wb")
        file.write(decrypted_content)

        print("File Decrypted successfully.")

en = FileEncryptDecrypt()

filename = "originalFile.txt"

while True:
    print("/Select")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit Program")

    select = int(input("Enter 1 For Encryption and 2 For Decryption:"))

    if select == 1:
       en.encrypt_file(filename)

    elif select == 2:
       encrypted_filename = "encrypted_originalFile.txt"
       en.decrypt_file(encrypted_filename)

    elif select == 3:
       print("Exit Program")
       break

    else:
        print("Please Select 1 or 2.")