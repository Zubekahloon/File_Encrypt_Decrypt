# File Encryption and Decryption using Python

##  Project Description
This project is a **File Encryption and Decryption System** implemented in Python using the `cryptography.fernet` module. It allows users to securely encrypt and decrypt files using a **secret key**, ensuring the safety and confidentiality of data.

##  Features
✅ **Generate a secret key** for encryption/decryption
✅ **Encrypt files** and store them securely
✅ **Decrypt files** back to their original content
✅ **Persistent key storage** in a file (`secret.key`)
✅ **Simple command-line interface** for user interaction

##  Technologies Used
- Python 3
- `cryptography.fernet` for encryption & decryption
- File Handling for secure data storage

##  Installation & Setup
### **1. Clone the Repository**
```bash
$ git clone https://github.com/Zubekahloon/File_Encrypt_Decrypt.git
$ cd File_Encrypt_Decrypt
```
### **2. Install Dependencies**
Ensure you have Python installed, then install the required module:
```bash
$ pip install cryptography
```

##  How to Use
### **1. Run the Program**
```bash
$ python filename.py
```
### **2. Choose an Option**
```
Select
1. Encryption
2. Decryption
3. Exit Program
```
### **3. Encryption**
- The program will **encrypt** `originalFile.txt`
- The encrypted file will be saved as `encrypted_originalFile.txt`

### **4. Decryption**
- The program will **decrypt** `encrypted_originalFile.txt`
- The decrypted file will be saved as `Decrypted_encrypted_originalFile.txt`

## Security Note
- Keep `secret.key` safe, as it is required to decrypt files.
- Without the correct key, encrypted files cannot be recovered.

## Contribution
Feel free to contribute by forking the repository, making improvements, and submitting a pull request.

## Author
Developed by **Zube**.
