from string import ascii_lowercase
alphabets = list(ascii_lowercase)


def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False


def draw_line(row, col):
    max_char = row/2
    placement = col/2
    for i in range(0, row):
        line = ''
        for j in range(0, col):
            cursor = 0
            if iseven(j):
                if j > max_char > i:
                    cursor += cursor
                elif j == max_char and i < max_char:
                    cursor = 0
                elif j < max_char and i < max_char:
                    cursor = max_char - cursor
                else:
                    line += "-"
                    continue
                line += alphabets[placement+cursor]
            else:
                line += "-"
        print(line)


def draw_letters(row, col):
    for i in range(0, row):
        letters = ""
        for j in range(0, i):
            letters += alphabets[i]
        print()


def print_rangoli(size):
    if not iseven(size):
        row = size * 2 - 1
        col = size * 3
        draw_line(row, col)
    else:
        print("Not valid !!! Size must be Odd number.")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)