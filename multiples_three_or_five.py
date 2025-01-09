"""
3 or 5 bellow 10 => 3,5,6,9 sum = 23

find  3 multiples
find 5 multiples
"""
three_multiples = []
five_multiples = []
result_list = []

for i in range(3,1000):
    if (i%3 == 0) or (i%5 == 0):
        result_list.append(i)


print("The sum is :" , sum(result_list))    

