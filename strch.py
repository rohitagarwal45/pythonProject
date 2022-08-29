# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     string, x = input().split()

# cook your dish here
for i in range(int(input())):
    n=int(input())
    a,b=input().split()
    c,res=0,0
    for i in range(n):
        if a[i]==b:
            c=i+1
        res+=c
    print(res)