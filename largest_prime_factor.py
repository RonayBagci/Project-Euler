"""
13195 => 5,7,13,29
"""

results = []      

def find_max_prime_numbers(num):  
    remainder = num
    division = 2
    while (remainder != 1):
        if remainder % division == 0:
            remainder = remainder/division
            if division not in results:
                results.append(division)
        else:
            division += 1
            
    return results

print(find_max_prime_numbers(600851475143))
