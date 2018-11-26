# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 id 17
# Bonus: Can you do this in one pass?

def add_to_k(nums, k):
    diffs = set()
    for n in nums:
        diff = k - n
        if n in diffs:
            return True
        else:
            diffs.add(diff)
    return False
def main():
    # call my function
    nums = [10, 15, 3, 7] # only exists one
    nums = [9, 15, 4, 6] # exists none
    nums = [7, 2, 1, 10] # in a different order
    nums = [10, 15, 2, 7] # more than one
    nums = [] # empty
    nums = [15, 2] # only 2 nums and both add to k
    nums = [18, -1, 1, 14] # negative numbers
    k = 17
    print(nums)
    if add_to_k(nums, k):
        print("Yayyy! There is exists 2 numbers that add to", k)
    else:
        print("NOOOOOOO!! There aren't any numbers in the list that add to", k)
main()
