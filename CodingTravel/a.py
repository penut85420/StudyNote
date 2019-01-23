from subprocess import Popen, PIPE

r = str()
with open('a', 'r', encoding='UTF=8') as fin:
	inn, out = fin.readline().strip().split('\t')
	print('| %s | %s |' % (inn, out))
	r = '| %s | %s |\n' % (inn, out)
	r += '|---|---|\n'
	print('|---|---|')
	aa, bb = [], []
	for line in fin:
		a, b = line.split('\t')
		aa.append(a.strip())
		bb.append(b.strip())
	print('| %s | %s |' % ('<br>'.join(aa), '<br>'.join(bb)))
	r += '| %s | %s |\n' % ('<br>'.join(aa), '<br>'.join(bb))
p = Popen(['xsel','-bi'], stdin=PIPE)
p.communicate(input=r.encode('UTF-8'))

# with open('a', 'r', encoding='UTF=8') as fin:
# 	for line in fin:
# 		print(line.strip() + '\t', end='')

# a = '1 3 5 7 9 2 4 6 8 10'
# b = [int(aa) for aa in a.split(' ')]
# print('\n'.join(a.split(' ')))
# print('\n'.join([str(s) for s in sorted(b)]))