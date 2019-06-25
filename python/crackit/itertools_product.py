from itertools import product

if '__main__' == __name__:
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(" ".join(map(str, list(product(A, B)))))

