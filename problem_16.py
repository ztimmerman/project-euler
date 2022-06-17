#Problem 16: what is the sum of the digits of 2^1000?

#Return the result of multiplying list l by number n
def f_listMultiply(l,n):
    carry = 0
    new_l = [0 for x in range(len(l))]
    for x in range(len(l)-1,-1,-1):
        result = n * l[x] + carry
        new_l[x] = result % 10
        carry = result // 10
    while carry > 0:
        new_l = [carry % 10] + new_l
        carry = carry // 10
    return new_l

product = [1]
for x in range(1000):
    product = f_listMultiply(product,2)
print(sum(product))