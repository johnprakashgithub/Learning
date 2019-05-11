# Task 
# ================================================================================
# Read two integers from STDIN and print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Input Format
# The first line contains the first integer, . The second line contains the second integer, .
# Constraints
 

# Output Format
# Print the three lines as explained above.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    tpt = pow(10, 10) + 1
    if (a in range(1, tpt) and b in range(1, tpt)):
        sum = a + b
        diff = a - b
        prod = a * b
        print("{}\n{}\n{}".format(sum, diff, prod))
    else:
        print("Wrong input!!!")