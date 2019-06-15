def swap_case(s):
    new_s = ""
    for c in s:
        if c.islower():
            new_s += c.capitalize()
        elif c.isupper:
            new_s += c.lower()
        else:
            new_s += str(c)
    return new_s

if __name__ == '__main__':
    while True:
        s = input()
        if 0 < len(s) <= 1000:
            result = swap_case(s)
            print(result)
            break
        else:
            print("Not a valid string !!! Re-enter the string")