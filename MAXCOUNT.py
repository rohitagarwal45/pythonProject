t = int(input())

a = list()
dictionary = dict()
for x in range(t):
    n = int(input())
    # for y in range(n):
    a = input().split( )

    for item in a:
        if item in dictionary:
            dictionary[item] = dictionary[item] + 1
        else:
            dictionary[item] = 1

    # print(dictionary)
    max_no = 0
    lv_element = 0
    # print(type(max_no))

    for element in dictionary:

        if max_no < int(dictionary[element]):
            max_no = int(dictionary[element])
            lv_element = element
        elif max_no == int(dictionary[element]):
            if int(lv_element) > int(element):
                lv_element = element

    dictionary.clear()

    print(f" {lv_element} {max_no}")



