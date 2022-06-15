#Find the largest prime factor of a very large number
import math
import time
composite = 600851475143
#largest possible prime factor of a number n is n/2
#all numbers have factors of 1 and n, and 2 is the smallest prime
#Because factors are always in pairs, n/2 is the complement of 2,
#and thus the largest possible prime factor
largest_prime = 0
#Algorithm divides the composite by any factor it finds divisible
#As it starts with 2, and the algorithm divides any factors of a
#divisible factor it finds (e.g. 8=2*2*2), the next divisible number
#will always be prime.
start_time = time.time()
while composite > 1:
    for x in range(2,composite,1):
        if composite % x == 0:
            print('Factor:',x)
            if x > largest_prime:
                largest_prime = x
            while composite % x == 0:
                composite = composite // x
            print('Composite:',composite)
        #Solution found, save time by not iterating in the loop
        #longer than necessary
        if composite == 1:
            break
end_time = time.time()
print("Largest prime:",largest_prime)
print("Solved in",end_time-start_time,'seconds')
