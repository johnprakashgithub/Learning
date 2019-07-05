def design(row):
    d = ""
    for i in range(0, row):
        d += ".|."
    return d

def line(m):
    l = ""
    for i in range(0, m):
        l += "-"
    return l

def draw(m, substring):
    start_pos = int(m/2) - int(len(substring)/2)
    end_pos = start_pos + len(substring)
    return line(start_pos) + substring + line(start_pos)

if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)
    row_half = int(n/2)
    init = 1
    for i in range(0, int(n)):
        if i < row_half:
            print(draw(m, design(init)))
            init += 2
        elif i == row_half:
            print(draw(m, "WELCOME"))
        else:
            init -= 2
            print(draw(m, design(init)))
