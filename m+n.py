NA = -1
def movToEnd(a):

    i = 0
    j = len(a) - 1

    for i in range(len(a)-1, -1, -1):
        if a[i]!= NA:
            a[j] = a[i]
            j -= 1

    return j

def merge(a,b,fi):
    i = 0
    j = 0
    while i < len(a):
        if b[j] < a[fi] or fi == i:
            a[i] = b[j]
            i += 1
            j+=1
        else:
            a[i] = a[fi]
            if  fi != len(a)-1:
                fi = fi + 1
            i += 1

a = [2, 8, NA, NA, NA, 13, NA, 15, 20]
b = [5, 7, 9, 25]

first_index = movToEnd(a) + 1


merge(a, b, first_index)

print(a)

def print(a):

    i = 0
    for i in range(len(a)):
        print(a[i])
