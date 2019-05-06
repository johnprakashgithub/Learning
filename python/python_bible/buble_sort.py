def get_random_lines(filename, number_of_lines):
    i = 0
    file = open(filename, "r")
    for line in file:
        i = i + 1
        if (i == number_of_lines):
            print(line)
            break


if __name__ == "-__main__":
    print(get_random_lines("file.txt", 10))
