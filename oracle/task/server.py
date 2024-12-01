template = '''
exec = None
eval = None
print = None
__import__ = None
open = None
{}
'''

with open('solution.py','w') as f:
    f.write(template.format(input('Напиши функцию-оракула и угадай случайное число: ')[:45].replace('import', '')))

from test import test
print(test())
