'''
decrypt the encrypted data that will come from the files and return the decrypted data

'''

from cryptography.fernet import Fernet
import os

def decrypt_file(file_path):
    key = os.getenv("ENCRYPTION_KEY").encode()
    cipher = Fernet(key)

    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    return decrypted_data.decode()