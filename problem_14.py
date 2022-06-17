#Problem 14: what starting number, under 1,000,000
#produces the longest Collatz chain?

#Tuple is structure (what number leads to,length)
collatz_sequences = {1:(1,1)}

def f_getCollatzLength(n):
    #print(n)
    global collatz_sequences
    if n in collatz_sequences:
        return collatz_sequences[n][1]
    else:
        if n % 2 == 0:
            collatzLength = f_getCollatzLength(n//2) + 1
            collatz_sequences[n]=(n//2,collatzLength)
        else:
            collatzLength = f_getCollatzLength(3*n+1) + 1
            collatz_sequences[n]=(3*n+1,collatzLength)
        #print(n,':',collatz_sequences[n])
        return collatzLength

max_collatz_length = 10
max_collatz_num = 13
for x in range(999999,0,-1):
    curr_collatz_length = f_getCollatzLength(x)
    if curr_collatz_length > max_collatz_length:
        max_collatz_length = curr_collatz_length
        max_collatz_num = x
        print(max_collatz_num,max_collatz_length)

print(max_collatz_num,max_collatz_length)
print('len:',len(collatz_sequences))