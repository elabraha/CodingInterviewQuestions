# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative
# numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
# give 3.
#
# You can modify the input array in-place.
#
import math

# This is probably a bad way to do it but there really isn't any clarification
# besides what is given above and so I only have my assumptions.
def lowest_positive(arr):
    min_ = [math.inf for _ in range(len(arr))]
    for n in arr:
        shift = False
        temp = math.inf
        for k in range(len(min_)):
            if n < min_[k] and not shift:
                temp = min_[k]
                min_[k] = n
                shift = True
                continue
            elif shift:
                new_temp = min_[k]
                min_[k] = temp
                temp = new_temp
    prev = min_[0]
    for i in range(1 , len(min_)):
        if min_[i] - prev >= 2:
            for j in range(1, min_[i] - prev):
                if (prev + j) > 0:
                    return prev + j
        prev = min_[i]
    return min_[len(min_) - 1] + 1

def main():
    arr = [3, 4, -1, 1]
    print("given example:", arr)
    print("result:", lowest_positive(arr))
    arr = [1, 2, 0]
    print("given example:", arr)
    print("result:", lowest_positive(arr))

main()
