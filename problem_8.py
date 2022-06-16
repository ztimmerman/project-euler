#Problem 8: Find the largest product in a 1000-digit number
#First, we might as well process the number from its original
# string form into a list of numbers.
#We can make an optimization by remembering what was the greatest
#multiple and its position, and save the current multiple, dividing by
#the first element whenever we move the cursor.

adjacentDigits = 13
f_string = ""
with open("problem_8.txt",'r') as f:
    for l in f.readlines():
        f_string+=l.strip()

greatestProduct = 0
for x in range(0,len(f_string)-adjacentDigits):
    str_slice = f_string[x:x+adjacentDigits]
    #Anything times 0 is 0, not worth bothering to calculate
    if '0' in str_slice:
        continue
    currentProduct = 1
    for c in str_slice:
        currentProduct*=int(c)
    if currentProduct > greatestProduct:
        greatestProduct=currentProduct
print(greatestProduct)
