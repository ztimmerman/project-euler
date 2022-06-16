#basic prime number generator, writes to primes.txt

import math
import os

desiredCount = 10001000
if os.path.exists("primes.txt"):
    with open("primes.txt","r") as f:
        primes = [int(x.strip()) for x in f.readlines()]
else:
    primes = [2,3]
n = primes[-1] + 2 #current number being tested
if len(primes) >= desiredCount:
    print("Already done!")
    exit(0)
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