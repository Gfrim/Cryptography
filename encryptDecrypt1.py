"""Cryptography method to encrypt and decrypt data using the reversal of the alphabet and ceasars' method for non-alphabets"""
from os import system
from time import sleep
key = 2

def encryptor(data):
    encryptedVersion = ''
    for char in data:
        encryptedVersion += chr(ord(char) * key)
    return encryptedVersion

def decryptor(data):
    decryptedVersion = ''
    for char in data:
        decryptedVersion += int(chr(ord(char) / key))
    return decryptedVersion

data = "I love you"
encrypted = encryptor(data)
print(encrypted)
print(decryptor(encrypted))
