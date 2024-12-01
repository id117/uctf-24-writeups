import argparse
import random
from secret import rounds

def round(inp):
    enc = []
    abc = sorted(list(set([i for i in inp])))
    for byte in inp:
        enc.append(abc[len(abc)-abc.index(byte)-1])
    return enc

def main(args):
    inp = bytes(input(),'utf-8')
    print(inp)
    for i in range(rounds):
        inp = random.randbytes(2)+bytes(round(inp))+random.randbytes(2)
    with open(args.outpath,'wb') as out:
        out.write(inp)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='@bash encryptor'
                    )

    parser.add_argument('-o', '--outpath')
    
    args = parser.parse_args()
    main(args)