#Problem 13: find the first ten digits of the sum of the following 100 50-digit numbers

#Easily the most hacky solution yet. We just make the difference of the succeeding numbers
#insignificant enough such that they can't possibly effect the first 10 numbers.
#Going to add the first 14 digits does the trick. This is because 9 * 50 is 450,
#and you can, at best, carry 1 in a summation of 2 1-digit numbers
with open("problem_13.txt",'r') as f:
    nums = [x.strip() for x in f.readlines()]

numSum = sum(int(x[:14]) for x in nums)
print(str(numSum)[:10])