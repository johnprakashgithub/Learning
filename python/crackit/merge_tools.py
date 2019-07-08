
def merge_the_tools(string, k):
    # your code goes here
    t = [ string[k*i:k*(i+1)] for i in range(int(len(string)/k))]
    result = ""
    for ti in t:
        w = ""
        for c in ti:
            if w.count(c) == 0:
                w += c
        result += w + "\n"
    print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)