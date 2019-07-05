from itertools import combinations_with_replacement

if '__main__' == __name__:
    s, k = input().split()
    for per in sorted(list(combinations_with_replacement(sorted(s), int(k)))):
        print("".join(per))
