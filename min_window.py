from collections import  Counter
string = "ADOBECODEBANC"
pattern = "ABC"

# string = string.replace(" ", "")
dict1 = dict()
# frequency map for pattern
patter_count = 0

for letter in pattern:
    if letter in dict1:
        dict1[letter] += 1
        patter_count += 1
    else:
        dict1[letter] = 1
        patter_count += 1

match_count = 0
dict_string = dict()
result_string = ""
final_str = ""
i = 0
j = 0
set_s = Counter(string)
set_t = Counter(pattern)
if not len(string) < len(pattern) and not(set_t - set_s ):
    while j in range(len(string)) and i < len(string):

        # Acquire
        while match_count < patter_count and i < len(string):
            if string[i] in dict_string:
                dict_string[string[i]] += 1
            else:
                dict_string[string[i]] = 1

            # inncrease match count only when it is less then equal to dict1 count
            if string[i] in dict1 and dict_string[string[i]] <= dict1[string[i]]:
                match_count = match_count + 1
            # adding letter in resultant string
            result_string += string[i]
            i += 1

        #  for the very first time assign resultant sting to final string
        if not final_str:
            final_str = result_string

        # release
        while match_count == patter_count:
            if string[j] not in dict1:
                dict_string[string[j]] -= 1
                result_string = ''.join(result_string.split(string[j], 1))
                if len(result_string) < len(final_str):
                    final_str = result_string
                j += 1

            #  if letter present in string
            elif string[j] in dict1:
                # if letter is not in access then only substract the match count
                if dict_string[string[j]] <= dict1[string[j]]:
                    match_count -= 1
                    result_string = ''.join(result_string.split(string[j], 1))
                    dict_string[string[j]] -= 1
                    j += 1
                    break
                else:
                    dict_string[string[j]] -= 1
                    result_string = ''.join(result_string.split(string[j], 1))
                    if len(result_string) < len(final_str):
                        final_str = result_string
                    j += 1
    print(final_str)
else:
    print(final_str)
