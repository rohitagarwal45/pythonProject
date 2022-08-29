t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    set_of_a = set(a)
    if 0 in set_of_a:
        print(len(set_of_a) - 1)
    else:
        print(len(set_of_a))
