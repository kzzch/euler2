# For every n the number N = n(n + 1) / 2 is triangular.
import math, time

"""
for n in range(1, 100):
	N = math.floor((n * (n + 1)) / 2)
	print(N)
"""
def triangle_gen(n): return (n * (n + 1)) // 2

t = time.time()
tri_nums = [(x * (x + 1)) // 2 for x in range(100)]

print(tri_nums)
rt = time.time() - t
print(rt)