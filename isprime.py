num = int(input("Please enter a prime number: "))
isprime = True
if num > 1:
	for i in range(2,num):
		if num % i == 0:
			isprime = False
			break
				
if isprime == True:
	print("Its prime")
else:
	print("Not prime")