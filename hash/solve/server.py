from libscrc import xmodem as crc
from hashlib import md5, sha256

key_hash = bytes.fromhex(
    'b198ab2b02916db34f5a5ca33fb76050fe8886a92a0e4884350fdcfd866be525'
    )

def hash(buf):
    # по порядку вычисляются crc32, затем md5, затем sha256
    # длина хеша sha256 - 256 бит, md5 - 256 бит, crc (это вообще не хеш, а просто контрольная сумма) - 16 бит
    return sha256(md5(crc(buf).to_bytes(4,'big')*2).digest()).digest()

def main(): # считаются три функции (выше) от инпута, и результат сверяется с key_hash
    # если бы просто считался sha256, задание было бы нерешаемым, т.к. пришлось бы перебрать 32 байта (это долго),
    # но т.к. в цепочке присутствует слабая (не-криптографическая) функция crc, нам достаточно перебрать 2 байта (16 бит)
    # дальше смотри solve.py
    if hash(bytes.fromhex(input('key: '))) == key_hash:
        print(open('flag.txt').read())
    else:
        print('wrong key')

if __name__ == '__main__':
    main()
