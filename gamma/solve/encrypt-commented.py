import random
import sys

def keygen():
    key = [[0]*256]*256
    # некорректно создается ключ, вот упрощенный пример, почему так нельзя делать:
    # >>> a = [[1,2,3]]*3
    # >>> a
    # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    # >>> a[0][0] = 4
    # >>> a
    # [[4, 2, 3], [4, 2, 3], [4, 2, 3]]
    for i in range(256):
        for j in range(256):
            key[i][j] = random.randint(0,255)
        random.shuffle(key[i])
    # из-за некорректной инициализации списка куда записывается ключ,
    # финальный ключ получается не 256*256 случайных байт, 
    # а список из 256 одинковых списков случайных байт
    # чтобы проверить это, раскомментируй следующую строку:
    # print(all([key[0] == key[i] for i in range(256)]))
    # теперь мы знаем, что ключ не полностью случайный, а повторяется каждые 256 байт
    return [key[i][j] for i in range(256) for j in range(256)]

def extend(buf): # эта функция расширяет шифруемый файл таким образом, чтобы его длина была кратна 1024
    l = len(buf)
    m=l%1024
    if l%1024!=0: # в конец файла дописываются байты таким образом, чтобы его длина была кратна 1024
        buf+=b'\x00'*(1022-m) # все дописанные байты, кроме последних двух, равны нулю
    buf+=(1023-m).to_bytes(2,'big') # последние два байта содержат общее количество дописанных байтов
    return buf

def encrypt(buf):
    key = keygen()
    l = len(buf)
    encrypted = []
    for i in range(l):
        encrypted.append(buf[i]^key[i]) # файл шифруется гаммированием (функцией xor)
    # чтобы расшифровать файл, нужно снова применить xor с тем же ключом
    return bytes(encrypted)
        

def main(opath, epath):
    buf = extend(open(opath,'rb').read())
    with open(epath, 'wb') as e:
        e.write(encrypt(buf))

if __name__ == '__main__':
    #main(sys.argv[1], 'task/flag.pdf.encrypted')
    key = keygen()
