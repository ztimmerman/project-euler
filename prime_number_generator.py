#basic prime number generator, writes to primes.txt

import math

desiredCount = 1000000
primes = [2,3]
n = 5 #current number being tested
while len(primes) < desiredCount:
    isPrime = True
    n_sqrt = int(math.sqrt(n))
    for p in primes:
        if p > n_sqrt:
            break
        if n % p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(n)
        print(n)
    n += 2

with open("primes.txt","w") as f:
    for p in primes:
        f.write(str(p)+"\n")