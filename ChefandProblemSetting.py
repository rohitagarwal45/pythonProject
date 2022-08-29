t = int(input())

a = list()
for i in range(t):

    n, m = map(int, input().split())
    for j in range(n):

        ele = input().split()
        a.append(ele)
    a.sort()
    for k in range(n):
        word = a[k][0]
        number = a[k][1]
        # print(number)

        # print(number_list)
        output = "FINE"
        if word == "correct" and "0" in number:
            output = "INVALID"
            break
        elif word == 'wrong' and "0" not in number:
            output = 'WEAK'
            break

    a.clear()
    print(output)

