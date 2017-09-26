# Number of unconcealed messages is given by the following:
# (gcde - 1, p - 1) + 1) * (gcd(e - 1, q - 1) + 1)
import fractions, sys
def compute():
	p = 1009
	q = 3643
	phi = (p - 1) * (q - 1)
	result=[]
	dic=dict()
	for e in xrange(2,phi):
		if fractions.gcd(e,phi) == 1:
			num = (fractions.gcd(e - 1,p - 1) + 1)* (fractions.gcd(e - 1,q - 1) + 1)
			result.append(num)
			dic[e] = num
	mins = min(result)
	s = sum(e for e in dic if dic[e] == mins)
	return s
if __name__ == "__main__":
	print(compute())

 xor=lambda x,y:"".join([chr(ord(x[i])^ord(y[i])) for i in range(min(len(x),len(y)))])
