# Given a list of integers, write a function that returns the largest sum of 
# non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, since we pick 5 and 5. [5, 1, 1, 5, 6]

# Follow-up: Can you do this in O(N) time and constant space?

def largest_sum(l):
	exprev = 0
	incprev = 0
	running_max = 0
	for curr in l:
		print("before:", running_max, incprev, exprev)
		running_max = max(exprev, incprev)
		temp = exprev + curr
		exprev = running_max
		incprev = temp
		print("after:", running_max, incprev, exprev)
	return max(exprev, incprev)


def main():
	lusty = [5, 1, 1, 5, 6]
	print(largest_sum(lusty))

main()