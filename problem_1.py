#This is basically the classic fizz buzz problem
#Threes are fizz, fives are buzz
#Find the sum of all multiples of 3, and multiples of 5, that aren't multiples of both
import time
start_time = time.time()
fizzList = [x for x in range(0,1000,3)]
buzzList = [x for x in range(0,1000,5)]
fizzBuzzList = [x for x in range(0,1000,15)]
#print('threes:',sum(fizzList))
#print('fives:',sum(buzzList))
#print('fifteens:',sum(fizzBuzzList))
#Subtracting the sum of the multiples of 15 gets rid of the 
print('Solution:',sum(fizzList)+sum(buzzList)-sum(fizzBuzzList))
sect1_time = time.time()
print('Solved in ',sect1_time-start_time,'seconds')

#This solution was very RAM inefficient and not terribly scalable.
#Let's try a different solution that's a bit more efficient.
threesSum, fivesSum, fifteensSum = (0,0,0)
for x in range(0,1000,3):
    threesSum += x
for x in range(0,1000,5):
    fivesSum += x
for x in range(0,1000,15):
    fifteensSum += x
sect2_time = time.time()
print('Solution:',threesSum+fivesSum-fifteensSum)
print('Solved in',sect2_time-sect1_time,'seconds')

#This solution, while taking very little RAM, takes 20% longer than the first solution (i7-720Q)
#Printout below
#Solution: 233168
#Solved in  0.00039887428283691406 seconds
#Solution: 233168
#Solved in 0.0005037784576416016 seconds
