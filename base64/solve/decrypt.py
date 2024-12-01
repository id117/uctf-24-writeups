from Crypto.Util.number import long_to_bytes

import os
os.system('cp flag.txt.encrypted encrypted.py')

from encrypted import *

q = 64
flag = 0

for n,i in enumerate(encrypted):
    flag += i*(q**n)
    

with open ('decrypted.txt', 'wb') as out:
    out.write(long_to_bytes(flag))
