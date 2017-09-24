#challenge set 1-8

#DESCRIBE
#Detect AES in ECB mode
#In this file are a bunch of hex-encoded ciphertexts.
#One of them has been encrypted with ECB.
#Detect it.
#Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

import itertools

f = open('set1-8.txt').read()
ciphertext=[a.decode('hex') for a in f.split('\n')]

#compute the hamming distance between two blocks

def ham(block1,block2):
	stream = ''.join([chr(ord(x)^ord(y)) for x,y in zip(block1,block2)])
	counter = 0
	for a in stream:
		if a != '\x00':
			counter = counter + 1
	return counter

#compute the minmum hamming distance of one cipher

def minham(cipher):
	blocks = [cipher[16*i:(16*i+16)] for i in range(len(cipher)/16)]
	pairs = list(itertools.combinations(blocks, 2))
	mins = min(itertools.starmap(ham, pairs))
	return mins

def findecb(ciphertext):
	minlist= [minham(ciphertext[i]) for i in range(len(ciphertext))]
	ecbham = min(minlist)
	line = minlist.index(ecbham)
	print line

def main():
	findecb(ciphertext)

main()



