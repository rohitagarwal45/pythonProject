t = int(input())

for loop1 in range(t):
    n, k = input().split()

    no_of_round = 0

    a = input().split()
    while len(a)!= 0:
        count = 0
        i = 0
        if  int(a[i]) > int(k):
            no_of_round = -1
            break
        else:
            while count < int(k) and len(a)!= 0:
                count = count + int(a[i])
                if  count <= int(k):
                    del a[i]
                    # i = i + 1

            no_of_round = no_of_round + 1
    a.clear()
    print(no_of_round)





