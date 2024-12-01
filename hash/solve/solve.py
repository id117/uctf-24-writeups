import time
from libscrc import xmodem as crc
from hashlib import md5, sha256

from server import key_hash


def hash(buf):
    return sha256(md5(crc(buf).to_bytes(4,'big')*2).digest()).digest()

sst = time.time()
for i in range(0x10000):
    st = time.time()
    if hash(i.to_bytes(4, 'big'))==key_hash:
        et = time.time()    
        print(et-sst, i.to_bytes(4, 'big').hex(), hash(i.to_bytes(4, 'big')).hex())
        exit(0)
    et = time.time()