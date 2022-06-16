#Already solved unintentionally by generating the first 1000000 prime numbers
with open("primes.txt",'r') as f:
    primes = [int(x) for x in f.readlines()]

searchTarget = 10001
print(primes[searchTarget-1])