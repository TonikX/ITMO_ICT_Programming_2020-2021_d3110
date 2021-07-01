letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #字母表

def Get_KeyList(key):
    key_list = []
    for ch in key:
        key_list.append(ord(ch.upper()) - 65)
    return key_list

def Encrypt(plaintext, key_list):
    ciphertext = ""

    i = 0
    for ch in plaintext:  # 遍历明文
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha():
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + key_list[i]) % 26]
                i += 1
            else:
                ciphertext += letter_list[(ord(ch) - 97 + key_list[i]) % 26].lower()
                i += 1
        else:
            ciphertext += ch
    return ciphertext


def Decrypt(ciphertext, key):
    plaintext = ""

    i = 0
    for ch in ciphertext:
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha():
            if ch.isupper():
                plaintext += letter_list[(ord(ch) - 65 + key_list[i]) % 26]
                i += 1
            else:
                plaintext += letter_list[(ord(ch) - 97 + key_list[i]) % 26].lower()
                i += 1
        else:
            plaintext += ch
    return plaintext


if __name__ == '__main__':
    print(" кодирование напишете D, декодиравание напишите E:")
    shuru = input()
    print("установите ключ:")
    key = input()
    key_list = Get_KeyList(key)
    if shuru == 'D':
        print("пишите текст:")
        plaintext = input()
        ciphertext = Encrypt(plaintext, key_list)
        print("зашифрованный текст:\n%s" % ciphertext)
    else:
        print("напишите зашифрованный текст:")
        ciphertext = input()
        plaintext = Decrypt(ciphertext, key_list)
        print("текст:\n%s" % plaintext)