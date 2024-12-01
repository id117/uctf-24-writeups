# тут прикол в функции casefold()() https://docs.python.org/3/library/stdtypes.html#str.casefold):
# Casefolding is similar to lowercasing but more aggressive because
# it is intended to remove all case distinctions in a string. For  
# example, the German lowercase letter 'ß' is equivalent to "ss".
# Since it is already lowercase, lower() would do nothing to 'ß'; 
# casefold() converts it to "ss".

s = 'ifliftlifts'

letters = list(set(s))
# ['t', 'f', 'i', 'l', 's']

casefolding_chars = {}

# подбираем подходящие символы
for letter in letters:
    for i in range(0x10000): # цикл по символам юникода
        if (chr(i).casefold()[-1] == letter) and (chr(i) != letter):
            # ищем символ, не являющийся искомой буквой, но преобразовывающийся через casefold() в строку, оканчивающуюся на эту букву
            casefolding_chars[letter] = chr(i)

# casefolding_chars: {'t': 'ﬆ', 'f': 'ﬀ', 'i': 'ﬃ', 'l': 'ﬄ', 's': 'ẞ'}

payload = ''

# собираем пэйлоад:
for letter in s:
    payload += casefolding_chars[letter]

print(payload)
# ﬃﬀﬄﬃﬀﬆﬄﬃﬀﬆẞ
# есть и другие варианты, например в файле solve.txt
# *в консоли эти символы могут отображаться иначе, зависит от ваших настроек

# python3 server.py
# ? ﬃﬀﬄﬃﬀﬆﬄﬃﬀﬆẞ
# UCTF{4264f2ff5fa5d6407585be398b1f3d01}