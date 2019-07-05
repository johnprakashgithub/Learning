from itertools import combinations

if '__main__' == __name__:
    s, k = input().split()
    for ki in range(1, int(k)+1):
        for per in sorted(list(combinations(sorted(s), ki))):
            print("".join(per))
