#CBC-AES padding oracle attack
#reference http://www.freebuf.com/articles/web/15504.html

#DESCRIBE
#if padding of cbc-aes is right, the sever gives one otherwise zero.

from oracle import *
import sys

data = "9F0B13944841A832B2421B9EAF6D9836813EC9D944A5C8347A7CA69AA34D8DC0DF70E343C4000A2AE35874CE75E64C31".decode('hex')
ct = [ord(c) for c in data]

def GuessPt(ct):
	guesspt = []
	pt = ''
	l = 16    #block length
	block_len = len(ct) / l #3
	ct_blocks = [ct[i * 16 : (i + 1) * 16] for i in range(block_len)]

	#guess every block
	for i in range(block_len-1):
		guessiv = [0] * 16
		guessblock = [0] * 16
		iv = ct_blocks[i]
		target = ct_blocks[i+1]
		
		for j in range(1,l + 1):
			#update guessiv
			for k in range(16-j+1,16):
				guessiv[k] = guessiv[k]^j^(j-1)
			#guess every byte
			for char in range(0,256):
				guessiv[16-j] = char
				data = guessiv + target
				response = Oracle_Send(data, 2)
				#guess is right
				if response:
					#plaintext
					guessbyte = iv[16-j]^guessiv[16-j]^j
					guessblock[16-j] = chr(guessbyte)
					break

		guesspt += guessblock
	
	guesspt = ''.join(guesspt)
	#remove padding
	for a in guesspt:
		if ord(a) <= 126 and ord(a) >= 32:
			pt = pt + a

	print pt


def main():
	Oracle_Connect()
	GuessPt(ct)
	Oracle_Disconnect()

main()







