a = list(map(int, input().split(", ")))
dict = dict()
count = 0
for i in range(len(a)):

    if a[i] in dict:
        dict[a[i]] = dict[a[i]] + 1
    else:
        dict[a[i]] = 1

    if count < dict[a[i]]:
        count = dict[a[i]]
        element = a[i]
if count > len(a)/2:
    print(element)
else:
    print("No Majority Element")

