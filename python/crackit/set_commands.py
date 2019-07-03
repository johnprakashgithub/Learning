n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    cmd = [x for x in input().split()]
    if len(cmd) == 1:
        getattr(s, cmd[0])()
    elif len(cmd) == 2:
        getattr(s, cmd[0])(int(cmd[1]))
print(sum(s))

# n, s = int(input()), set(map(int, input().split()))
# # [(lambda x: getattr(s, x[0])(*map(int, x[1:])))(input().strip().split()) for _ in range(int(input().strip()))]
# # print(sum(s))