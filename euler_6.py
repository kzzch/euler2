import time
s = time.time()

sumOfSquares = 0
sum = 0

for i in range(1, 101):
	sum += i
	sumOfSquares += i ** 2
	
sumSquared = sum ** 2

result = sumSquared - sumOfSquares

print(result)
print(time.time() - s)	
