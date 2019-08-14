from itertools import combinations_with_replacement

if __name__ == '__main__':
    string = input()
    num = int(input())
    
    output =  {"".join(per) for per in set(combinations_with_replacement(string,num))}
    print(output)
