# for _ in range(int(input())):
#     s = input()
#     t = input()
#     dict_s = dict()
#
#     for letter in s:
#         if letter in dict_s:
#             dict_s[letter] = dict_s[letter] + 1
#         else:
#             dict_s[letter] = 1
#
#     result = 'B'
#
#     for letter in dict_s:
#
#         if (letter not in t) and dict_s[letter] > 1:
#             result = 'A'
#             break
#
#
#     print(result)
# cook your dish here
t = int(input())

for i in range(t):
    a = input()
    b = input()
    u1 = set(a) - set(b)
    u2 = set(b) - set(a)
    for j in (u1):
        if a.count(j) > 1:
            x = 1
            break
        else:
            x = 0
    if not u1:
        print("B")
    elif u1 and not u2:
        print("A")
    elif x == 1:
        print("A")
    else:
        print("B")