def input_command(args, list, N):
    if args[0]:
        cmd = args[0].lower()
        pos = 0
        item = 0
    else:
        print("Invalid commmand!!!")
        return False
    if cmd == 'insert':
        if len(list) == N:
            print("{}: List is full !!!".format(cmd))
            return True
        pos = int(args[1])
        element = int(args[2])
        # print("Insert {} {}".format(pos, element))
        list.insert(pos, element)
    elif cmd == 'remove':
        if len(list) == 0:
            print("{}: List is empty !!!".format(cmd))
            return True
        element = int(args[1])
        # print("Remove {}".format(element))
        list.remove(element)
    elif cmd == 'append':
        if len(list) == N:
            print("{}: List is full !!!".format(cmd))
            return True
        element = int(args[1])
        # print("Append {}".format(element))
        list.append(element)
    elif cmd == 'print':
        print(list)
    elif cmd == 'sort':
        # print("Sort")
        list.sort()
    elif cmd == 'pop':
        if len(list) == 0:
            print("{}: List is empty !!!".format(cmd))
            return True
        # print("Pop")
        list.pop()
    elif cmd == 'reverse':
        # print("Reverse")
        list.reverse()
    else:
        print("Commmand Not found!!!")
        return False
    return True
        
if __name__ == '__main__':
    N = int(input())
    list = []
    while(True):
        command = input().split()
        if not input_command(command, list, N):
            break
