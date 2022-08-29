# 1.	Remove duplicates from string
def duplicare():
    str = input()
    seta = set()
    str1 = " "
    for letter in str:
        seta.add(letter)
    for i in seta:
        str1 = str1 + i
    print(str1)

# 2.	Remove characters from the first string which are present in the second string
def del_str2_in_str1():
    str1 = input("enter string1")
    str2 = input("Enter string 2")
    set1 =set()
    set2 =set()

    set1 = set(str1)
    set2 = set(str2)
    print(f"{set1 - set2}")

# del_str2_in_str1()

# 3.	Check if strings are rotations of each other
def check_rotation():
    str1 = input()
    str2 = input()
    list1 = list()
    if len(str1) == len(str2):

        if str1[0] in str2:
            for k in range(len(str2)):
                if str2[k] == str1[0]:
                    list1.append(k)
                else:
                    continue
        flag = False
        for ele in list1:

            # j = str2.index(str1[0])
            j = ele
            i = 1
            flag = True
            while i != len(str1):
                if str1[i] == str2[(j+1) % len(str2)]:
                    i+=1
                    j+=1
                else:
                    flag = False
                    break
            if flag:
                print('string are rotation of each other ')
                break

        if flag == False:
            print('string are not rotation of each other ')

    else:
        print('string are not rotation of each other ')

# check_rotation()

# 4.	Print all permutations of a given string
def permutation():

    def permute(a,l,r):

        if l == r:
            print(''.join(a))
            # print(a)
        else:
            for i in range(l,r):
                a[l],a[i] = a[i],a[l]
                permute(a,l+1,r)
                a[l],a[i] = a[i],a[l]

    s = input("Enter string with non duplicate one ")
    lenth = len(s)

    print(f"Entered string is {s}")

    list_s = list(s)
    print(f"list s is {list_s}")
    permute(list_s,0,lenth)


    # def toString(List):
    #     return ''.join(List)
    # def permute(a, l, r):
    #     if l == r:
    #         print(toString(a))
    #     else:
    #         for i in range(l, r):
    #             a[l], a[i] = a[i], a[l]
    #             permute(a, l + 1, r)
    #             a[l], a[i] = a[i], a[l]  # backtrack
    #
    # # Driver program to test the above function
    # string = "ABC"
    # n = len(string)
    # a = list(string)
    # permute(a, 0, n)

# permutation()

# 5.	Reverse words in a given string

def reverse_word():

    # s = []
    # s = input().split(" ")
    # print(s)
    #
    # for i in range(int(len(s) / 2)):
    #     s[i],s[len(s)-1 - i] = s[len(s)-1 - i],s[i]
    # print(f"after reverse : {' '.join(s)}")
    s = "a good   example"

    # s = s.strip()

    s = " ".join(s.split())
    s1 = list(s.split(" "))
    # print(s)

    for i in range(int(len(s1) / 2)):
        s1[i], s1[len(s1) - 1 - i] = s1[len(s1) - 1 - i], s1[i]
        # return (''.join(s1))
    print(f"after reverse : {' '.join(s1)}")


reverse_word()





