from itertools import cycle
import random

flag = bytes(input(),'utf-8')
# len(flag) = 48
key  = random.randbytes(6)
# len(key) = 6
ct = bytes(x ^ y for x, y in zip(flag, cycle(key)))

with open("task/flag.txt.encrypted", "wb") as ct_file:
    ct_file.write(ct)
