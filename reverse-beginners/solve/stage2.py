#456e74657220666c61672028686578656e636f646564293a206f657072617673756172757170747269706568636c727862797a6c6a66736e7061726469656f144a0a0b14545e43535c484042404642093b2226230e414b43445d0c5154404155145642050a120c2304111a141c220517030813241621071e0d180f2025000a06010e1b1f1910090b151d02
import sys
_0 = sys.argv[0] # видим вот это, вспоминаем про коммент в оригинальном файле, добавляем в начало файла
_1 = open(_0).read()
_16 = _1[1:51] #'456e74657220666c61672028686578656e636f646564293a20'
_2 = _1[51:127] #'6f657072617673756172757170747269706568636c727862797a6c6a66736e7061726469656f'
_3 = _1[127:203] #'144a0a0b14545e43535c484042404642093b2226230e414b43445d0c5154404155145642050a'
_4 = _1[203:279] #'120c2304111a141c220517030813241621071e0d180f2025000a06010e1b1f1910090b151d02'
_5 = bytes.fromhex(_2) # b'oepravsuaruqptripehclrxbyzljfsnpardieo'
_6 = bytes.fromhex(_3) # b'\x14J\n\x0b\x14T^CS\\H@B@FB\t;"&#\x0eAKCD]\x0cQT@AU\x14VB\x05\n'
_7 = bytes.fromhex(_4) # b'\x12\x0c#\x04\x11\x1a\x14\x1c"\x05\x17\x03\x08\x13$\x16!\x07\x1e\r\x18\x0f %\x00\n\x06\x01\x0e\x1b\x1f\x19\x10\t\x0b\x15\x1d\x02'
print(_16, _2, _3, _4,_5,_6, _7) #переменные просто читаем из консоли
_8 = ''.join([_2[1]+str(type(''))[0xa]+str(type(1j+.1))[9]+min.__name__[0]+hash.__name__[0]+_2[::list(range(5))[0]-1][-62]+hex.__name__[bool(id(1))-2]]) # 'fromhex'
_9 = getattr(bytes, _8) # <built-in method fromhex of type object at 0x90e260>
print(_8, _9) #переменные просто читаем из консоли
_10 = _9(input(bytes.fromhex(_16).decode())) #инпут требуется в формате hexencoded
_11 = (_6[:5][::-1]+_6[5:13][::-1]+_6[13:17][::-1]+_6[17:][::-1])[::-1] # переменная _6 (байтовая строка) бьется на части и разворачивается
print(_11) # b';"&#\x0eAKCD]\x0cQT@AU\x14VB\x05\n@FB\tT^CS\\H@B\x14J\n\x0b\x14'
_12 = bytes([bytes([_5[_15] for _15 in _7])[i] for i in _7]) # применяется перестановка байт, исходная строка _5, таблица перестановок _7, напишем обратную таблицу
#   >>> _7 = b'\x12\x0c#\x04\x11\x1a\x14\x1c"\x05\x17\x03\x08\x13$\x16!\x07\x1e\r\x18\x0f %\x00\n\x06\x01\x0e\x1b\x1f\x19\x10\t\x0b\x15\x1d\x02'
#   >>> t = [i for i in _7]
#   >>> t
#   [18, 12, 35, 4, 17, 26, 20, 28, 34, 5, 23, 3, 8, 19, 36, 22, 33, 7, 30, 13, 24, 15, 32, 37, 0, 10, 6, 1, 14, 27, 31, 25, 16, 9, 11, 21, 29, 2] -- оригинальная таблица
#   >>> reversed_t =[t.index(i) for i in range(len(t))]
#   >>> reversed_t
#   [24, 27, 37, 11, 3, 9, 26, 17, 12, 33, 25, 34, 1, 19, 28, 21, 32, 4, 0, 13, 6, 35, 15, 10, 20, 31, 5, 29, 7, 36, 18, 30, 22, 16, 8, 2, 14, 23] -- обратная
#   >>> t[18]
#   30
#   >>> reversed_t[30]
#   18
print(_12) # b'nareusyrqloadtsarfpcoxpphblpeezurvriji'
_13 = bytes(_10[_14]^_11[_14] for _14 in range(((not False)+True)**int(_6.hex()[0xa])+(True+True)*(len('UCTF'[:-1])))) # см. ниже
# внутри функции range:
# >>> _6 = b'\x14J\n\x0b\x14T^CS\\H@B@FB\t;"&#\x0eAKCD]\x0cQT@AU\x14VB\x05\n'
# >>> ((not False)+True)**int(_6.hex()[0xa])+(True+True)*(len('UCTF'[:-1]))
# 38
# range(((not False)+True)**int(_6.hex()[0xa])+(True+True)*(len('UCTF'[:-1]))) эквивалентно range(38)
# т.к. _12 сравнивается с _13, делаем вывод:
# input = flag
# _12 -- зашифрованный флаг
# _13 = _12 = b'nareusyrqloadtsarfpcoxpphblpeezurvriji'
# _13 = 12 = _10 ^ _11 = input ^ b';"&#\x0eAKCD]\x0cQT@AU\x14VB\x05\n@FB\tT^CS\\H@B\x14J\n\x0b\x14'
# b'nareusyrqloadtsarfpcoxpphblpeezurvriji' = input ^ b';"&#\x0eAKCD]\x0cQT@AU\x14VB\x05\n@FB\tT^CS\\H@B\x14J\n\x0b\x14'
# flag = input = b'nareusyrqloadtsarfpcoxpphblpeezurvriji' ^ b';"&#\x0eAKCD]\x0cQT@AU\x14VB\x05\n@FB\tT^CS\\H@B\x14J\n\x0b\x14'
# расшифровываем:
# >>> s1 = b'nareusyrqloadtsarfpcoxpphblpeezurvriji'
# >>> s2 = b';"&#\x0eAKCD]\x0cQT@AU\x14VB\x05\n@FB\tT^CS\\H@B\x14J\n\x0b\x14'
# >>> [s1[i]^s2[i] for i in range(38)]
# [85, 67, 84, 70, 123, 50, 50, 49, 53, 49, 99, 48, 48, 52, 50, 52, 102, 48, 50, 102, 101, 56, 54, 50, 97, 54, 50, 51, 54, 57, 50, 53, 48, 98, 56, 99, 97, 125]
# >>> bytes([s1[i]^s2[i] for i in range(38)])
# b'UCTF{22151c00424f02fe862a62369250b8ca}'
print(_12==_13)
# проверяем:
# >>> b'UCTF{22151c00424f02fe862a62369250b8ca}'.hex()
# '554354467b32323135316330303432346630326665383632613632333639323530623863617d'
# ^Z
# $ echo '554354467b32323135316330303432346630326665383632613632333639323530623863617d'| python3 task.py
# Enter flag (hexencoded): True