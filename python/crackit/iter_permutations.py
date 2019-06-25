from itertools import permutations

if '__main__' == __name__:
    s, k = input().split()
    for per in sorted(list(permutations(s, int(k)))):
        print("".join(per))
