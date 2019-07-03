from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoes = Counter(map(int, input().split()))
    N = int(input())
    earn = 0
    for _ in range(N):
        size, price = map(int, input().split())
        if shoes[size]:
            shoes[size] -= 1
            earn += price
    print(earn)

