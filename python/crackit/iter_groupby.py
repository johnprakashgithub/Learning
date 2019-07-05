from itertools import groupby

if '__main__' == __name__:
    items = [(len(list(k)), int(c)) for c, k in groupby(str(input()))]
    result = ""
    for item in items:
        result += str(item) + " "
    print(result)