# Function is to check whether two strings are anagram of each other or not.
class Solution:
    def isAnagram(self, a, b):
        if sorted(a) == sorted(b):
            return True
        else:
            return False


# {
#  Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(str, input().strip().split())
        print(f"{sorted(a)}")
        print(type(sorted(a)))
        if (Solution().isAnagram(a, b)):
            print("The two strings are anagram of each other")
        else:
            print("The two strings are not anagram of each other")
# } Driver Code Ends


# from collections import Counter
#
# s = "a"
# t = "ab"
#
# dict_s = Counter(s)
# dict_t = Counter(t)
#
# if dict_s - dict_t or dict_t - dict_s:
#     print("false")
# else:
#     print("true")