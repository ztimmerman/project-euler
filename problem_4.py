#Find the largest palindrome number that is the product of 2 3-digit numbers

import time

def f_isPalindromeNumber(n):
    str_n = str(n)
    len_str_n = len(str_n)
    if len_str_n % 2 == 0:
        if str_n[:len_str_n//2] == str_n[len_str_n//2:][::-1]:
            return True
    else:
        if str_n[:len_str_n//2+1] == str_n[len_str_n//2:][::-1]:
            return True
    return False

#whatever is the largest palindrome will be the product of the highest possible factors
largestPalindrome=0
start_time  = time.time()
for a in range(999,100,-1):
    #setting a as the lower bounds of b prevents repeats
    for b in range(999,a,-1):
        c=a*b
        if c <= largestPalindrome:
            break
        if f_isPalindromeNumber(c):
            if largestPalindrome<c:
                largestPalindrome=c
end_time=time.time()
print(largestPalindrome)
print('Solved in',end_time-start_time,'seconds')
