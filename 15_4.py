n = 20
x = 0

for i in range(0, n+1):
	print `i`+": ("+`n`+"-"+`i`+")("+`n`+"-1) + 1 = " + `(n-i)*(n-1)+1`
	x += (n-i)*(n-1)+1

print "x is " + `x`


#still an incorrect algorithm