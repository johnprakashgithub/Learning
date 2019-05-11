if __name__ == '__main__':
    a = int(input())
    if a in range(1, 21):
        for i in range(0, a):
            print(i*i)
    else:
        print("Wrong input!!!")