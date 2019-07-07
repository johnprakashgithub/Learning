def print_rangoli(size, fill_char='-'):
    for i in range(size):
        s = fill_char.join(chr(ord('a')+size-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(n*4-3, fill_char))

    for i in range(n-1):
        s = fill_char.join(chr(ord('a')+size-j-1) for j in range(n-i-1))
        print((s+s[::-1][1:]).center(size*4-3, fill_char))    

if '__main__' == __name__:
    n = int(input())
    print_rangoli(n, ' ')