t = int(input())

for j in range(t):
    r, g, b = map(int, (input().split()))
    k = int(input())

    max_val = r
    if r < g and g > b:
        max_val = g
    elif r < b and b > g:
        max_val = b

    count = 0
    i = 0
    count1 = count2 = count3 = 0
    while not(count1 == k or count2 == k or count3 == k):
        i = i + 1
        if r != 0
            if (i % 3 == 1):
                r = r - 1
                count = count + 1
                count1 = count1 + 1
        else
            i = i -1



        if g != 0 and (i % 3 == 2):
            g = g - 1
            count = count + 1
            count2 = count2 + 1

        if b != 0 and (i % 3 == 0):
            b = b - 1
            count = count + 1
            count3 = count3 + 1


    print(f"{count} \n")
