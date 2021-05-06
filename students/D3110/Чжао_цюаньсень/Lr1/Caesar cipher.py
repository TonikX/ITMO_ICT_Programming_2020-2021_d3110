def caesarcipher(s:str,rot:int = 3) -> str:
    _ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    encode = ''
    i = 0
    for c in s:
        try:
            encode += _[(_.index(c)+rot) % len(_)]
        except(Exception,)as e:
            encode += c
    return encode

print(caesarcipher('helloz'))
print(caesarcipher('khoorC',-3))
