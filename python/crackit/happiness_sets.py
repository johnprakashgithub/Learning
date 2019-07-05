if __name__ == '__main__':
    n, m = map(int, input().split())
    nset = set(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    smiles = sum((e in a) - (e in b) for e in nset)
    print(smiles)