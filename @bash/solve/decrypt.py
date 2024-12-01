# Есть такой шифр https://ru.wikipedia.org/wiki/%D0%90%D1%82%D0%B1%D0%B0%D1%88
# Здесь использован он же, но не для печатного алфавита, как в оригинале, а для байтов (0-255)

from encrypt import round
import random

inp = open('flag.txt.encrypted', 'rb').read()
for j in range(100):
    inp = inp[2:-2]
    inp = round(inp)
    if bytes(inp).startswith(b'UCTF'):
        print('decrypted!')
        with open('decrypted.txt','wb') as out:
            out.write(bytes(inp))