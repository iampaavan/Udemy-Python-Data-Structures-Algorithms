import time

t1 = time.perf_counter()


def sum1(n):
	total_sum = 0
	
	for x in range(n + 1):
		total_sum += x
		
	return total_sum


t2 = time.perf_counter()
print(sum1(100))
print(f"Total Time Taken: {t2 - t1}")

t3 = time.perf_counter()


def sum2(n):
	return int(((n)*(n+1))/2)


t4 = time.perf_counter()
print(sum2(100))
print(f"Total Time: {t4 - t3}")
