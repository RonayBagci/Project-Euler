"""
fibonacci numbers 1,2,3,5,8,13,21,34,55...

Even numbers = (Even Number + Even Number) or (Odd Number + Odd Number)

Find fibonacci numbers 1 to 4 million
Find even numbers in the list

"""

result = [1,2]
counter = 2
fibo_number = 0
answer = []

while fibo_number<4000000:
    fibo_number = result[counter-1] + result[counter-2]
    result.append(fibo_number)
    counter += 1


for i in result:
    if i%2 == 0:
        answer.append(i)

print(sum(answer))

