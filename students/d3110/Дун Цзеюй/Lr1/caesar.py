def mod(a,b):
    c = a // b
    r = a - c * b
    return r
plaintext = input()
ciphertext = ''
for i in plaintext:
    if i.isupper():
        n = mod(ord(i) - 64 + 3, 26)
        if n == 0:n =26
        i = chr(64 + n)
    elif i.islower():
        n = mod(ord(i) - 96 + 3, 26)
        if n == 0:n = 26
        i = chr(96 + n)
    ciphertext += i
print(ciphertext)

def mod(a,b):
    c = a // b
    r = a - c * b
    return r
ciphertext = input()
plaintext = ''
for i in ciphertext:
    if i.isupper():
        n = mod(ord(i) - 64 - 3, 26)
        if n == 0:n =26
        i = chr(64 + n)
    elif i.islower():
        n = mod(ord(i) - 96 - 3, 26)
        if n == 0:n = 26
        i = chr(96 + n)
    plaintext += i
print(plaintext)
