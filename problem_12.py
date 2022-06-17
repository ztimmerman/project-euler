#Problem 12: find first triangular number with over 500 divisors
#First, let's find the first number to have over 500 divisors
#It's fairly quick to divise prime factors, so let's start with those

import time, math

#Returns a prime factor dictionary for a given number n
def f_getPrimeFactorDictionary(n):
    prime_factor_dictionary = dict()
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor in prime_factor_dictionary:
                prime_factor_dictionary[divisor] += 1
            else:
                prime_factor_dictionary[divisor] = 1
            n = n // divisor
        divisor += 1
    return prime_factor_dictionary

def f_getFactors(n):
    factors = [1,n]
    divisor = 2
    n_sqrt = math.sqrt(n)
    while divisor < n_sqrt:
        if n % divisor == 0:
            factors.append(divisor)
            factors.append(n//divisor)
        divisor+=1
    if divisor == n_sqrt and n % divisor == 0:
        factors.append(divisor)
    return factors

max_factors = 0
max_factors_num = 0
triangular_val = 1
triangular_counter = 2
start_time = time.time()
while max_factors < 500:
    curr_factors = f_getFactors(triangular_val)
    if len(curr_factors) > max_factors:
        max_factors = len(curr_factors)
        max_factors_num = triangular_val
        print("New max: {}".format((max_factors,max_factors_num)))
    triangular_val += triangular_counter
    triangular_counter += 1
    
end_time = time.time()
print(max_factors,max_factors_num)
print(end_time-start_time)
