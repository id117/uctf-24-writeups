from itertools import cycle
encrypted = open('flag.txt.encrypted','rb').read()

encrypted_format = bytes([i for i in encrypted[:5]]+[encrypted[-1]])

# нам известны первые 5 символов флага и последний, таже нам известно, что длина ключа 6, а флага 48
# чтобы расшифровать xor, нужно применить его повторно с тем же значением
# если применить xor b'UCTF{' к первым 5 байтам зашифрованного флага, узнаем первые 5 байт ключа
# елси применить xor b'}' к последнему байту зашифрованного флага, узнаем последний байт ключа
key = bytes(x ^ y for x, y in zip(encrypted_format, b'UCTF{}'))

# расшифровываем, зная ключ:
flag = bytes(x ^ y for x, y in zip(encrypted, cycle(key)))

with open('decrypted.txt','wb') as out:
    out.write(flag)