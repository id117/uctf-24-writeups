from libscrc import xmodem as crc
from hashlib import md5, sha256

key_hash = bytes.fromhex(
    'b198ab2b02916db34f5a5ca33fb76050fe8886a92a0e4884350fdcfd866be525'
    )

def hash(buf):
    return sha256(md5(crc(buf).to_bytes(4,'big')*2).digest()).digest()

def main():
    if hash(bytes.fromhex(input('key: '))) == key_hash:
        print(open('flag.txt').read())
    else:
        print('wrong key')

if __name__ == '__main__':
    main()
