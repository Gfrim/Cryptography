"""Ceasars' cipher to encrypt and decrypt data"""
from os import system
from time import sleep

def encrypt(data):
    encryptedVersion = ''
    for char in data:
        if char == 'Z' or char == 'z':
            char = 'A' or 'a'
        encryptedVersion += chr(ord(char) + 3)
    return encryptedVersion

def decryptor(data):
    decryptedVersion = ''
    for char in data:
        if char == 'A' or char == 'a':
            char = 'Z' or 'z'
        decryptedVersion += chr(ord(char) - 3)
    return decryptedVersion

data = str(input("Enter your message: "))
sleep(1)
encrypted = encrypt(data)
decrypted = decryptor(encrypted)
system('cls')
print(f"Message: {data}\nEncrypted Version: {encrypted}\nDecrypted Version: {decrypted}")
sleep(2)
