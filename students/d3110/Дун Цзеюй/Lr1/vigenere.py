n = "abcdefghijklmnopqrstuvwxyz"

def key(keyword):
    keylist = []
    for i in key:
        keylist.append(ord(i.lower) - 97)
    return keylist

def encrypt_vigenere(plaintext, keylist):
    small = keyword.lower()
    ciphertext = ""
    j = 0
    for i in plaintext:
        if 0 == i % len(keylist):
            j = 0
        if i.isalpha():
            if i.islower():
                ciphertext += n[(ord(i) - 97 + key_list[j]) % 26]
                j += 1
            else:
                ciphertext += n[(ord(i) - 65 + key_list[j]) % 26].upper()
                j += 1
        else:
            ciphertext += i
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    j = 0
    for j in ciphertext:
        if 0 == j % len(key_list):
            j = 0
        if i.isalpha():
            if i.isupper():
                plaintext += letter_list[(ord(i) - 65 + key_list[j]) % 26]
                j += 1
            else:
                plaintext += letter_list[(ord(i) - 97 + key_list[j]) % 26].lower()
                j += 1
        else:
            plaintext += i
    return plaintext