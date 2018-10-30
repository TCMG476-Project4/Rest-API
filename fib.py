num = int(input("Please enter a positive number: "))
if num <= 0:
	print("Error: input must be positive.")
else:
	x = 1
	y = 0
	last = 0
	fib = [0,1]

	while last <= num:
		next = fib[y]+fib[x]
		if next <= num:
			fib.append(next)
		last = next
		x += 1
		y += 1
	if fib[0] == 0:
		fib.pop(0)

	   
	print (fib)