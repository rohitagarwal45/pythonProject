t = int(input())
for z in range(t):

    n = int(input())
    output = list() #store final value as list
    temp = list()

    fact = n
    while n != 0:
        output.append(n % 10)
        n = int(n / 10)


    carry = 0

    i = fact - 1
    while i >= 1:
        for j in range(len(output)):
            prod = (output[j] * i) + carry
            temp.append(prod % 10)
            carry = int(prod / 10)
        while(carry > 0):
            temp.append(carry % 10)
            carry = int(carry / 10)
        output = temp.copy()
        temp.clear()
        i = i-1

    result = ""
    # output = output.reverse()
    # print(output)
    m = len(output) - 1
    while m >= 0:
        result = result + str(output[m])
        m = m-1

    print(result)
    # print(type(output))
    # print(output)



# for i in range(int(input())):
#     n = int(input())
#     result = 1
#     for j in range(n):
#         result = result * (j+1)
#     print(result)


    # We have populated the solutions for the 10 easiest problems for your support.
    # Click on the SUBMIT button to make a submission to this problem.

    # # Note that it's python3 Code. Here, we are using input() instead of raw_input().
    # # You can check on your local machine the version of python by typing "python --version" in the terminal.
    #
    # def factorial(n):
    #     if n == 0:
    #         return 1
    #     elif n == 1:
    #         return 1
    #     else:
    #         return n * factorial(n - 1)
    #
    #
    # n = int(input())
    # for i in range(n):
    #     num = int(input())
    #     print(factorial(num))




