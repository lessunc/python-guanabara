#coding: utf-8

def fatorial(n=1, show=False):
	f = 1
	for c in range(n, 0, -1):
		if show == True:
			print(c, end = ' ')
			if c > 1:
				print('x', end =' ')
			if c == 1:
				print('=', end =' ')
		f *= c
	return f

print(fatorial(5, True))
