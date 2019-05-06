# =================================================================
# Task
# =================================================================
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints
#
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Output 0
# Weird
# Explanation 0
#
# is odd and odd numbers are weird, so we print Weird.
# Sample Input 1
# 24
# Sample Output 1
# Not Weird
# Explanation 1
# and  is even, so it isn't weird. Thus, we print Not Weird.
# =================================================================


N = int(input())


def iseven(n):
    if (n % 2) == 0:
        return True
    else:
        return False


if not iseven(N):
    print("weird")

if iseven(N) and (N in range(21, 101) or N in range(2, 5)):
    print("Not weird")

if iseven(N) and N in range(6, 21):
    print("weird")

if N < 0 or N > 100:
    print("N is out of range 1 to 100")
