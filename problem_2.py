#Find even terms in the Fibonacci sequence whose values do not exceed 4 million
import time

sumOfEvenFibonaccis = 2
fibA = 1
fibB = 2
limit = 4000000
start_time = time.time()
while fibB <= limit:
    temp = fibB
    fibB = fibA + fibB
    fibA = temp
    if fibB % 2 == 0:
        sumOfEvenFibonaccis += fibB

end_time = time.time()
print('Solution:',sumOfEvenFibonaccis)
print('Solved in',end_time - start_time,'seconds')

#As gone through in the guide, this is a somewhat inefficient method, but it still
#calculated in 2.74*10^-5 seconds, so that's fast enough for me.