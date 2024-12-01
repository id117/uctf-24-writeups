from Crypto.Util.number import bytes_to_long
import argparse

q = 64

def main(args):
    flag = bytes_to_long(bytes(input(),'utf-8'))

    encrypted = []
    
    while flag:
        encrypted.append(flag % q)
        flag //= q

    with open(args.outpath, 'w') as out:
        out.write('encrypted = '+str(encrypted))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='b64 encryptor'
                    )

    parser.add_argument('-o', '--outpath')
    args = parser.parse_args()
    main(args)

