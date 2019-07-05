def count_substring(string, sub_string):
    index = string.find(sub_string)
    if index == -1:
        return 0
    else:
        return count_substring(string[index+1:], sub_string) + 1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)