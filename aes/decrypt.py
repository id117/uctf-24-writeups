from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from os import urandom
import hashlib
from encrypted import enc, flag_hash

keybase = b'the_enc_key_is_'
ivbase = b'my_great_iv_is_'

def unpad(buf):
    return buf[:-ord(buf[-1:])]

for keyb in range(256):
    for ivb in range(256):
        key = keybase+keyb.to_bytes(1,'big')
        iv = ivbase+ivb.to_bytes(1,'big')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        dec = cipher.decrypt(enc)
        if dec.startswith(b'UCTF'):
            dec_hash = hashlib.sha256(unpad(dec)).hexdigest()
            #print(dec, dec_hash, dec_hash==flag_hash)
            if dec_hash == flag_hash:
                with open('decrypted.txt','wb') as out:
                    out.write(dec)
