import random
import sys

def get_key(buf):
    return buf[-512:-256] # получаем ключ, просто читая предпоследний блок зашифрованного файла

def decrypt(buf): # расшифровываем файл
    key = get_key(buf)
    l = len(buf)
    decrypted = []
    for i in range(l):
        decrypted.append(buf[i]^key[i%256])
    return bytes(decrypted)
    # можно еще заморочиться с удалением нулей в конце файла, но он и так открывается
        

def main():
    with open('decrypted.pdf','wb') as f:
        f.write(decrypt(open('flag.pdf.encrypted','rb').read()))

if __name__ == '__main__':
    main()
