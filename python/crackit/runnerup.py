# ==============================================================================
# Problem
# ==============================================================================
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
# Input Format
# The first line contains . The second line contains an array   of  integers each separated by a space.
# Constraints
#
#
# Output Format
# Print the runner-up score.
# Sample Input 0
# 5
# 2 3 6 6 5
# Sample Output 0
# 5
# Explanation 0
# Given list is [2, 3, 6, 6, 5] The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if n < 2 or n > 10:
        exit(0)
    p = list(arr)
    m = p[0]
    r = -100
    for i in p:
        if i < -100 or i > 100:
            continue
        if i > m:
            r = m
            m = i
        elif r <= i < m:
            r = i

    if m != r:
        print(r)


# def runnerup(p):
#     if p > max:
#         runnerup = max
#         max = p
#     return runnerup
