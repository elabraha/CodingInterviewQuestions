# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as
# 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example,
# '001' is not allowed.

# There is a harder version on leetcode with 0 that was going to try and do but
# I don't understand yet what effect it has. I might have to do recursion.
# I will do that one in this question as well but later.

def decode_ways(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        return 2
    letters = 26 # not sure if this number actually matters
    ways = [0 for _ in range(len(s))]
    ways[0] = 1
    ways[1] = 2
    for n in range(2, len(ways)):
        ways[n] = ways[n - 1] + ways[n -2]
    return ways[len(ways) - 1]

def main():
    message = '1111'
    print(decode_ways(message))

main()
