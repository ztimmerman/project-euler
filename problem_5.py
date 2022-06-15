#What is the smallest positive number that is evenly divisible by all numbers from 1 to 20?
primes = [2,3,5,7,11,13,17,19]

#Returns a dictionary of prime factors and their powers for the given number
def f_primeFactorize(n):
    global primes
    if n in primes:
        return {n:1}
    factorDict = dict()
    for p in primes:
        if n < p:
            return factorDict
        while n % p == 0:
            if p not in factorDict:
                factorDict[p]=1
            else:
                factorDict[p]+=1
            n = n//p
    return factorDict

if __name__ == '__main__':
    primeFactorDict = dict()
    for n in range(1,21):
        newFactorDict = f_primeFactorize(n)
        for k in newFactorDict:
            if k not in primeFactorDict:
                primeFactorDict[k]=newFactorDict[k]
            elif primeFactorDict[k] < newFactorDict[k]:
                primeFactorDict[k]=newFactorDict[k]
    evenlyDivisibleNumber = 1
    for k in primeFactorDict:
        evenlyDivisibleNumber*=k**primeFactorDict[k]
    print(evenlyDivisibleNumber)