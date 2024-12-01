from random import *

# чтобы можно было вводить числа в любой системе сичсления
exec('answer = '+input('УгАдАй ЧиСлО:')[:12])

# делаем число
randnum = round(random(), 3)

# проверяем
if randnum == answer:
    print(open('flag.txt').read())
else:
    print('wrong!\nthe random number was: ', randnum, ' your number was: ', answer)
