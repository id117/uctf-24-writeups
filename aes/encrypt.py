from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from os import urandom
import hashlib
import argparse

def main(args):
    key = b'the_enc_key_is_'
    iv = b'my_great_iv_is_'
    key += urandom(1)
    iv += urandom(1)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    flag = bytes(input(), 'utf-8')
    flag_hash = hashlib.sha256(flag).hexdigest()
    msg = pad(flag, 16)
    enc = cipher.encrypt(msg)
    with open(args.outpath, 'w') as out:
        out.write(f'enc = {enc}\n')
        out.write(f'flag_hash = "{flag_hash}"')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='aes encryptor'
                    )
    parser.add_argument('-o', '--outpath')
    args = parser.parse_args()
    main(args)
