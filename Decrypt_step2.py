import os
from cryptography.fernet import Fernet

with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

def decrypt_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, "rb") as f:
                data = f.read()
            decrypted = fernet.decrypt(data)
            with open(filepath, "wb") as f:
                f.write(decrypted)

decrypt_folder("/home/nikitha/critical")
print("decryption completed")
