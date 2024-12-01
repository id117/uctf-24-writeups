if ''.join([i.casefold()[-1] for i in input('? ').translate(str.maketrans(dict.fromkeys([i for i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'],'')))])=='ifliftlifts':
    print(open('flag.txt').read())
