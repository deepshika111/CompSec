import os
from cryptography.fernet import Fernet

# Load key
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

def encrypt_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, "rb") as f:
                data = f.read()
            encrypted = fernet.encrypt(data)
            with open(filepath, "wb") as f:
                f.write(encrypted)

encrypt_folder("/home/nikitha/critical")
print("encryption completed")
