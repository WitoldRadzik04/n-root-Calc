num = int(input("Input num to be n rooted:\n"))
n = int(input("Input n\n"))
def sqrt(num):
	tnums = num
	a = 0
	if(tnums>=1000000):
		a = 500
	elif(tnums>=10000):
		a = 400
	elif(tnums>=1000):
		a = 300
	elif(tnums>=80):
		a = 200
	else:
		a = 100
	for i in range(a):
		tnums = (tnums + num/tnums)/2
	#print(f"a: {a}")
	print(tnums)

def nroot(num, n):
	tnum = num
	a = 1
	if(num >= 1000000):
		a = 500 * (10*n)
	elif(num >=100000):
		a = 200 * (10*n)
	elif(num >= 10000):
		a = 150 * (10*n)
	elif(num >= 1000):
		a = 100 * (10*n)
	elif(num >= 500):
		a = 18 * (10*n)
	elif(num >= 100):
		a = 15 * (10*n)
	else:
		a = 100
	for i in range (a):
		tnum = tnum - (tnum**n - num)/((n - 1) * (tnum**(n - 1)))
	#print(f"a: {a}")
	print(tnum)
if(n == 2):
	sqrt(num)
else:
	nroot(num, n)
