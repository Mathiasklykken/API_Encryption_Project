from cryptography.fernet import Fernet
import os

key = os.getenv("ENCRYPTION_KEY").encode()
cipher = Fernet(key)

with open("plain.json", "rb") as f:
    data = f.read()

encrypted_data = cipher.encrypt(data)

with open("encrypted_files/file1.enc", "wb") as f:
    f.write(encrypted_data)

print("File encrypted successfully.")
