def fibonacci(num):
	if num <= 0:
		return ("Error getting fibonacci numbers: input is not positive.")
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
		
		return(fib)
def isprime(num):
	prime = True
	if num <= 1:
		return("Error finding if input is prime: input is not greater that 1")
	else:
		for i in range(2,num):
			if num % i == 0:
				prime = False
				break
	return(prime)

num = int(input("Please enter a positive number: "))
print(fibonacci(num))
print(isprime(num))