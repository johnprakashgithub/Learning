# z = x + yj

import cmath

if __name__ == '__main__':
    z = complex(input())
    e = cmath.phase(z)
    r = abs(complex(z))
    print(r)
    print(e)
