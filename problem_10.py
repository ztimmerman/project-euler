#Find the sum of all primes less than 2,000,000
limit = 2000000

primes = []
with open("primes.txt",'r') as f:
    for l in f.readlines():
        primes.append(int(l.strip()))

if len([x for x in primes if x >= limit]) == 0:
    raise Exception('Prime number file too small, generate a bigger one and try again.')

print(sum(x for x in primes if x < limit))