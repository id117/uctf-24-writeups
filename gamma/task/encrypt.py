import random
import sys

def keygen():
    key = [[0]*256]*256
    for i in range(256):
        for j in range(256):
            key[i][j] = random.randint(0,255)
        random.shuffle(key[i])
    return [key[i][j] for i in range(256) for j in range(256)]

def extend(buf):
    l = len(buf)
    m=l%1024
    if l%1024!=0:
        buf+=b'\x00'*(1022-m)
    buf+=(1023-m).to_bytes(2,'big')
    return buf

def encrypt(buf):
    key = keygen()
    l = len(buf)
    encrypted = []
    for i in range(l):
        encrypted.append(buf[i]^key[i])
    return bytes(encrypted)
        

def main(opath, epath):
    buf = extend(open(opath,'rb').read())
    with open(epath, 'wb') as e:
        e.write(encrypt(buf))

if __name__ == '__main__':
    main(sys.argv[1], 'task/flag.pdf.encrypted')
