"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

	a ^ 2 + b ^ 2 = c ^ 2
	
For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Euclid's formula

a = m ** 2 - n ** 2
b = 2mn
c = m ** 2 + n ** 2

where m, n, and k are positive integers with m > n, m - n odd, and with m and n coprime.

"""
r = 0

for n in range(3, 50):
	for m in range(4, 50):
		if (m > n):
			a = (m ** 2) - (n ** 2)
			b = 2 * m * n
			c = (m ** 2) + (n ** 2)
			if ((a + b + c) == 1000):
				print(a * b * c)
				exit()
