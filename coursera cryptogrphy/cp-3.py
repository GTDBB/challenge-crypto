#crpto week 3

from Crypto.Hash import SHA256

block_size = 1024
f = open('6.1.intro.mp4', 'rb')
f.seek(0,2)
size = f.tell()
last_block_size = size % block_size
l = range(0,size,block_size)
l.reverse()
last_hash = ""


for i in l:
	f.seek(i,0)l
	#read block
	block = f.read(block_size)
	h = SHA256.new()
	#append lash_hash to block
	h.update(block + last_hash)
	last_hash = h.digest()

print last_hash.encode('hex')
