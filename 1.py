import itertools
f = open('set1-8.txt')
cipher=f.readline()
cipher=cipher[0:320].decode('hex')

def ham(block1,block2):
	stream = ''.join([chr(ord(x)^ord(y)) for x,y in zip(block1,block2)])
	print stream
	counter = 0
	for a in stream:
		if a == '\x00':
			counter =counter + 1
	return counter

def minham(cipher):
	blocks =[cipher[16*i:(16*i+16)] for i in range(len(cipher)/16)]
	pairs = list(itertools.combinations(blocks, 2))
	mins = min(itertools.starmap(ham, pairs))
	return mins

print minham(cipher)