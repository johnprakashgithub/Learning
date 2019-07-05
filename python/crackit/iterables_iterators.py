from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    S = list(input().split())
    K = input()
    if 0 < int(K) < N + 1:
        print("N is {}, S is {} and K is {}".format(N, S, K))
        print(list(combinations(S, 2)))
