'''
Trailing zeroes are caused by pairs of fives and twos. If I find the number of fives,
and the number of twos, the lesser will be the number of 'pairs.'
'''

def zeros(num):
    num_of_5 = 0
    num_of_2 = 0
    x = 1
    # print(num // (5**x))
    # print(num // (2**x))
    while ((num // (5**x)) >= 1):
        num_of_5 += (num // (5**x))
        x += 1
    x = 1
    while ((num // (2**x)) >= 1):
        num_of_2 += (num // (2**x))
        x += 1
    return num_of_2 if num_of_5 >= num_of_2 else num_of_5

print(zeros(6))
