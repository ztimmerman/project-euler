#Stitches together primes retrieved from https://www.utm.edu/staff/caldwell/primes/millions/

import os

start = 1
end = 15
primes = []
print(os.getcwd())
for file_no in range(start,end+1):
    print('primes{}'.format(file_no))
    with open("./utm-prime-stitcher/primes{}.txt".format(file_no),'r') as f:
        lines = f.readlines()
        lines = lines[2:]
        lines = [x.strip() for x in lines]
        for l in lines:
            [primes.append(int(x)) for x in l.split()]

print("length:",len(primes))
with open("primes_utm.txt",'w') as f:
    for p in primes:
        f.write(str(p)+"\n")
