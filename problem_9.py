#Problem 9: Find the Pythagorean Triplet
#This one's a bit weird
#Pythagorean triplet: 3 natural numbers for which a^2 + b^2 = c^2
#There is one triplet for which a+b+c=1000
#Find a*b*c
import math

limit=1000
found=False
for a in range(1,limit-2):
    a2 = a*a
    for b in range(a,limit-a+1):
        b2 = b*b
        c = limit - (a+b)
        if (c*c == a2+b2) and (a+b+c==1000):
            print(a*b*c)
            found=True
            break
    if found:
        break