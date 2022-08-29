for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split(" "))

    min = abs(d - b) + abs(c - a)
    output = 'NO'
    if k >= min:
        if min % 2 == 0 and k % 2 == 0:
            output = 'YES'
        elif min % 2 == 1 and k % 2 == 1:
            output = 'YES'

    print(output)
