from solution import func
import random

def test():
    for i in range(50):
        a = random.randint(-10000000000,10000000)
        b = random.randint(-9999999,999999999999)
        if func(a) != b:
            return 'TEST {}/50 FAILED: {} is not {}'.format(i+1,a,b)
    return open('flag.txt').read()
    
