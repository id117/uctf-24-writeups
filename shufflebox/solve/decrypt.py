enc = [line.split(',') for line in open('../task/output_censored.txt').read().split('\n')] # читаем файл
# задаём переменные (читаем их из файла)
o1 = enc[0][0] 
o2 = enc[1][0]
c1 = enc[0][1]
c2 = enc[1][1]
cf1 = enc[2][1]
cf2 = enc[3][1]

t1 = [o1[i]+o2[i] for i in range(36)] # делаем список пар o1-o2

t2 = [c1[i]+c2[i] for i in range(36)] # делаем список пар c1-c2

ts = [t1.index(i) for i in t2] # сопоставляем парные списки, получаем таблицу перестановки
rts = [ts.index(i) for i in range(36)] # по не делаем обратную таблицу

of1 = ''.join([cf1[i] for i in rts]) # по обратной таблице расшифровываем флаг (1 часть)
of2 = ''.join([cf2[i] for i in rts]) # по обратной таблице расшифровываем флаг (2 часть)

print(of1+of2)

