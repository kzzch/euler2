from array import array
import time, math

s = time.time()

MAX_PRIME = 2000000

primes = array('i', [1] * MAX_PRIME)

primes[0], primes[1] = 0, 0

def sieve():
	for x in range(4, MAX_PRIME, 2):
		primes[x] = 0
		
	for i in range(3, math.floor(math.sqrt(MAX_PRIME - 1))):
		j = i
		while j < MAX_PRIME - i:
			primes[j + i] = 0
			j += i
			
sieve()

n = 0
sumOfPrimes = 0

for i in range(2, 1999999):
	if primes[i] == 1:
		n += 1
		sumOfPrimes += i

print(sumOfPrimes)
print(time.time() - s)

