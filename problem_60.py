# Problem 60: Prime Pair sets
# Find combinations of string concatenations which are themselves prime

from functools import reduce
import time

with open("primes_utm.txt",'r') as f:
    primes_str_l = [x.strip() for x in f.readlines()]

#Speedhack: remove 2 and 5 as they will never produce a prime pair set
primes_str_l = primes_str_l[:2] + primes_str_l[3:] #Remove 5
primes_str_l = primes_str_l[1:] #remove 2
#Experimental: limit to first 1000 primes
#primes_str_l = primes_str_l[:10000]

#Returns a list of prime pair tuples, 
# ** TOO SLOW **
def f_findPrimePairs():
    global primes_str_l
    prime_pairs = []
    for x in range(len(primes_str_l)-1):
        n = primes_str_l[x]
        if n not in ['2','5']:
            for y in range(x,len(primes_str_l)):
                reducedPrimes = primes_str_l[y+1:]
                if len(reducedPrimes) == 0:
                    print("Out of options!")
                    continue
                m = primes_str_l[y]
                nM = n + m
                mN = m + n
                if len(nM) > len(reducedPrimes[-1]):
                    print("Too long!")
                    continue
                if nM in reducedPrimes:
                    if mN in reducedPrimes:
                        print((n,m))
                        prime_pairs.append((n,m))
    return prime_pairs

#Start at position 1 because 2 will never create a prime pair set
#Parameters:
#   limit: how big is the set you want to find
#
def f_findLowestPrimePairSet(limit,prime_pair_set=[],position=0):
    global primes_str_l
    count = len(prime_pair_set)
    if count == limit:
        return prime_pair_set
    #list of all primes in primes_str_l that are also ahead of n
    #Speedhack to reduce slicing calls
    reducedPrimeList = primes_str_l[position+1:]
    if len(reducedPrimeList) == 0:
        print("Out of options!")
        return []
    for x in range(position,len(primes_str_l)-(limit-count),1):
        n=primes_str_l[x]
        if count==0:
            returnedVal = f_findLowestPrimePairSet(limit,[n],x+1)
        else:
            #Does n pair with all primes n already in the list
            pairsWell = True
            for m in prime_pair_set:
                nM = n+m
                if len(nM) > len(reducedPrimeList[-1]):
                    #print("Too long!")
                    pairsWell = False
                    break
                if nM not in reducedPrimeList:
                    pairsWell = False
                    break
                if m+n not in reducedPrimeList:
                    pairsWell = False
                    break
            if pairsWell:
                print(prime_pair_set+[n])
                returnedVal = f_findLowestPrimePairSet(limit,prime_pair_set+[n],x+1)
            else:
                returnedVal = []
        if returnedVal != [] and returnedVal is not None:
            return returnedVal


start_time = time.time()
#prime_pairs = f_findPrimePairs()
print(f_findLowestPrimePairSet(5))
#print('Number of pairs:',len(prime_pairs))
end_time = time.time()
print(end_time-start_time,'seconds')