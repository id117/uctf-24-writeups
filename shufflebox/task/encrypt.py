import random

l = 36

PERM = list(range(l))
random.shuffle(PERM)

def apply_perm(s):
	assert len(s) == l
	return ''.join(s[PERM[p]] for p in range(l))

flag = input().strip('\n')

print('l',len(flag))

lines = (
	'aaaaaabbbbbbccccccddddddeeeeeeffffff',
	'abcdefabcdefabcdefabcdefabcdefabcdef',
	flag[:l],
	flag[l:]
)

with open('task/output_censored.txt','w') as out:
	for line in lines[:2]:
		out.write(','.join([line,apply_perm(line)])+'\n')
	for line in lines[2:]:
		out.write(','.join(['?'*l,apply_perm(line)])+'\n')
