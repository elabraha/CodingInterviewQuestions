# Given an array of integers, return a new array such that each element at index
# of the new array is the product of all the numbers in the original array
# except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
# be [2, 3, 6].
# Follow up: what if you can't use division

# I had this before excluding the zero edge case. the zero esge case makes
# this look very ugly.
def product_of_list(nums):
    if len(nums) < 2:
        return nums
    product = 1
    zeros = 0
    new_arr = []
    for n in nums:
        if n == 0:
            zeros += 1
            continue
        product *= n
    if zeros > 1:
        return [0 for _ in range(len(nums))]
    for n in nums:
        if zeros == 1:
            if n == 0:
                new_arr.append(product)
            else:
                new_arr.append(0)
        else:
            new_prod = product / n
            new_arr.append(new_prod)
    return new_arr

def product_list_no_division(nums):
    # This one is o(n^2) please let me know if there is a better way to do this
    # without division
    new_arr = [1 for _ in range(len(nums))]
    for x, n in enumerate(nums):
        for i in range(len(new_arr)):
            if x!= i:
                new_arr[i] *= n
    return new_arr

def main():
    nums = [1, 2, 3, 4, 5]
    comp = [120, 60, 40, 30, 24]
    nums = [3,2,1]
    comp = [2,3,6]
    nums = [0, 1, 2, 0]
    comp = [0, 0, 0, 0]
    nums = [0, 1, 2, 3]
    nums = [6, 0, 0, 0]
    # if product_of_list(nums) == comp:
    #     print("Correct!")
    # else:
    #     print("Incorrect.")
    if product_list_no_division(nums) == comp:
        print("Correct!")
    else:
        print("Incorrect.")

main()
